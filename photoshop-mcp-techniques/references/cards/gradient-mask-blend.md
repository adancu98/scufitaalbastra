# Create a gradual transition on a layer mask

ID: `gradient-mask-blend` · Theme: `masks`

## Problem

Blend overlapping image regions with a controllable transition instead of a hard seam.

## Use when

- A soft transition contributes to the requested composite or fade.
- The image overlap contains compatible content that can tolerate partial transparency.

## Avoid when

- Do not fade across an important object merely to conceal poor placement.
- Do not use gradient blending as a substitute for a precise object boundary.
- Do not assume every multi-image layout needs a blended seam.

## Preconditions

- Place the participating images on separate layers with sufficient overlap.
- Identify which image must remain visible at each end and select the correct mask.

## Limits

- The gradient changes visibility, not the photographs' perspective or lighting.
- Both images remain partly visible in the gray transition, so unwanted double contours are possible.
- The gradient recipe's supported geometry and mask behavior require separate MCP verification.

## Essential Adobe-documented steps

- Create an editable mask on the layer that will fade.
- Apply a white-to-black or black-to-white gradient on that mask with the intended visibility direction.
- Adjust the line position, direction, and length until the transition supports the composition.
- Where the verified tools permit, restore important details locally with white or conceal conflicting overlap with black.

## Adapt to the image

- Adapt gradient endpoints to image overlap and the location of critical features.
- Shorten or lengthen the transition from the visible seam quality.
- Choose the gradient direction from which source should dominate each region.

## Visual verification

- Inspect the grayscale mask and the final overlap.
- Look for doubled objects, ghosted edges, obvious tonal bands, or transparency through a subject.
- Judge the transition at intended viewing size as well as close view.

## Current MCP mapping

- **feasibility:** native_linear_gradient_with_preservation_and_targeting_limits
- **tools:** ["photoshop_recipe_gradient_fade", "photoshop_apply_gradient_mask", "photoshop_get_layers", "photoshop_get_preview"]
- **parameters:** {"document_id": "Pin the intended document and active fading layer.", "direction": "top_to_bottom, bottom_to_top, left_to_right, or right_to_left; actual endpoints follow this axis. Default bottom_to_top.", "start_pct_end_pct": "Integers0–100 after handler clamping/rounding, measured along the document width/height, not the selected layer's bounds. Avoid identical endpoints.", "angle_deg": "Advertised but not applied to the gradient geometry in the inspected implementation. It is calculated and returned as metadata only; do not claim arbitrary-angle support."}
- **limits:** ["Prefer the recipe for the requested multi-step fade outcome; it creates a mask if absent and wraps the change in one history state. The atomic route can auto-create a mask through a two-step retry path.", "The gradient helper uses Normal blending with fully opaque stops. It writes a new grayscale gradient over the affected mask area, rather than multiplying it with an existing subject-isolation mask. Existing mask detail is therefore not preserved by design; active selection/channel behavior needs runtime inspection.", "Neither route deselects before filling. An active selection can constrain the gradient, so inspect and intentionally manage it before executing a permitted fade.", "The mask-channel selection helper uses channel ordinal target instead of explicitly identifying the mask channel. From source alone, mask-only targeting cannot be guaranteed for every prior channel state; test a pre-existing mask with RGB active and confirm image pixels remain untouched.", "No radial gradient or arbitrary endpoint-pair parameters are exposed by these two tools. Do not substitute a Gradient Fill layer for the Adobe mask technique."]
- **server_contract_notes:** ["The recipe description requires an isolated subject for a subject fade and suggests removal first; do not add background removal to a simple unrelated fade without the user's intent. When explicit background removal is the request, its strict sequence stops after preview rather than continuing into this recipe.", "If preserving the existing subject mask is necessary, do not run this normal-opacity gradient over it as a safe default. Consider a separate group mask only through a permitted and separately verified missing-operation script, or state the limit.", "Record actual gradient direction and observed visibility. The returned angle value alone is not evidence that the requested angle was rendered."]
- **implementation_evidence:** ["validation/environment-20261109/discovery.json: gradient recipe/atomic schemas and four direction enums.", "photoshop-mcp/src/tools/recipes/gradient-fade.ts:76-132: angle calculated, axis endpoints used, existing mask reused, no deselect, history state.", "photoshop-mcp/src/tools/recipes/_shared.ts:341-360: axis-only endpoint mapping.", "photoshop-mcp/src/api/extendscript.ts:918-925,948-990: current-channel selector, Normal gradient blend, opaque stops, linear fill.", "photoshop-mcp/src/api/extendscript.ts:3075-3130: atomic gradient endpoints, angle reported only, component-channel restore.", "photoshop-mcp/src/tools/mask-tools.ts:205-268: atomic retry creating a missing mask."]
- **runtime_gates:** ["Do not use the recipe/atomic gradient on an existing mask with RGB active.", "When replacement of the mask is intended, first run the tested explicit-mask-channel snippet with pinned document_id, then use the recipe.", "For preserving an existing isolation mask, a separate verified combination workflow is still required."]

## Historical execution report, not an installation test

- **status:** historical_report_not_reproduced_here
- **reported_status:** conditional_validation_with_confirmed_unsafe_case
- **reported_checked_on:** 2026-11-09
- **reported_environment:** {"photoshop": "27.11.0", "mcp": "1.7.37", "commit": "ba36d8f2a28ecc56686568f3c0191e388336d498"}
- **observations:** ["Fresh reveal-all mask: left_to_right20–80 hides left and reveals right; actual mask exists.", "Existing mask+RGB: recipe painted RGB to black/white while preserving the rectangular mask, confirmed visually in case11.", "Explicit mask-channel selection before the recipe produced the intended color fade in case12."]
- **limits:** ["Only left_to_right was tested; arbitrary angles are not implemented.", "Gradient replaces existing mask values; it does not intersect with subject isolation.", "Historical development summary only. Raw logs, local paths and fixture files are not distributed; installation does not run or certify this operation."]
- **runtime_gates:** ["Do not use the recipe/atomic gradient on an existing mask with RGB active.", "When replacement of the mask is intended, first run the tested explicit-mask-channel snippet with pinned document_id, then use the recipe.", "For preserving an existing isolation mask, a separate verified combination workflow is still required."]
- **verified_script:** references/verified-scripts/select-layer-mask.jsx

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/layer-mask
- **title:** How to gradually blend images with a layer mask
- **checked_on:** 2026-11-09
- **content_read:** transcript
- **coverage:** Read accessible transcript and written summary through gradient placement, mask inspection, and white-brush refinement. Video not played.
- **sections_read:** ["Understanding the layer setup and blending goal", "Adding a layer mask to the top layer", "Applying a black-to-white gradient on the mask", "Viewing and understanding the gradient mask effect", "Refining the gradient mask by painting with the Brush tool"]
- **supplemental_sources:** [{"url": "https://www.adobe.com/learn/photoshop/web/blend-two-images-gradient", "title": "Combine images with a smooth transition", "content_read": "transcript", "coverage": "Read accessible introduction and available explanatory sections; used as supplementary confirmation, not a separate fully analyzed video."}]

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
