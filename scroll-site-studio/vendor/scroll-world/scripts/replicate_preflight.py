#!/usr/bin/env python3
"""Read-only Replicate schema checks. Never uploads files or creates predictions."""

import argparse
import json
import os
import re
import shutil
import sys
import urllib.error
import urllib.request
from pathlib import Path

MODELS = {
    "bytedance/seedance-2.0": {
        "first": "image", "last": "last_frame_image", "quality": "resolution",
        "qualities": {"480p": "480p", "720p": "720p", "1080p": "1080p", "4k": "4k"},
    },
    "kwaivgi/kling-v3-video": {
        "first": "start_image", "last": "end_image", "quality": "mode",
        "qualities": {"720p": "standard", "1080p": "pro", "4k": "4k"},
    },
}

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError("Unexpected API redirect; stopped without forwarding credentials.")

def fetch_metadata(model):
    token = os.environ.get("REPLICATE_API_TOKEN")
    if not token:
        raise ValueError("REPLICATE_API_TOKEN is not set. Configure it securely or use connected Replicate tools.")
    if not re.fullmatch(r"[A-Za-z0-9_-]+/[A-Za-z0-9_.-]+", model):
        raise ValueError("Model must be an owner/name identifier.")
    request = urllib.request.Request(
        "https://api.replicate.com/v1/models/" + model,
        headers={"Authorization": "Bearer " + token, "Accept": "application/json",
                 "User-Agent": "scroll-world-preflight/1.0"}, method="GET",
    )
    try:
        with urllib.request.build_opener(NoRedirect()).open(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        raise ValueError(f"Model metadata GET failed: HTTP {exc.code}. No generation submitted.") from None
    except urllib.error.URLError:
        raise ValueError("Model metadata GET failed: network error. No generation submitted.") from None

def resolve_schema(root, schema, trail=()):
    """Resolve local references/allOf used by Replicate's enum input properties."""
    result = {}
    if "$ref" in schema:
        ref = schema["$ref"]
        if not ref.startswith("#/") or ref in trail:
            raise ValueError("Unsupported or circular schema reference.")
        target = root
        for key in ref[2:].split("/"):
            target = target[key.replace("~1", "/").replace("~0", "~")]
        result.update(resolve_schema(root, target, (*trail, ref)))
    for part in schema.get("allOf", []):
        result.update(resolve_schema(root, part, trail))
    result.update({k: v for k, v in schema.items() if k not in ("$ref", "allOf")})
    return result

def validate_candidate(metadata, model, quality, duration, aspect):
    if model not in MODELS:
        raise ValueError("Helper maps Seedance 2.0 and Kling v3 only. Inspect other models through replicate-media.")
    mapping = MODELS[model]
    if quality not in mapping["qualities"]:
        raise ValueError(f"{quality} is not mapped for {model}.")
    if duration <= 0:
        raise ValueError("Use an explicit positive duration for a predictable flight budget.")
    version = metadata.get("latest_version") or {}
    root = version.get("openapi_schema")
    if not root:
        raise ValueError("No current input schema; inspect the model API before generation.")
    input_schema = resolve_schema(root, root["components"]["schemas"]["Input"])
    properties = input_schema.get("properties", {})
    candidate = {
        "prompt": "A continuous camera flight through the approved scene.",
        mapping["first"]: "https://example.invalid/previous-final.png",
        mapping["last"]: "https://example.invalid/destination.png",
        mapping["quality"]: mapping["qualities"][quality],
        "duration": duration, "aspect_ratio": aspect, "generate_audio": False,
    }
    missing = set(input_schema.get("required", [])) - candidate.keys()
    if missing:
        raise ValueError("New required fields need inspection: " + ", ".join(sorted(missing)))
    resolved = {}
    for field, value in candidate.items():
        if field not in properties:
            raise ValueError(f"Schema no longer exposes {field}; inspect the changed model.")
        spec = resolve_schema(root, properties[field])
        resolved[field] = spec
        kind = spec.get("type")
        valid_type = (
            (kind == "string" and isinstance(value, str))
            or (kind == "integer" and type(value) is int)
            or (kind == "number" and type(value) in (int, float))
            or (kind == "boolean" and type(value) is bool) or kind is None
        )
        if not valid_type:
            raise ValueError(f"Input type changed for {field}.")
        if "enum" in spec and value not in spec["enum"]:
            raise ValueError(f"Selected {field} value is absent from the current enum.")
        if type(value) in (int, float):
            if "minimum" in spec and value < spec["minimum"]:
                raise ValueError(f"{field} is below the model minimum.")
            if "maximum" in spec and value > spec["maximum"]:
                raise ValueError(f"{field} exceeds the model maximum.")
    return {
        "model": model, "version": version.get("id"), "official": metadata.get("is_official"),
        "first_frame_field": mapping["first"], "last_frame_field": mapping["last"],
        "quality_field": mapping["quality"], "quality_value": candidate[mapping["quality"]],
        "quality_options": resolved[mapping["quality"]].get("enum"),
        "duration": duration, "aspect_ratio": aspect, "generate_audio": False,
        "schema_check": "passed", "frame_fidelity": "not tested",
        "billing_balance": "not checked", "predictions_submitted": 0,
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default="bytedance/seedance-2.0")
    parser.add_argument("--quality", choices=("480p", "720p", "1080p", "4k"), default="1080p")
    parser.add_argument("--duration", type=int, default=8)
    parser.add_argument("--aspect", default="16:9")
    parser.add_argument("--schema-file", type=Path, help="Validate a metadata snapshot offline")
    parser.add_argument("--save-schema", type=Path, help="Save public model name/version/schema locally")
    parser.add_argument("--require-media-tools", action="store_true")
    args = parser.parse_args()
    try:
        if args.schema_file:
            metadata = json.loads(args.schema_file.read_text(encoding="utf-8-sig"))
            snapshot_model = metadata.get("model") or "/".join(
                str(metadata.get(key, "")) for key in ("owner", "name")
            )
            if snapshot_model != args.model:
                raise ValueError("Saved schema belongs to a different model.")
        else:
            metadata = fetch_metadata(args.model)
        result = validate_candidate(metadata, args.model, args.quality, args.duration, args.aspect)
        result["schema_source"] = "offline snapshot" if args.schema_file else "live metadata GET"
        result["tools"] = {tool: shutil.which(tool) for tool in ("ffmpeg", "ffprobe")}
        result["media_tools_ready"] = all(result["tools"].values())
        if args.save_schema:
            version = metadata["latest_version"]
            snapshot = {
                "model": args.model, "is_official": metadata.get("is_official"),
                "latest_version": {"id": version.get("id"), "openapi_schema": version["openapi_schema"]},
            }
            args.save_schema.parent.mkdir(parents=True, exist_ok=True)
            args.save_schema.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(result, indent=2))
        return 2 if args.require_media_tools and not result["media_tools_ready"] else 0
    except (ValueError, KeyError, OSError) as exc:
        print(json.dumps({"error": str(exc), "predictions_submitted": 0}), file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
