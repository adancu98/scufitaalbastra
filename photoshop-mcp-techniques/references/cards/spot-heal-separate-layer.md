# Repair small blemishes on a separate retouch layer

ID: `spot-heal-separate-layer` · Theme: `retouch`

## Problem

Dust, small blemishes, scratches, or isolated distractions interrupt otherwise usable image detail.

## Use when

- Use Spot Healing when nearby pixels offer suitable texture and color for an automatic repair.
- Use selection-based Content-Aware Fill only when a larger selected repair is actually needed.

## Avoid when

- Avoid removing intentional subject features or authentic product details.
- Avoid repeated large strokes across strong edges when automatic sampling produces smears.

## Preconditions

- Work on a copy and inspect the defect at useful magnification.
- Create an empty retouch layer above the source and enable sampling of visible source layers when supported.

## Limits

- Automatic blending is less predictable around complex edges or repeated structures.
- A successful tool return does not prove the repair is visually convincing.

## Essential Adobe-documented steps

- Select the retouch layer and Spot Healing Brush.
- Set a brush slightly larger than the defect and adapt hardness to the surrounding texture.
- Use Content-Aware sampling and Sample All Layers when writing onto the empty layer.
- Click a small spot or use a short stroke, then inspect before proceeding.
- For a selected Content-Aware Fill route, preserve the source and verify that the actual MCP operation offers separate output or explicitly work on a disposable copy.

## Adapt to the image

- Adapt brush size, hardness, stroke extent, sample scope, and selection margin to the defect.
- Separate-layer sampling must be confirmed in the MCP implementation.

## Visual verification

- Inspect at 100% for halos, smears, repeated texture, broken edges, and lost detail.
- Toggle the retouch layer and compare at fit view to ensure the repair serves the requested result.

## Current MCP mapping

- **feasibility:** Spot Healing_documented_only; selected_content_aware_repair_available_destructively_on_a_copy
- **tools:** ["photoshop_create_layer", "photoshop_duplicate_layer", "photoshop_select_rectangle", "photoshop_content_aware_fill", "photoshop_recipe_remove_distraction", "photoshop_get_state", "photoshop_get_preview"]
- **parameters:** {"photoshop_create_layer": {"name": "explicit retouch layer name", "document_id": "positive target id"}, "photoshop_duplicate_layer": {"newName": "disposable pixel copy name", "document_id": "positive target id"}, "photoshop_select_rectangle": {"left": "pixel coordinate", "top": "pixel coordinate", "right": "pixel coordinate", "bottom": "pixel coordinate", "mode": ["replace", "add", "subtract", "intersect"], "document_id": "positive target id"}, "photoshop_content_aware_fill": {"document_id": "positive target id; current pixel selection required"}, "photoshop_recipe_remove_distraction": {"feather_px": "0–20; adapt to selection edge", "use_generative": false, "document_id": "positive target id"}}
- **limits:** ["No dedicated Spot Healing or Healing Brush tool is advertised. Creating an empty layer is possible, but no native tool exposes brush size/hardness/strokes or Sample All Layers. Empty-layer creation alone is not a realizable separate-layer healing workflow.", "Content-Aware Fill uses a fill action on the active pixel layer and clears the selection. Its schema has no Output To New Layer, sampling-region, or Sample All Layers control.", "The non-generative remove-distraction recipe also modifies selected pixels and clears the selection; it is not brush healing and does not create a new repair layer. Preserve originals by using a disposable source copy for this alternative.", "Remove Distraction defaults to generative when version-derived capability is true; explicitly set use_generative:false when only classical content-aware repair is intended.", "A spike script contains guessed removeTool/spotHealing Brush action probes and explicitly requests visual confirmation. Probe source code is not proof of supported brush execution or visual validation."]
- **server_contract_notes:** ["Read photoshop_get_state; capture and pass a positive document_id; select the intended layer by exact unique name when needed; inspect photoshop_get_preview after the meaningful change. All current live schemas reject additional properties.", "Selected distraction removal may use the matching recipe when suitable. Do not call a content-aware fill a validated Spot Healing workflow. Do not apply background-removal workarounds; that separate intent retains its strict recipe-only contract."]
- **implementation_evidence:** ["validation/environment-20261109/discovery.json (live 128 tools, server 1.7.37,2026-11-09)", "photoshop-mcp/src/tools/selection-tools.ts:357–377 (selection fill tool and parameters)", "photoshop-mcp/src/api/extendscript.ts:3007–3032 (current-layer fill, deselect, no output/sampling controls)", "photoshop-mcp/src/tools/recipes/remove-distraction.ts:51–157 (generative default and non-generative pixel path)", "photoshop-mcp/scripts/spike-photoshop-actions.ts:387–425 (experimental action probes, not validated brush support)"]

## Historical execution report, not an installation test

- **status:** not_run
- **checked_on:** 2026-11-09
- **reason:** Not executed in the initial development batch; no runtime validation is bundled.

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/remove-objects-from-your-photos
- **title:** Remove unwanted objects from your photos
- **checked_on:** 2026-11-09
- **content_read:** transcript
- **coverage:** Read visible Photoshop-on-the-web retouch transcript. Desktop Help confirms separate empty-layer Spot Healing and Content-Aware sampling; web UI is not taken as desktop MCP support.
- **secondary_urls:** ["https://helpx.adobe.com/photoshop/desktop/repair-retouch/clean-restore-images/remove-small-spots-with-the-spot-healing-brush.html"]
- **source_ids:** ["cr-learn-web-retouch", "cr-help-spot-healing"]

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
