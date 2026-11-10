# Limit a layer or adjustment with a clipping mask

ID: `clipping-masks` · Theme: `layers`

## Problem

Restrict an upper layer's visible contribution or adjustment to the content of a specific base layer.

## Use when

- An adjustment should affect one composited object without altering the surrounding image.
- An image or effect should appear within the visible content of a shape or text layer.

## Avoid when

- Do not clip when the desired adjustment should affect all layers beneath it.
- Do not treat a clipping mask as identical to a painted layer mask.
- Do not alter an existing clipping chain without understanding its base and members.

## Preconditions

- Identify the base layer and the upper layer to restrict.
- Arrange them consecutively in the intended order and inspect the base's transparency.

## Limits

- A base layer's opaque content reveals the clipped content; transparent areas hide it.
- Additional clipped layers must remain consecutive, and moving layers into a chain can change its membership.
- Clipping does not repair inaccurate transparency already present in the base layer.

## Essential Adobe-documented steps

- Place the intended adjustment or image immediately above its base.
- Create the clipping relationship using the verified supported command.
- Change only the parameters needed for the requested result.
- Release the clipping relationship only when its broader effect is intended.

## Adapt to the image

- Adapt the base choice to which object should receive the edit.
- Tune the adjustment amount independently of the clipping relationship.
- Inspect chain membership and layer order after any reordering.

## Visual verification

- Check the Layers panel for the expected clipping indication and base relationship.
- Compare the object's change against adjacent content that should remain untouched.
- Inspect semitransparent edges and test that removing or hiding the adjustment restores the expected previous appearance.

## Current MCP mapping

- **feasibility:** native_clipping_create_and_release
- **tools:** ["photoshop_create_clipping_mask", "photoshop_release_clipping_mask", "photoshop_get_layers", "photoshop_select_layer_by_name", "photoshop_move_layer_to_position", "photoshop_get_preview"]
- **parameters:** {"document_id": "Pin the target document.", "layer_name": "Optional exact name for recursive lookup on create/release; omit only if inspected active layer is definitely the intended upper layer.", "layer_relationship": "The upper layer must sit directly above its base in the same parent stack. No independent base_layer_id/base_layer_name parameter is exposed.", "reorder_if_needed": "photoshop_move_layer_to_position accepts targetLayerName and position ABOVE, BELOW, TOP, BOTTOM. Reordering can alter rendering and must be scoped deliberately."}
- **limits:** ["The create tool checks that a layer exists directly below and then invokes Action Manager groupEvent. It does not assess whether that base's visible pixels are the correct boundary for the request.", "A layer already grouped returns success with already_clipping:true. This does not verify that its existing base relationship is the one requested.", "Release sets layer.grouped=false. For a multi-layer chain, inspect the resulting chain and rendering rather than assuming every other relationship stayed unchanged.", "Clipping controls scope/visibility; the adjustment value or image positioning still requires a separate actual tool. Do not map an unsupported editable adjustment to a destructive atomic operation simply because clipping itself is native.", "Bottom-most target returns no_base_layer_below; a non-clipped release returns not_clipping. Follow the structured envelope and inspect the stack before a bounded correction.", "get_layers does not expose layer.grouped or parent relationships, so it does not prove the clipping chain on its own. Confirm the create/release result, permitted targeted structural metadata, and the visual scope together."]
- **server_contract_notes:** ["Inspect state/layers and pin document_id; name collisions must be resolved by actual structure rather than guessed matching.", "Use native create/release for this precise operation; no execute_script is needed when these tools cover it.", "Verify expected clipped-layer indication/base, the unchanged neighboring content, and mask-edge rendering before recording visual validation."]
- **implementation_evidence:** ["validation/environment-20261109/discovery.json: create/release schemas, optional layer_name, document_id, and reorder properties.", "photoshop-mcp/src/tools/mask-tools.ts:131-202: native create/release schemas and structured snippet parsing.", "photoshop-mcp/src/api/extendscript.ts:1000-1020: finds the directly lower layer in the same parent container.", "photoshop-mcp/src/api/extendscript.ts:3160-3216: optional layer activation, no-base check, already-clipped result, Action Manager creation.", "photoshop-mcp/src/api/extendscript.ts:3220-3276: grouped-state check and release via layer.grouped=false."]

## Historical execution report, not an installation test

- **status:** historical_report_not_reproduced_here
- **reported_status:** validated_mechanism_partial_fill
- **reported_checked_on:** 2026-11-09
- **reported_environment:** {"photoshop": "27.11.0", "mcp": "1.7.37", "commit": "ba36d8f2a28ecc56686568f3c0191e388336d498"}
- **observations:** ["Placed photo remains a Smart Object with grouped:true above a base with hasUserMask:true.", "Photo pixels appear only in the rectangular base region."]
- **limits:** ["Photo was500px high and did not cover the lower120px of the base; red base remains there. This validates clipping mechanics, not a completed fill/mockup. Fit scale/placement before final compositing.", "Historical development summary only. Raw logs, local paths and fixture files are not distributed; installation does not run or certify this operation."]

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/adjustment-layer
- **title:** Fine-tune an image adjustment layer
- **checked_on:** 2026-11-09
- **content_read:** written_steps
- **coverage:** Read complete article on clipping an adjustment to the layer below and controlling local adjustment strength with masks.
- **sections_read:** ["Control which layers are affected by your adjustment layer", "Make an adjustment to selective parts of an image", "Vary your adjustments"]
- **supplemental_sources:** [{"url": "https://helpx.adobe.com/photoshop/desktop/create-masks/layer-masks/create-and-manage-clipping-masks.html", "title": "Create and manage clipping masks", "content_read": "article_text", "coverage": "Read the complete desktop article: base transparency, consecutive chain membership, creation, release, and blend-group note."}]

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
