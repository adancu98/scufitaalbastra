# Generation and Photoshop routing

Read this reference when a requested design needs generated assets, a named image model, or a generated concept to reconstruct as an editable Photoshop document. A simple resize, export or precise existing-document edit does not require generation. Live tool schemas and current user choices take precedence over this catalog snapshot.

## Select the route

- **Primary configured Higgsfield profile:** `gpt_image_2_6` (GPT Image 2.6 Sunburst), for concepts, detailed compositions and image assets.
- **Secondary:** `nano_banana_2_1`, when the user chooses it or a reference-based task benefits from comparing that model. Preserve the user's explicit model choice; do not replace identities or products silently.
- **Optional iteration profile:** `gpt_image_2_6_flare`, for faster exploration when suitable.
- **Native host route:** when the user chooses the available built-in image generation path, or host instructions require it, use `image_gen__imagegen` and the `imagegen` skill. It needs no new API key. Its schema does not expose a selectable model ID, quality or resolution argument: never label its output as a particular model without evidence. Do not silently switch providers after a rejection or uncertain submission.

The named Higgsfield profiles are integrations through your own connected account, not downloaded weights or fine-tuning. See [model-registry.json](model-registry.json) for provider/API identifier separation and observed status. The recorded development setup inspected catalogs; this distribution has **not** executed or visually validated a generation, and does not connect your accounts.

## Readiness, destination and cost

1. Discover the actual tool names and schemas. Higgsfield catalog reads are `mcp__codex_apps__higgsfield_models_get({"model_id":"gpt_image_2_6"})` and `mcp__codex_apps__higgsfield_models_search({"query":"nano banana","type":"image","limit":10})`. Refresh when requirements or availability differ from the registry.
2. Reuse a destination already selected for this chat. Before the first generation without one, read `mcp__codex_apps__higgsfield_get_preferences({})`; create a project only if requested or `auto_create_project` is true. Never reuse another chat's folder or change the selected workspace without authorization.
3. `mcp__codex_apps__higgsfield_estimate_image_cost({"params":{...}})` accepts the generation parameters without creating a job. With HTTPS references it imports media into the provider library, so it is not a purely read-only probe. Prefer known confirmed IDs for repeat quotes. Use a quote when required by the tool, the user's budget, or a material scope/cost change; respect authorization already given rather than asking on every call.
4. Connection and catalog access do not establish credits, free eligibility, or job success. The historical catalog/account inspection did not establish free or unlimited generation for recipients. If the tool returns `unlim_choice`, no job was submitted: present its question and repeat unchanged parameters with the user's `use_unlim` choice. Never infer that a separate free-influencer/video counter covers these images. Do not purchase credits or silently change a free request to paid.

## Concrete Higgsfield requests

All generation arguments go in `params`. Choose explicit output settings: catalog defaults are draft settings (`quality: low`, `resolution: 1k`). A final asset must use settings appropriate to its required pixel dimensions, detail and budget. `high` and `2k` below are examples, not universal print specifications; use 4k only when it contributes useful detail at the intended size. Record actual returned dimensions.

Primary raster asset, only when generation is authorized by the task:

```json
{
  "params": {
    "model": "gpt_image_2_6",
    "prompt": "Describe one asset, its role, composition, lighting and invariants here.",
    "quality": "high",
    "resolution": "2k",
    "output_format": "png",
    "count": 1
  }
}
```

Call `mcp__codex_apps__higgsfield_generate_image` with that object. For a transparent isolated asset, add `background: "transparent"` and retain PNG/WebP alpha. For a reference, add `medias: [{"role":"image","value":"<confirmed media UUID, completed job UUID, or authorized HTTPS image URL>"}]`. This is a schema example, not a runnable request until real authorized values replace the prose.

For Nano Banana use the same tool with `model: "nano_banana_2_1"`, an explicit `resolution`, and an appropriate `thinking_level` (`minimal`, `medium`, or `high`). Omit GPT-only `quality`, `background` and `output_format` controls unless its live schema adds them. For Flare change only the model to `gpt_image_2_6_flare` and preserve the selected brief/constraints.

Native SVG generation is available on the two GPT Image 2.6 profiles via `output_format: "svg"`; it accepts **no references**. Inspect the vector result. SVG paths are not a semantic PSD layer tree or a guarantee of editable typography. Do not generate SVG as a substitute for requested photography.

The Nano catalog advertises backend `mask` and `video_references` roles, but the common `generate_image.medias[].role` enum does not expose `mask`. Treat masked/video-reference routing as unresolved until a live supported request schema establishes the mapping. Do not invent a `role: "mask"` call.

## References and local files

- Label each image as edit target, identity/product reference, style reference, or composition reference in the prompt. Preserve approved products and exact copy. Do not regenerate real product geometry when the brief calls for original photography.
- Normal generation accepts `medias[].value` as an uploaded confirmed UUID, a completed generation job UUID, or an authorized HTTPS image URL. HTTPS images are uploaded into the provider library automatically; send only task-authorized assets.
- `mcp__codex_apps__higgsfield_media_upload_and_confirm({"file":"<user attachment path>","type":"image"})` is **for user-provided attachments only**. Despite its path-shaped argument, it is not a generic local-file reader. Do not call `media_confirm` after this helper.
- The documented remote-sandbox flow is `media_upload` before the producing `higgsfield_sandbox_exec` command, create the remote file and PUT it to the returned upload URL in that same command, then `media_confirm` only after HTTP 200. A path on the local Mac is not a remote sandbox path. Do not advertise arbitrary local Photoshop-preview upload as tested through this flow.
- Native host editing: inspect a local target with `view_image` first. Use `referenced_image_paths` when every target has a local path; otherwise use the smallest sufficient `num_last_images_to_include`. Never send both. Preserve transparency unless the user asks to change it. Follow the actual available tool and imagegen skill rather than inventing path/model controls.

## Completion, transfer and Photoshop assembly

`generate_image` returns job IDs and displays an updating widget. Wait with `mcp__codex_apps__higgsfield_jobs_wait({"jobs":[{"index":0,"job_id":"<returned UUID>"}],"timeout_seconds":15})`; retain `result_url` only from a completed result. Respect `poll_after_seconds`. A transport timeout can leave submission uncertain: resolve the original job before any retry.

Do not add duplicate display calls merely to refresh a normal generation widget. For independent batches use `generate_image_batch`, retain all indexed outcomes, wait in groups of at most eight, and display the terminal set once with `show_generation_by_ids` within its limit. A partial batch failure does not authorize regenerating successful jobs.

There is no dedicated connector tool that saves a generated image directly onto the Mac. For Photoshop import, download the completed authorized `result_url` using local execution into the task's authorized asset directory. Validate HTTPS and redirects, successful response, size limit, actual MIME/file signature, decoder readability and dimensions; write atomically to a new filename. Do not execute downloaded content, invent a URL, hard-code credentials or expose signed URL query strings in logs. This is asset preparation for Photoshop, not a workaround for media display restrictions. Network or filesystem access may still block transfer; report the actual limitation instead of claiming import succeeded.

For built-in generation, use an actual returned output path when provided; for project-bound assets copy the selected file into the authorized workspace before Photoshop import. Do not guess a generated filename or promise a destination argument. If only an inline image is returned, resolve an actual file through the host's supported output mechanism before claiming local availability.

After local validation:

1. Follow the existing Photoshop techniques skill and server contract. Inspect state, choose the intended document, and pin its positive `document_id`.
2. Import the asset with `mcp__photoshop__photoshop_place_image({"document_id":123,"filePath":"<verified absolute local path>","x":0,"y":0})`; use an actual document ID and image-appropriate coordinates. Inspect the resulting layer kind before claiming Smart Object editability.
3. Build final text, masks, adjustments, shapes and layout in Photoshop as the brief requires. A generated full-canvas concept can guide reconstruction; placing it alone does not satisfy a request for editable design.
4. Inspect `mcp__photoshop__photoshop_get_preview({"document_id":123,"max_dimension_px":1500,"quality":10})` and relevant layer/type state. The agent can review this image directly; no paid external critic is required. Check critical details at sufficient scale before marking them passed.
5. Save the requested PSD and exports with verified paths/dimensions. Record model/provider, chosen settings, job IDs, actual output dimensions, source asset and preview paths, visual findings and remaining limits. A complete job is not visual validation.

For remove-background intent the strict Photoshop state → removal recipe → preview → stop rule remains in force; do not route it through another generator as a workaround.

## Optional candidates are not connected integrations

Ideogram Layerize Text could provide a text-free base and positioned text data for a future Photoshop adapter. Qwen Image Layered and Ming remain optional research candidates. None is installed, connected, executed or automatically selected by this skill. Do not ask for keys, connect services, install weights, train a model, or claim a working adapter merely because a candidate appears in the registry.
