# Hide and reveal content with an editable layer mask

ID: `editable-layer-masks` · Theme: `masks`

## Problem

Control which parts of a layer remain visible while keeping the original image content recoverable.

## Use when

- The requested composite or local edit needs some content hidden and other content retained.
- The boundary may need correction after the first attempt.

## Avoid when

- Do not paint on image pixels when the intention is to edit a mask.
- Do not introduce a mask for an unrelated whole-image operation.
- For an explicit remove-background request, preserve the server's prescribed recipe workflow.

## Preconditions

- Identify the target layer and meaningful underlying content or transparency.
- Use a verified MCP route that can address the mask separately from image pixels.

## Limits

- White reveals, black conceals, and gray produces partial visibility; this does not change the underlying source pixels.
- A mask alone does not correct incompatible lighting, perspective, scale, or missing source detail.
- The tutorial's brush values are image-specific examples, not defaults for other files.

## Essential Adobe-documented steps

- Add an appropriate editable mask to the target layer.
- Ensure the mask, rather than the image thumbnail, is the active editing target.
- Place black on mask areas to conceal and white to restore; use gray only for intentional partial visibility.
- Inspect the mask and composite, then correct a mistaken concealed area by restoring white.

## Adapt to the image

- Adapt brush or mask-region size to the detail being edited.
- Match boundary hardness and transition width to the source edge.
- Use opacity for deliberate partial blending instead of unintentionally weakening the subject.

## Visual verification

- Inspect the mask itself and the rendered composite.
- Confirm the source content can be restored and that no image pixels were painted over accidentally.
- Check halos and visibility around critical subject details.

## Current MCP mapping

- **feasibility:** partial_native_mask_creation_not_interactive_painting
- **tools:** ["photoshop_create_layer_mask", "photoshop_select_all", "photoshop_select_rectangle", "photoshop_select_ellipse", "photoshop_get_layers", "photoshop_get_preview", "photoshop_execute_script"]
- **parameters:** {"document_id": "Pin the inspected target document and ensure the intended layer is active.", "create_mask": "No mask-mode, layer-name, brush, opacity, hardness, target-channel, or paint coordinates are exposed by create_layer_mask.", "selection": "For the advertised selection-based route, make the desired selection using supported tools; select_all represents an intentional reveal-all area. Existing masks are not replaced by this create operation."}
- **limits:** ["Native create_layer_mask supports a mask from the current selection. Its snippet also creates revealAll when no selection exists, even though the tool description states that a selection is a precondition.", "If a mask already exists, the snippet returns maskCreated:false and performs no update. The handler discards the snippet's returned status and still prints 'Layer mask created from selection'. Verify actual layer/mask state rather than relying on that text.", "The live128-tool surface has no atomic manual paint-on-mask brush with stroke points, brush hardness, or opacity. A selected-region mask fill would need a permitted, verified scoped script; it is not a native painting equivalent.", "photoshop_apply_layer_mask bakes/deletes concealed pixels and removes editability. It is not a step in this editable-mask technique.", "Do not automatically delete an existing mask or rasterize a layer to force a new mask. Preserve useful current work and choose an appropriate scoped operation.", "get_layers returns a flattened name/kind/visibility/opacity/blend-mode listing without mask-presence metadata. It cannot independently prove a mask exists; use permitted targeted structural inspection or an appropriate saved artifact, plus visual evidence."]
- **server_contract_notes:** ["Ordinary masks for compositing/local edits are distinct from explicit remove-background intent, where create_layer_mask and execute_script are forbidden and the dedicated recipe sequence must stop after preview.", "A scripted mask operation must explicitly target the mask channel rather than image pixels, have no matching native operation, and be verified on a disposable copy before promotion.", "A generic test helper may read state before ordinary mutations; it must not add extra get_state calls inside the strict state -> background-removal recipe -> preview sequence."]
- **implementation_evidence:** ["validation/environment-20261109/discovery.json: create_layer_mask schema has document_id only; no paint-mask brush tool.", "photoshop-mcp/src/tools/selection-tools.ts:288-310,703-727: advertised selection precondition and handler's unconditional creation confirmation.", "photoshop-mcp/src/api/extendscript.ts:3039-3070: existing-mask no-op; revealSelection versus revealAll behavior.", "photoshop-mcp/src/tools/selection-tools.ts:316-330: apply_layer_mask explicitly destroys hidden pixels and removes the mask.", "photoshop-mcp/src/api/extendscript.ts:1629-1677: getLayerNames provides no mask-presence field.", "photoshop-mcp/src/prompts/instructions.ts: strict background-removal forbidden operations."]

## Historical execution report, not an installation test

- **status:** historical_report_not_reproduced_here
- **reported_status:** validated_creation_fixture_only
- **reported_checked_on:** 2026-11-09
- **reported_environment:** {"photoshop": "27.11.0", "mcp": "1.7.37", "commit": "ba36d8f2a28ecc56686568f3c0191e388336d498"}
- **observations:** ["Preview contains only the selected red rectangle; hasUserMask:true was separately confirmed."]
- **limits:** ["Manual brush painting, fine edges and repeated create-mask no-op cases were not tested.", "Historical development summary only. Raw logs, local paths and fixture files are not distributed; installation does not run or certify this operation."]

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/combine-image-layer-mask
- **title:** How to combine images with a layer mask
- **checked_on:** 2026-11-09
- **content_read:** transcript
- **coverage:** Read accessible transcript and What you learned, including adding a white mask, targeting it, hiding with black, restoring with white, and inspecting it. Video not played.
- **sections_read:** ["Understanding the image setup and layer mask basics", "Creating a layer mask on the top layer", "Painting with black to hide areas and reveal the background", "Fixing mistakes by painting with white and viewing the mask"]
- **supplemental_sources:** []

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
