# Media and providers

Read the selected vendor workflow and current official provider docs/schema/pricing.
This package contains no accounts, API keys or credits. **Default to Replicate for
every new media-generation task**, using an existing REPLICATE_API_TOKEN or connected
tool. Use another provider only when the user explicitly chooses it. Bundled KIE
helpers are not an automatic fallback. If Replicate is unavailable, prepare prompts
and local placeholders and report the missing access; do not switch providers.
Honour the chosen model, prompt reuse/adaptation mode and budget. A verbatim prompt
must remain unchanged except for a required, disclosed input-format adaptation.

## Mandatory chat review before web publication

1. Generate or select media locally within the authorized scope. Save originals and
   distinct versions. Provider reference uploads necessary for an authorized generation
   are allowed as part of that operation; do not confuse them with site publication.
2. Show the actual images/videos here in chat using native media previews or local
   file previews. If direct playback is unavailable, provide a usable local review
   page/file and explain that limit. A prompt, contact sheet, plan or thumbnail does
   not replace approval of the actual final video when it can differ materially.
3. Ask for explicit approval of the identified assets/versions for the website, then
   wait. Continue layout/code work using placeholders without uploading pending media.
4. Record the user's approval with filenames/versions and approved use. Only those
   approved assets may enter public/staging hosting, CDNs, public repositories or
   deployment artifacts. Do not upload pending media merely to produce a review link.
5. Keep approval for unchanged media. Re-review meaningful visual changes, replacement
   generations, crops or reframing. Nonvisual encoding with the same composition
   does not by itself invalidate approval; still verify the delivered result.

This applies to supplied/newly selected assets as well as generated images, videos
and other media. An upload for reference or an approved generation budget does not
by itself authorize publishing that asset. Never infer approval from silence or elapsed
time. Existing approved live assets may remain unchanged without another gate.

Metadata GET does not prove a balance. Before POST record an approved count, estimate
and retry allowance. Save prediction IDs immediately; an uncertain timeout is not
permission to submit again. Inspect existing state/listing before considering a retry;
stop when a possibly paid submission cannot be reconciled. There is no hidden paid
API POST in the main scripts. Keep successful outputs and preserve prior work.

Keep credentials, data URIs and expiring signed URLs out of distributable manifests.
Do not forward API authentication to arbitrary media CDN hosts. Download successful
outputs promptly before their provider URLs expire.

media.py resolves SCROLLSITE_FFMPEG/SCROLLSITE_FFPROBE, PATH, then known package-manager
locations. H.264/yuv420p/faststart, no audio, GOP 8 desktop / 4 mobile are starting
settings. Preserve dimensions. --mobile tunes encoding; it **does not crop or generate**
portrait footage. frames saves first and true final decoded images. Re-encoding does
not turn a lower-resolution input into native high resolution. Visually inspect files.

Separate 9:16 generation costs extra; agree whether phones receive it, a responsive
landscape version, an approved crop or a still. Label the treatment accurately.
