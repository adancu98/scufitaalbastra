# Geometric selections and selection arithmetic

ID: `geometric-selections` · Theme: `selections`

## Problem

Confine an edit to a known rectangular, elliptical, or straight-sided region instead of changing the entire photograph.

## Use when

- The target has measurable geometric boundaries.
- Only part of a layer should receive an adjustment, fill, or mask.

## Avoid when

- Do not make a selection for a simple whole-image resize.
- Do not approximate hair, curved product details, or spokes with a rectangle.

## Preconditions

- Identify the intended document, layer, canvas dimensions, and whether an existing selection must be preserved.

## Limits

- A visible selection border does not describe partial transparency along a feathered edge.
- The beginner tutorial demonstrates direct image adjustments; this library prefers an adjustment layer or mask when the verified MCP path permits editability.

## Essential Adobe-documented steps

- Choose the simplest suitable geometric selector and define its bounds.
- Add missing regions or subtract excess regions rather than starting again unnecessarily.
- Invert the selection only when the complementary area is the intended target.
- Perform the requested local operation, then deselect so later edits are not accidentally restricted.

## Adapt to the image

- Adapt bounds to the actual document pixels and target geometry.
- Use zero feather for intentionally crisp boundaries; increase it only for a visibly required transition.
- Use a fixed ratio or equal dimensions only when the request requires those proportions.

## Visual verification

- Preview the boundary against the intended object at close view.
- Compare the edited and untouched regions; confirm no spill beyond the intended area.
- Confirm that a later whole-image operation is no longer constrained by a leftover selection.

## Current MCP mapping

- **feasibility:** partial_native
- **tools:** ["photoshop_select_rectangle", "photoshop_select_ellipse", "photoshop_select_all", "photoshop_invert_selection", "photoshop_deselect", "photoshop_get_selection_bounds", "photoshop_feather_selection", "photoshop_save_selection", "photoshop_execute_script"]
- **parameters:** {"document_id": "Pass the positive target document id from state/list_documents; the live schema includes document_id on these tools.", "rectangle": "left, top, right, bottom in document pixels; optional mode: replace, add, subtract, intersect. Default replace.", "ellipse": "left, top, right, bottom in document pixels; right > left and bottom > top. No combine-mode parameter is advertised.", "feather": "pixels >= 1; the handler rounds to an integer. For a crisp boundary, omit feather rather than passing zero.", "saved_selection": "Optional channel_name; saves an alpha channel, but no native load-selection tool is present in this discovery snapshot."}
- **limits:** ["Rectangle and ellipse are native; polygonal/freehand lasso and arbitrary path selection are not atomic tools in this 128-tool catalog. Scoped scripting is an unvalidated alternative only when no matching native operation exists and the intent permits it.", "Non-replace rectangle modes are advertised as Action Manager operations independent of SelectionType, but the inspected helper actually calls SelectionType.EXTEND, DIMINISH, or INTERSECT. Do not promise those modes work in every host/version before executing a fixture.", "Rectangle handler returns a text confirmation rather than parsed actual bounds. Read get_selection_bounds and inspect a resulting mask/local edit to verify geometry.", "Ellipse replaces the current selection. It does not expose the tutorial's add/subtract ellipse arithmetic, anti-alias switch, fixed ratio, or fixed size UI settings. Preserve proportions numerically through equal or ratio-derived bounds."]
- **server_contract_notes:** ["Bootstrap once per MCP session, inspect target state before action, and pin document_id. Adapt all bounds from the actual document dimensions.", "For explicit remove-background/cut-out/isolate/transparent-background intent, do not use this selection chain or a script workaround. Follow the strict state -> remove-background recipe -> preview -> stop sequence instead.", "A helper that automatically inserts get_state before every tool would break that strict background-removal sequence; exclude that intent from automatic per-tool state insertion. This mapping does not execute it."]
- **implementation_evidence:** ["validation/environment-20261109/discovery.json: advertised tool names and parameter schemas, server1.7.37.", "photoshop-mcp/src/tools/selection-tools.ts:72-233,416-565,569-614: ellipse/rectangle schemas and handlers, pixel modifier rounding.", "photoshop-mcp/src/api/extendscript.ts:306-334: __mcp_selectRect uses SelectionType for non-replace modes despite the description's contrary claim.", "photoshop-mcp/src/api/extendscript.ts:2707-2850: ellipse and selection edge modification snippets.", "photoshop-mcp/src/prompts/instructions.ts: strict background-removal and state/document-pinning contract."]

## Historical execution report, not an installation test

- **status:** historical_report_not_reproduced_here
- **reported_status:** validated_rectangle_fixture_only
- **reported_checked_on:** 2026-11-09
- **reported_environment:** {"photoshop": "27.11.0", "mcp": "1.7.37", "commit": "ba36d8f2a28ecc56686568f3c0191e388336d498"}
- **observations:** ["Rectangle250,280–710,620 produced the expected red-only rectangular visible region. Selection bounds and mask descriptor were inspected."]
- **limits:** ["Ellipse, add/subtract/intersect arithmetic and difficult organic edges were not tested.", "Historical development summary only. Raw logs, local paths and fixture files are not distributed; installation does not run or certify this operation."]

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/rectangular-marquee-tool
- **title:** Learn selection basics
- **checked_on:** 2026-11-09
- **content_read:** transcript
- **coverage:** Accessible written transcript and What you learned section read; video not played or visually analyzed.
- **sections_read:** ["Creating a basic selection with the marquee tool", "Adding to and subtracting from selections", "Applying adjustments inside a selection", "Inverting and deselecting selections"]
- **supplemental_sources:** [{"url": "https://www.adobe.com/learn/photoshop/web/types-selection-tools", "title": "Try out simple selection tools", "content_read": "transcript", "coverage": "Read geometric and polygonal selection demonstrations and summary."}, {"url": "https://helpx.adobe.com/photoshop/desktop/make-selections/get-started-selections/make-selections-with-marquee-tools.html", "title": "Make selections with the Marquee tools", "content_read": "article_text", "coverage": "Read desktop tool options including feather, anti-aliasing, style, and selection modes."}]

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
