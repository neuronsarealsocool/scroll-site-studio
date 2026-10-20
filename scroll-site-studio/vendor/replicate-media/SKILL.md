---
name: replicate-media
description: Create, edit, and upscale images or generate videos using Replicate. Use when the user chooses Replicate, asks to run a Replicate model, or invokes this skill; includes model discovery, prompting, prediction tracking, and saving media.
---

# Replicate media

Turn the user's brief into finished media through Replicate. Preserve their chosen provider, model, references, and budget. This skill supplies a workflow, not an authenticated connection.

## Access

Prefer connected Replicate MCP tools; discover their actual names and schemas rather than assuming them. If none are available, use Replicate's HTTP API through available shell/network tools with an existing `REPLICATE_API_TOKEN` environment variable. Check whether the token exists without printing it. Never embed it in this skill, command arguments, logs, public files, or source control.

If authentication is missing, prepare the prompt and model/input plan, then explain that a token must be configured securely or the MCP connected. Link to https://replicate.com/account/api-tokens. Do not ask the user to paste a token into chat. Do not claim connection or successful generation without evidence.

Official integration instructions: https://mcp.replicate.com/ and https://replicate.com/docs/reference/mcp/ . Replicate's maintained complementary skills: https://replicate.com/docs/reference/skills . Do not install packages or change MCP configuration just to generate an asset unless the user requests setup.

## Choose and prepare

Infer ordinary creative choices from the request. Ask only when a missing reference, duration, deliverable, or budget would materially change the result. For video, establish text-to-video versus image-to-video, duration, aspect ratio, and whether audio is wanted.

Inspect the current model page and its API input schema before submitting. Models, availability, supported resolutions, pricing, and parameters change; do not rely on a fixed catalog. Keep an explicitly requested model. When choosing one, compare relevant candidates on output quality, reference support, duration, audio, speed, and current price. Explain the selected model and expected cost briefly; distinguish estimates from final billing. If price is unavailable, say so rather than inventing it.

Read https://replicate.com/docs/reference/http for current discovery and prediction endpoints. Fetch model metadata and version schemas with authenticated requests when available. Respect required fields, enums, input formats, and ranges; do not transfer settings between models without checking.

For images, express subject, action, framing, style, lighting, materials, palette, and any exact visible wording. For edits, specify the change and what must remain consistent. Only use negative prompts or seeds when supported.

For videos, describe a clear starting scene, subject movement, camera movement, and timing. Match the amount of action to the clip length. For image-to-video, preserve the supplied subject and composition while describing motion. Supply speech or audio instructions only when supported. Use multi-shot prompting only when the model supports it.

Use the user's reference URLs or supported file upload mechanism. A local filesystem path is not a remotely readable URL. Before sending files, read https://replicate.com/docs/topics/predictions/input-files . Avoid publishing private references merely to obtain an input URL.

## Execute and recover

A request to generate authorizes its stated count and scope. For an unspecified count, start with one output; do not launch paid comparison grids or repeated creative retries without authorization. Honor a stated spend limit. Creating this skill or setting up access does not authorize test generations.

With direct HTTP, authenticate against `https://api.replicate.com/v1` using a Bearer header built from the environment. For official models use the documented model prediction endpoint and input body; for versioned community models use the predictions endpoint with the inspected version ID. Keep request data in a structured JSON body or temporary file rather than interpolating prompts into shell commands.

Record the returned prediction ID immediately. Poll that prediction until a terminal status, using short waits that allow progress updates. Download results only after confirmed success. On failure, explain the API error and useful next step. On timeout or uncertain POST delivery, inspect existing prediction state before considering another submission; never blindly duplicate a potentially paid job. Stop on authentication, billing, or unrecoverable input errors. Cancellation requires the user's request or an already agreed time/spend limit.

## Save and deliver

Save successful outputs promptly; hosted result URLs can expire. Read https://replicate.com/docs/topics/predictions/output-files for current retention behavior. Follow the actual output schema, including arrays and nested objects. Download only identified media URLs, without sending the Replicate authorization header to arbitrary output hosts.

Use descriptive filenames in the requested output directory, or a workspace `replicate-output` folder. Preserve previous work. Record model/version, prompt, non-secret settings, prediction ID, and saved files in a small manifest; omit credentials, inline base64 inputs, and sensitive signed URLs.

Verify the downloaded files exist and inspect images or video metadata when tools permit. Distinguish file verification from visual review. Return an image preview where supported, usable media links, and local absolute file links. Report the selected model and any material limitation. Never present a temporary provider URL as permanent storage or claim a cost that was not returned or calculated from verified pricing.
