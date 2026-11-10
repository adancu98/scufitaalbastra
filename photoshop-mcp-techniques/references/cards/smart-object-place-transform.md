# Place and transform an asset as an editable Smart Object

ID: `smart-object-place-transform` · Theme: `smart-objects`

## Problem

A layout needs a photograph positioned and resized while retaining its source for later changes.

## Use when

- An imported asset will be scaled, rotated, replaced or revised.
- A reusable composition must keep its photographs independent of surrounding layers.

## Avoid when

- Do not convert unrelated layers merely because the feature is available.
- Do not rasterize the placed source to make a simple transform easier.

## Preconditions

- Inspect the intended destination document and source dimensions.
- Use an available source file; an embedded object packages its source in the document.

## Limits

- A Smart Object preserves source content; it does not create missing photographic detail.
- The Learn transcript uses a legacy Shift-key instruction for proportional scaling. Use explicit linked proportions in the current UI or equivalent verified MCP parameters rather than copying that modifier blindly.

## Essential Adobe-documented steps

- Use Place Embedded to import the asset, or convert the selected existing content to a Smart Object when appropriate.
- Scale proportionally, position and optionally rotate, then commit the transform.
- Keep the object separate and named. Edit its contents through its thumbnail when an actual source revision is needed.
- Save the layered working file; export a separate presentation copy if required.

## Adapt to the image

- Source and destination pixel dimensions; proportional scale; placement anchor; rotation; important subject bounds; intended output size.

## Visual verification

- Inspect the whole composition and the important subject at useful detail scale: no stretching, accidental crop or soft detail hidden by a small preview.
- Verify a Smart Object entry remains in the layer structure. Repositionability alone is not proof that source pixels were retained.

## Current MCP mapping

- **feasibility:** native_with_kind_verification
- **tools:** ["photoshop_place_image", "photoshop_convert_to_smart_object", "photoshop_get_layers", "photoshop_select_layer_by_name", "photoshop_scale_layer", "photoshop_move_layer", "photoshop_rotate_layer", "photoshop_fit_layer_to_document", "photoshop_replace_smart_object_contents", "photoshop_edit_smart_object_contents", "photoshop_create_smart_object_via_copy", "photoshop_save_document"]
- **parameter_constraints:** {"place": "filePath exists; x/y absolute top-left canvas coordinates in pixels, not offsets from Photoshop's default centered Place. Placement invokes AM Plc then translates its actual bounds.", "convert": "Optional exact layer_name; background layer is rejected; existing Smart Object returns already_smart_object. Do not use this conversion as background-removal preparation.", "scale": "scalePercent >=1 applies the same percentage to both axes; centerAnchor true by default, false uses top-left. Background or an empty layer cannot transform.", "move": "deltaX/deltaY are relative pixel offsets; rotation degrees use middle-center.", "fit": "fillDocument false fits inside with possible margins; true fills the canvas and can crop subjects.", "replace": "file_path must be absolute and exist; optional exact layer_name; embedded-content replacement, not a linked-file relink.", "edit_contents": "Opens embedded PSB as active document: re-list and pin IDs before returning to the parent. Do not assume the original tab stayed active.", "targeting": "Pin a positive document_id from current state on mutations, previews and save; use exact unique layer names."}
- **side_effects:** ["Place adds a layer and can auto-fit on import. Inspect bounds rather than assuming native source scale.", "Convert bundles content; edit-contents changes active document; ordinary duplicate instances may share content, whereas via-copy is independent.", "Replace changes embedded source while retaining transforms; do not confuse preserving transforms with preserving the old source content."]
- **sources_inspected:** ["src/tools/image-placement-tools.ts", "src/tools/smart-object-tools.ts", "src/api/extendscript.ts:1264", "src/api/extendscript.ts:1792", "src/api/extendscript.ts:1850", "src/api/extendscript.ts:4581"]

## Historical execution report, not an installation test

- **status:** historical_report_not_reproduced_here
- **reported_status:** validated_place_convert_scale_components
- **reported_checked_on:** 2026-11-09
- **reported_environment:** {"photoshop": "27.11.0", "mcp": "1.7.37", "commit": "ba36d8f2a28ecc56686568f3c0191e388336d498"}
- **observations:** ["Convert-to-Smart-Object retained SMARTOBJECT kind after80% uniform scale.", "Separate clipping case confirms place_image imported an embedded Smart Object."]
- **limits:** ["Replace/edit contents, independent copies and production output quality were not tested.", "Historical development summary only. Raw logs, local paths and fixture files are not distributed; installation does not run or certify this operation."]

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/applying-filters-basics
- **title:** Apply filters — part 2: placing the foreground image
- **checked_on:** 2026-11-09
- **content_read:** transcript
- **coverage:** Part 2 placement, positioning and committing the transform were read. The video itself was not played.

- {"url": "https://www.adobe.com/products/photoshop/smart-objects.html", "title": "Create embedded Smart Objects", "content_read": "article_text", "coverage": "Adobe Help content surfaced at an Adobe product URL: embedded creation routes and editing contents."}

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
