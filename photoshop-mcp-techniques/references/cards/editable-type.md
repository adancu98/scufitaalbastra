# Create readable text on editable Type layers

ID: `editable-type` · Theme: `text`

## Problem

A design requires text whose wording, appearance and placement can still be revised.

## Use when

- Text is requested or is necessary to the stated deliverable.
- Use point text for a short label or headline; use a paragraph box for longer controlled wrapping.

## Avoid when

- Do not add a slogan, label or logo to an image-only request.
- Do not rasterize type for routine styling or positioning. Do not select an arbitrary font just because the tutorial uses it.

## Preconditions

- Confirm the exact wording and the intended document.
- Choose an installed font or an explicitly supplied font file; account for document resolution because font size is measured in points.

## Limits

- A JPEG sharing copy does not retain editable type.
- A font appearing in a tutorial is not evidence that it exists on this machine. A text box can hide overflow that is not obvious in a small preview.

## Essential Adobe-documented steps

- Create point text by clicking with the Type tool, or paragraph text by dragging a box.
- Set the actual wording, font, point size, color and alignment; commit the text.
- Move the Type layer into position and adjust line wrapping or spacing only as needed.
- Keep editable type in the layered working file and export a separate delivery copy when required.

## Adapt to the image

- Installed font's PostScript name; point size; tracking; leading; paragraph box dimensions; alignment; position; color against the actual photograph.

## Visual verification

- Read every word at expected output size; inspect contrast over the image, clipped letters, unintended breaks and paragraph overflow.
- Verify the Type layer survives and that a wording edit still works. Check the exported copy separately.

## Current MCP mapping

- **feasibility:** native
- **tools:** ["photoshop_list_fonts", "photoshop_create_text_layer", "photoshop_update_text_content", "photoshop_set_text_style", "photoshop_set_text_font", "photoshop_set_text_alignment", "photoshop_set_text_ranges", "photoshop_move_layer", "photoshop_save_document"]
- **parameter_constraints:** {"content": "create/update text require exact text. Discover installed fontName/PostScript name using list_fonts.", "units": "x/y and paragraph box_width/box_height in pixels; fontSize and leading in points; tracking in1/1000em.", "style": "fontSize1–10000; leading0.1–10000; tracking−1000–10000; paragraph dimensions1–100000 rounded to integers; auto_leading true overrides fixed leading.", "color": "Supply red,green,blue together, each0–255. Supplying only one channel errors even though schema properties are individually optional.", "kind": "point or paragraph; supplying a box dimension defaults kind to paragraph unless explicitly set; avoid contradictory point+box inputs.", "ranges": "1–64 non-overlapping ranges; from inclusive and to exclusive, using JavaScript/ExtendScript string indices. Whole-layer styling uses set_text_style instead.", "routing": "Do not execute_script for tracking/leading/box or split mixed styles into extra layers unless the native tool fails."}
- **side_effects:** ["Creates or edits live Type layers; applying subsequent rasterizing filters destroys editability.", "Paragraph boxes can overflow; native success does not verify all wording remains visible.", "JPEG exports do not retain live text; save a layered PSD for further editing."]
- **sources_inspected:** ["src/tools/text-tools.ts", "src/tools/text-style-options.ts", "src/api/extendscript.ts"]

## Historical execution report, not an installation test

- **status:** historical_report_not_reproduced_here
- **reported_status:** validated_fixture_only
- **reported_checked_on:** 2026-11-09
- **reported_environment:** {"photoshop": "27.11.0", "mcp": "1.7.37", "commit": "ba36d8f2a28ecc56686568f3c0191e388336d498"}
- **observations:** ["Readable paragraph type with32pt size, tracking20 and leading40 remains LayerKind.TEXT after grouping."]
- **limits:** ["Mixed fonts/ranges, installed-font changes and clipping/overflow across other content were not tested.", "Historical development summary only. Raw logs, local paths and fixture files are not distributed; installation does not run or certify this operation."]

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/add-text-to-image
- **title:** Add text to your photos
- **checked_on:** 2026-11-09
- **content_read:** transcript
- **coverage:** Full tutorial transcript and written recap read: font, size, color, position and PSD preservation. No video playback claimed.

- {"url": "https://helpx.adobe.com/photoshop/desktop/text-typography/get-started-with-text/add-text.html", "title": "Add text", "content_read": "article_text", "coverage": "Point versus paragraph text mechanics."}

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
