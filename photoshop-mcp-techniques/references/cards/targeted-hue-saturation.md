# Adjust a color range with Hue/Saturation and a spatial mask

ID: `targeted-hue-saturation` · Theme: `color`

## Problem

One color is too dull, intense, or incorrectly hued while other colors should remain unchanged.

## Use when

- Use when the requested correction is specific to a color or object.
- Use a spatial mask when the same color appears elsewhere and should not change.

## Avoid when

- Avoid global saturation increases that damage skin or product colors.
- Do not recolor an authentic product unless that change is requested.

## Preconditions

- Identify the target color range and any protected areas.
- Confirm whether the adjustment should be clipped to one image layer.

## Limits

- A chosen color range affects matching colors throughout the image; it does not identify an object.
- Large hue or saturation changes can reveal color artifacts.

## Essential Adobe-documented steps

- Create a Hue/Saturation adjustment layer above the intended content.
- Choose a color family or sample it with the targeted adjustment tool instead of leaving Master selected by habit.
- Adjust only the requested properties: hue changes the color, saturation its intensity, and lightness its brightness.
- For local changes, start with a black adjustment mask and reveal the correction with white only where required.
- Clip the adjustment to the intended layer when other image layers must be protected.
- Save the layered master with the adjustment intact.

## Adapt to the image

- Adapt color range, hue shift, saturation, lightness, opacity, and mask transition.
- Tutorial example values such as +60 saturation are specific to its practice image and are not defaults.

## Visual verification

- Compare the target and protected colors at fit view, then inspect edges and gradients at 100%.
- Verify that skin, adjacent objects, and colors in other layers remain appropriate.

## Current MCP mapping

- **feasibility:** partial_native_destructive_global_HSL; editable_global_layer_script_candidate_not_tested; targeted_range_and_mask_editing_not_verified
- **tools:** ["photoshop_adjust_hue_saturation", "photoshop_recipe_apply_color_grade", "photoshop_create_clipping_mask", "photoshop_set_layer_opacity", "photoshop_get_state", "photoshop_get_preview", "photoshop_execute_script"]
- **parameters:** {"photoshop_adjust_hue_saturation": {"hue": "-180–180", "saturation": "-100–100", "lightness": "-100–100", "document_id": "positive target id"}, "photoshop_create_clipping_mask": {"document_id": "positive target id"}, "photoshop_execute_script": {"code": "A self-contained editable global HSL adjustment descriptor can be derived from the inspected recipe helper, then tested on a copy", "document_id": "positive target id"}, "missing_native_controls": ["Reds/Yellows/etc color-family range", "on-image color sampling", "new editable HSL adjustment with arbitrary values", "brush painting on an existing adjustment mask"]}
- **limits:** ["The atomic HSL tool applies Image>Adjustments once to pixels, rasterizes text/SmartObjects, and resets non-Normal blend modes to Normal. It does not create an adjustment layer.", "The color-grade recipe creates editable HSL+brightness/contrast layers but exposes only six style presets and applies globally. It is not suitable for a specific product-color edit.", "An upstream recipe helper builds a global editable HSL layer using ActionDescriptor/ActionList; its code is an implementation reference for a scoped script, not a globally callable function.", "A custom global HSL layer does not establish support for targeted color families or accurate spatial-mask painting. Both require independent implementation evidence and tests.", "Vibrance is editable natively but cannot replace an exact hue change."]
- **server_contract_notes:** ["Read photoshop_get_state; capture and pass a positive document_id; select the intended layer by exact unique name when needed; inspect photoshop_get_preview after the meaningful change. All current live schemas reject additional properties.", "Prefer the recipe only when its actual global preset matches a requested stylistic grade. For exact targeted recoloring, preserve the gap instead of silently rasterizing or adding an unrelated grade."]
- **implementation_evidence:** ["validation/environment-20261109/discovery.json (live 128 tools, server 1.7.37,2026-11-09)", "photoshop-mcp/src/tools/adjustment-tools.ts:58–89 (atomic HSL schema and declared rasterization)", "photoshop-mcp/src/api/extendscript.ts:2282–2339 (rasterization, blend reset, global HStr descriptor)", "photoshop-mcp/src/tools/recipes/_shared.ts:122–143 (editable global HSL descriptor helper)", "photoshop-mcp/src/tools/recipes/apply-color-grade.ts:25–61 (fixed presets, global only)", "photoshop-mcp/src/api/extendscript.ts:4308–4337 (Vibrance adjustment layer is different)"]

## Historical execution report, not an installation test

- **status:** not_run
- **checked_on:** 2026-11-09
- **reason:** Not executed in the initial development batch; no runtime validation is bundled.

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/make-colors-pop-in-photo
- **title:** Make colors pop in a photo
- **checked_on:** 2026-11-09
- **content_read:** transcript
- **coverage:** Read visible desktop Learn transcript and written steps, including targeted colors and masks. Web adjustment tutorial independently documents clipping scope; its web UI is not an MCP procedure.
- **secondary_urls:** ["https://www.adobe.com/learn/photoshop/web/edit-photos-adjustment-layers"]
- **source_ids:** ["cr-learn-color-pop", "cr-learn-web-adjustments"]

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
