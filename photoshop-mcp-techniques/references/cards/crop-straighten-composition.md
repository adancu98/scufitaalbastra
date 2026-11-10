# Crop and straighten while preserving intended framing

ID: `crop-straighten-composition` · Theme: `composition`

## Problem

The image has excess edges, a tilted horizon, or the wrong framing for the requested format.

## Use when

- Use when changing composition or fitting a requested aspect ratio.
- For a simple pixel resize with acceptable framing, resize without adding a crop.

## Avoid when

- Do not cut important subject features solely to fill a template.
- Do not invent missing background through content-aware or generative expansion unless justified or requested.

## Preconditions

- Know the requested aspect ratio and the content that must remain visible.
- Distinguish aspect ratio from pixel dimensions and resolution.

## Limits

- Straightening can expose empty corners or require cropping.
- Hidden cropped content is recoverable only if the actual operation preserves it; MCP parity must be checked.

## Essential Adobe-documented steps

- Select the Crop tool and set the boundary by dragging edges or entering an aspect ratio.
- Straighten by rotating outside the crop boundary and comparing a real horizon or architectural line with the grid.
- Position the image within the boundary; composition guides are optional aids, not a fixed rule.
- Leave Delete Cropped Pixels disabled when reversible framing is required and supported.
- Commit only after checking all important edges, then clear a temporary crop ratio so it does not affect later work.

## Adapt to the image

- Adapt crop rectangle, target ratio, rotation angle, focal placement, and preserved margins to the image.
- Choose output pixel dimensions separately rather than treating a ratio as a size.

## Visual verification

- Inspect the entire frame for clipped wheels, limbs, text, or other required details.
- Check that genuinely horizontal or vertical references appear correct and that no blank corners remain.
- Verify resulting dimensions and whether hidden pixels can still be recovered.

## Current MCP mapping

- **feasibility:** native_destructive_rectangular_crop; no_native_nondestructive_or_document_straighten_control
- **tools:** ["photoshop_crop_document", "photoshop_resize_image", "photoshop_rotate_layer", "photoshop_get_state", "photoshop_get_preview"]
- **parameters:** {"photoshop_crop_document": {"left": "nonnegativepx", "top": "nonnegativepx", "right": "px>left", "bottom": "px>top", "document_id": "positive target id"}, "photoshop_resize_image": {"width": "targetpx>=1", "height": "targetpx>=1", "document_id": "positive target id"}, "photoshop_rotate_layer": {"degrees": "clockwisepositive; targetlayeronly", "document_id": "positive target id"}, "missing_native_controls": ["Delete Cropped Pixels:false", "cropangle", "straightenreference-line", "cropaspect-ratioasaseparateparameter"]}
- **limits:** ["The crop tool passes a rectangle to doc.crop(bounds), deletes pixels outside it, and affects all layers. It has no nondestructive-crop flag, ratio control, or straighten angle.", "Compute a rectangle from the intended aspect ratio and visible subject; do not send ratio, rotation, or preserve-pixels fields absent from the live schema.", "Layer rotation does not rotate the document canvas or straighten an entire multilayer document. A layer-rotate-plus-crop sequence is not automatically equivalent to Adobe CropTool straightening.", "ResizeImage resamples the entire document to exactly the supplied width and height; it is a separate operation. Preserve aspect ratio by calculating both values rather than assuming a constrain-proportions option.", "Test destructive crop on a disposable document copy. No current verified script for nondestructive CropTool straightening is supplied by this mapping."]
- **server_contract_notes:** ["Read photoshop_get_state; capture and pass a positive document_id; select the intended layer by exact unique name when needed; inspect photoshop_get_preview after the meaningful change. All current live schemas reject additional properties.", "A resize-only request should use resize_image without an added crop or style change. Use crop_document only when its destructive rectangle matches the requested result and the source is preserved."]
- **implementation_evidence:** ["validation/environment-20261109/discovery.json (live 128 tools, server 1.7.37,2026-11-09)", "photoshop-mcp/src/tools/image-tools.ts:9–75 (resize/crop schemas and destructive side effects)", "photoshop-mcp/src/api/extendscript.ts:2478–2492 (doc.crop(bounds))", "photoshop-mcp/src/api/extendscript.ts:1850–1872 (layer.rotate, not canvas)", "photoshop-mcp/src/tools/layer-transform-tools.ts:82–112 (rotate_layer degrees only)"]

## Historical execution report, not an installation test

- **status:** historical_report_not_reproduced_here
- **reported_status:** validated_crop_component_only
- **reported_checked_on:** 2026-11-09
- **reported_environment:** {"photoshop": "27.11.0", "mcp": "1.7.37", "commit": "ba36d8f2a28ecc56686568f3c0191e388336d498"}
- **observations:** ["Bounds350,40–1550,800 yielded1200×760; all product wheels remain inside the crop."]
- **limits:** ["This atomic crop deletes outside pixels. Straightening and non-destructive crop were not tested or exposed by this tool.", "Historical development summary only. Raw logs, local paths and fixture files are not distributed; installation does not run or certify this operation."]

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/crop-straighten-to-improve-composition
- **title:** How to crop a photo
- **checked_on:** 2026-11-09
- **content_read:** transcript
- **coverage:** Read the four-step desktop tutorial transcript and written recap: boundary, aspect ratio, positioning, non-destructive option, commit, and clearing settings.
- **secondary_urls:** []
- **source_ids:** ["cr-learn-crop"]

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
