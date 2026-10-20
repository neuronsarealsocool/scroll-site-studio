# Replicate pipeline

Use alongside `$replicate-media`; that skill owns generation and prediction
recovery. This guide supplies the scroll-world frame mapping and local processing.
All examples are templates to fill from the agreed project, not instructions to
start paid jobs during setup.

## Read-only preflight

```powershell
python '<scroll-world-root>/scripts/replicate_preflight.py' --model bytedance/seedance-2.0 --quality 1080p --duration 8
python '<scroll-world-root>/scripts/replicate_preflight.py' --model kwaivgi/kling-v3-video --quality 1080p --duration 8
```

The helper checks live model metadata using GET only, resolves schema enums,
and reports frame field names plus dependencies. `--save-schema model-schema.json`
saves a local public schema snapshot (no token, user data, or prediction output).
`--schema-file model-schema.json` validates offline instead. Use `--require-media-tools`
when checking readiness to actually generate a flight. A successful schema check
does not qualify frame fidelity and does not verify the user's billing balance.

Official sources to recheck when executing:

- https://replicate.com/docs/reference/http
- https://replicate.com/docs/topics/predictions/input-files
- https://replicate.com/docs/topics/predictions/output-files
- https://replicate.com/bytedance/seedance-2.0/api
- https://replicate.com/kwaivgi/kling-v3-video/api

## Build inputs from current schemas

On 2026-10-16 the authenticated metadata GETs confirmed these input mappings:

```json
{
  "prompt": "The inspected scene and continuous forward camera move",
  "image": "https://host/actual-previous-final-frame.png",
  "last_frame_image": "https://host/approved-destination.png",
  "duration": 8,
  "resolution": "1080p",
  "aspect_ratio": "16:9",
  "generate_audio": false
}
```

The above is Seedance 2.0. For Kling v3 use:

```json
{
  "prompt": "The inspected scene and continuous forward camera move",
  "start_image": "https://host/actual-previous-final-frame.png",
  "end_image": "https://host/approved-destination.png",
  "duration": 8,
  "mode": "pro",
  "aspect_ratio": "16:9",
  "generate_audio": false
}
```

Kling maps 720p to `mode: standard`, 1080p to `pro`, and 4K to `4k` in the
inspected schema. Seedance uses its resolution field. Pass actual supported
values from the live schema; do not copy Higgsfield `std`, `--sound`, or CLI flags.
Kling derives the output aspect from the start image, so prepare the input canvas
at the agreed aspect ratio. Seedance first/last frames cannot be combined with
`reference_images`; do not treat reference arrays as frame pinning.

Never submit a local Windows path as a URI. Use the connected Replicate tools'
supported file upload, the documented client/file API, or a small data URI when
supported. The docs recommend data URIs below 1 MB; the API schema recommends
hosted uploads above 256 KB, so prefer Replicate's file API for cabin PNGs.
Do not publish private images to an unrelated public host merely to get a URL.
Local file transfers are part of an authorized generation, never preflight.
Do not persist base64 input bodies or signed upload URLs in run manifests.

## Submit and resume through replicate-media

After generation scope/budget are authorized, construct the input object as data.
Use an authenticated `GET /v1/models/{owner}/{name}` to inspect
`latest_version.openapi_schema` and `is_official` first. For an official model,
POST `{"input": ...}` to `/v1/models/{owner}/{name}/predictions`. For a versioned
community model, POST `{"version": "<verified-version-id>", "input": ...}` to
`/v1/predictions`. Use the token only in the Authorization header, never command
arguments. Submit once, asynchronously; immediately save the prediction ID.

Poll `GET /v1/predictions/{id}` in short, interruptible intervals. Save status and
known IDs before yielding. A timeout or uncertain POST delivery does not authorize
resubmission: inspect existing prediction state/history first. On `succeeded`,
follow the real output schema and download identified result files promptly;
output URLs can expire. Download output hosts without the Replicate auth header.
Stop on authentication/billing failures. No automatic paid re-rolls or model swaps
beyond the agreed count and budget. A failed clip does not invalidate saved clips.

Use a local manifest with model/version, prompt, settings, source image paths,
leg order, prediction IDs, status, raw/encoded output paths, boundary frame paths,
and known cost. Never include credentials, inline base64, or sensitive signed URLs.
Retain API outputs privately only if needed for recovery; sanitize before sharing.

## Frame extraction

Keep raw clips under a project-owned `work/scroll-world` directory and finished
assets in the site's asset directory. Never assume Unix `/tmp` or Bash on Windows.
Use absolute tool paths if ffmpeg/ffprobe are not on PATH.

First frame:

```powershell
ffmpeg -v error -i leg1.mp4 -frames:v 1 first.png
```

To get the **actual final decoded frame**, decode the clip and overwrite one
temporary image as every frame passes. Use a distinct target for each clip:

```powershell
ffmpeg -v error -i leg1.mp4 -map 0:v:0 -fps_mode passthrough -update 1 -y last.png
```

This is more exact than `-sseof -0.15 -frames:v 1`, which selects a frame near
the end rather than necessarily the final one. For short generation clips the
full decode cost is small. Inspect last.png before chaining. After compositing,
trimming, or encoding, regenerate boundary frames from the delivered version;
keep dimensions and color handling consistent across all clips.

Architecture A: leg n+1 starts from leg n's final frame and targets its own
approved destination still. Render sequentially. Architecture B: generate dives,
then connectors from dive n's final frame to dive n+1's first frame.

## Encode for browser scrubbing

Inspect native dimensions, duration, and frame rate first:

```powershell
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate,codec_name -show_entries format=duration -of json raw.mp4
ffmpeg -v error -i raw.mp4 -an -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p -g 8 -keyint_min 8 -sc_threshold 0 -movflags +faststart delivered.mp4
```

Do not overwrite raw clips or add upscaling. Sharpening is optional, not required.
Use GOP 4/CRF about 23 for lighter phone encodes when useful. A downscaled landscape
file is still landscape: keep the distinction from a separately generated portrait
chain. For native portrait film, a phone encode may use `-vf scale=720:-2` when
the source width is at least 720; preserve smaller sources at their native size.
Save each delivered clip's first frame as its engine poster.

## Engine wiring

Read the header of `scrub-engine.js` for current configuration. For A:

```javascript
mountScrollWorld(document.getElementById('world'), {
  brand: { name: 'Project name' },
  atmosphere: false,
  diveScroll: 1.3,
  sections: [
    { id: 'arrival', label: 'Arrival', still: 'assets/arrival-first.png',
      clip: 'assets/vid/arrival.mp4', title: 'Approved existing headline' },
    { id: 'living', label: 'Great room', still: 'assets/living-first.png',
      clip: 'assets/vid/living.mp4', title: 'Approved room headline' }
  ],
  connectors: []
});
```

For B, connectors has N-1 entries in route order. Only provide mobile media keys
when those files actually exist. The supplied full-page template is a starter;
its example asset URLs and brand text must be replaced before delivery.

The upstream engine loads MP4s as blobs to make them seekable even without HTTP
range support. Preserve this, lazy prefetch, touch priming, seek coalescing,
`playsinline`, muted playback, and the poster-until-painted behavior when porting.
