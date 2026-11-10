# Clone controlled source detail onto an editable retouch layer

ID: `clone-stamp-controlled-repair` · Theme: `retouch`

## Problem

A repair needs predictable source texture or an exact detail copy instead of automatic healing.

## Use when

- Use when an appropriate sample exists and texture direction or structural continuity matters.
- Use when healing blends unwanted colors into the target.

## Avoid when

- Avoid cloning distinctive details repeatedly into an obvious pattern.
- Do not stamp source detail with different lighting or perspective merely to cover the defect.

## Preconditions

- Create a blank pixel retouch layer above the source.
- Choose Current & Below or All Layers so the blank layer can obtain image samples.
- Choose a source region matching the target's texture and illumination.

## Limits

- Clone Stamp copies source detail rather than automatically matching target color and brightness.
- It cannot paint onto an adjustment layer.
- Source and target coordinates require image-specific decisions.

## Essential Adobe-documented steps

- Select Clone Stamp and set blend mode, brush properties, opacity, and flow.
- Choose Aligned for continuous source offset, or unaligned sampling when each stroke should restart at the initial point.
- Set the source with Alt/Option-click and paint short controlled strokes on the retouch layer.
- Resample when nearing unsuitable source content or when repeated features become visible.
- Keep the original image and retouch layer separately editable.

## Adapt to the image

- Adapt source coordinates, brush size and hardness, mode, opacity, flow, alignment, and sample-layer scope.
- Keep explicit source and target regions in any reproducible MCP test record.

## Visual verification

- Inspect edge continuity and texture at 100%.
- Compare at fit view for repeated patterns, tonal seams, or an altered subject silhouette.
- Toggle the retouch layer to ensure the intended defect alone was changed.

## Current MCP mapping

- **feasibility:** documented_only_no_dedicated_tool_or_verified_brush_script
- **tools:** ["photoshop_create_layer", "photoshop_get_state", "photoshop_get_preview"]
- **parameters:** {"photoshop_create_layer": {"name": "retouch layer name; preparation only", "document_id": "positive target id"}, "missing_native_controls": ["clone source point", "target brush stroke", "Aligned", "sampling layer scope", "brush hardness/size/flow for cloning"]}
- **limits:** ["No Clone Stamp tool is present in the current 128 tools, and no verified Clone Stamp implementation was found in src/tools or src/api/extendscript.ts.", "Creating an empty pixel layer is preparation only; it does not supply a sample source or paint cloned pixels.", "Content-Aware Fill, Healing, and generative removal are different methods. Do not silently use them when exact source-detail cloning is required.", "The generic execute_script escape hatch does not prove brush-event descriptors or sample-all-layers cloning. No invented cloneStamp()/paintStroke() function is authorized by this mapping.", "A recorded action might become usable through photoshop_play_action only if a real matching action/set is supplied and its image-specific sampling behavior is verified separately; none was inspected or executed here."]
- **server_contract_notes:** ["Read photoshop_get_state; capture and pass a positive document_id; select the intended layer by exact unique name when needed; inspect photoshop_get_preview after the meaningful change. All current live schemas reject additional properties.", "Keep this card documented-only until an exact native or verified scripted/manual path is available. Do not claim a retouching result merely because a blank layer was added."]
- **implementation_evidence:** ["validation/environment-20261109/discovery.json (live 128 tools, server 1.7.37,2026-11-09)", "photoshop-mcp/src/tools/layer-tools.ts:8–28 (blank layer creation only)", "photoshop-mcp/src/tools/action-tools.ts:12–35 (action requires an actual existing action/set)", "photoshop-mcp/src/tools/action-tools.ts:38–74 (generic JSX is not a specific brush implementation)", "Staticsearchofsrc/toolsandapi/extendscript.tsfoundnoClone Stampimplementation"]

## Historical execution report, not an installation test

- **status:** not_run
- **checked_on:** 2026-11-09
- **reason:** Not executed in the initial development batch; no runtime validation is bundled.

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/remove-objects-from-your-photos
- **title:** Remove unwanted objects from your photos
- **checked_on:** 2026-11-09
- **content_read:** transcript
- **coverage:** Learn transcript explains exact copying, separate retouch layer, and resampling repeated texture. Desktop Help confirms modes, sampling scopes, alignment, and the adjustment-layer restriction.
- **secondary_urls:** ["https://helpx.adobe.com/photoshop/desktop/repair-retouch/heal-clone/retouch-images-with-the-clone-stamp-tool.html"]
- **source_ids:** ["cr-learn-web-retouch", "cr-help-clone-stamp"]

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
