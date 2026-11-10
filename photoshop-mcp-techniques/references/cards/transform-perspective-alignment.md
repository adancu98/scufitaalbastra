# Align a layer with proportional transforms; use perspective correction only when needed

ID: `transform-perspective-alignment` · Theme: `composition`

## Problem

A placed layer has the wrong scale, rotation, position, or perspective relative to the target scene.

## Use when

- Use the smallest transform that resolves the mismatch.
- Use perspective correction for tilted architecture or a justified composite with clearly identifiable planes.

## Avoid when

- Do not stretch products non-proportionally to fill space.
- Do not use viewpoint-changing Perspective Warp as a routine alignment shortcut.

## Preconditions

- Identify the target plane, horizon, and alignment references.
- Prefer preserved source data such as a Smart Object for repeated transformations.
- Check the actual Photoshop feature and MCP operation separately.

## Limits

- Free Transform perspective and Perspective Warp's connected planes are different operations.
- Repeated committed transforms of ordinary pixels can soften them.

## Essential Adobe-documented steps

- Select the intended layer and enter Free Transform.
- Keep width and height linked for proportional scaling; set position and rotation numerically when useful.
- Use distortion or perspective only if the requested scene requires it, then commit the combined transformation once.
- If genuine Perspective Warp is available and appropriate, fit layout grids to the image planes, connect adjoining edges, switch to Warp, and refine pins against the scene's lines.
- Compare the result with the preserved original.

## Adapt to the image

- Adapt X/Y position, equal scale values, angle, pivot/reference point, and any justified corner or plane coordinates.
- Plane coordinates cannot be reused blindly across images.

## Visual verification

- Check subject proportions, straight edges, contact with the scene, and complete frame coverage.
- Inspect at 100% for resampling damage and at fit view for credible perspective.
- Do not call a transform validated from a tool response alone.

## Current MCP mapping

- **feasibility:** native_proportional_scale_move_rotate; perspective_and_PerspectiveWarp_not_exposed_or_verified
- **tools:** ["photoshop_select_layer_by_name", "photoshop_convert_to_smart_object", "photoshop_scale_layer", "photoshop_fit_layer_to_document", "photoshop_move_layer", "photoshop_rotate_layer", "photoshop_get_state", "photoshop_get_layers", "photoshop_get_preview"]
- **parameters:** {"photoshop_select_layer_by_name": {"name": "unique exact name", "document_id": "positive target id"}, "photoshop_convert_to_smart_object": {"layer_name": "optional exact name", "document_id": "positive target id"}, "photoshop_scale_layer": {"scalePercent": ">=1;uniform width and height percentage", "centerAnchor": "true=center,false=top-left", "document_id": "positive target id"}, "photoshop_fit_layer_to_document": {"fillDocument": "false=fitinside,true=cover and possibly crop", "document_id": "positive target id"}, "photoshop_move_layer": {"deltaX": "relative pixel offset", "deltaY": "relative pixel offset", "document_id": "positive target id"}, "photoshop_rotate_layer": {"degrees": "relative clockwise angle", "document_id": "positive target id"}, "missing_native_controls": ["independent corner coordinates", "skew/distort/perspective", "Perspective Warp layout planes/pins", "arbitrary pivot", "absoluteX/Yplacement"]}
- **limits:** ["Native scale calls layer.resize(percent,percent), preserving proportions. centerAnchor offers only center/top-left. Native move is relative translation; native rotate is relative rotation around center.", "Transform tools reject Background layers and scaling rejects empty bounding rectangles. SmartObject conversion also requires an unlocked/non-Background target.", "Fitting to fillDocument:true covers the canvas and may hide important edges; fitinside may leave margins.", "The recipe batch_mockup_replace preserves pre-existing SmartObject perspective/warp; that does not mean MCP can author a new perspective transform or PerspectiveWarp plane network.", "No current dedicated perspective/distort/warp tool or verified script was found. A generic escape hatch is not evidence of these operations.", "Do not rasterize a SmartObject to satisfy a transform or assume native scale/rotate equals PerspectiveWarp."]
- **server_contract_notes:** ["Read photoshop_get_state; capture and pass a positive document_id; select the intended layer by exact unique name when needed; inspect photoshop_get_preview after the meaningful change. All current live schemas reject additional properties.", "Use these atomics for single precise transforms. Scale/rotate/move accumulate, so reread state before repeating them after an error. Preserve source via SmartObject when compatible."]
- **implementation_evidence:** ["validation/environment-20261109/discovery.json (live 128 tools, server 1.7.37,2026-11-09)", "photoshop-mcp/src/tools/layer-transform-tools.ts:8–114 (actual schemas)", "photoshop-mcp/src/api/extendscript.ts:1792–1872 (uniform resize, relative offset, center rotation)", "photoshop-mcp/src/tools/smart-object-tools.ts:15–36 (conversion preconditions)", "photoshop-mcp/src/tools/recipes/batch-mockup-replace.ts:30–38 (preserves existing warp, does not create one)"]

## Historical execution report, not an installation test

- **status:** historical_report_not_reproduced_here
- **reported_status:** validated_uniform_scale_component_only
- **reported_checked_on:** 2026-11-09
- **reported_environment:** {"photoshop": "27.11.0", "mcp": "1.7.37", "commit": "ba36d8f2a28ecc56686568f3c0191e388336d498"}
- **observations:** ["Smart Object bounds changed from1200×800 to960×640, centered at120,80; proportions remained intact."]
- **limits:** ["Rotation, straightening, corner transforms and Perspective Warp were not tested; native uniform scale is not perspective support.", "Historical development summary only. Raw logs, local paths and fixture files are not distributed; installation does not run or certify this operation."]

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/photoshop-perspective-warp
- **title:** Adjust perspective in a photo
- **checked_on:** 2026-11-09
- **content_read:** transcript
- **coverage:** Read visible legacy Perspective Warp transcript. Current desktop Free Transform Help supplies proportional scaling, positioning, combined transforms, and Smart Object preservation.
- **secondary_urls:** ["https://helpx.adobe.com/photoshop/desktop/crop-resize-transform/resize-adjust-resolution/transform-images-shapes-and-paths.html", "https://helpx.adobe.com/photoshop/desktop/crop-resize-transform/transform-manipulate-reshape/adjust-scale-rotation-and-perspective.html"]
- **source_ids:** ["cr-learn-perspective", "cr-help-free-transform", "cr-help-transform-types"]

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
