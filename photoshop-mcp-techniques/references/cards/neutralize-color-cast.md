# Neutralize an unwanted color cast, then refine tonal color balance

ID: `neutralize-color-cast` · Theme: `color`

## Problem

Lighting gives nominally neutral objects an unwanted blue, green, or warm cast.

## Use when

- Use when faithful color is part of the requested result and a reliable neutral reference exists.
- Use Color Balance for residual casts isolated to shadows, midtones, or highlights.

## Avoid when

- Do not neutralize intentional sunset or colored lighting merely because it is not neutral.
- Do not assume a colored object should be gray.

## Preconditions

- Identify a credible neutral patch and inspect the whole scene.
- Confirm whether correction should affect one layer, a masked region, or the full image.

## Limits

- A gray-point correction depends on the sample location.
- A global neutralization can be inadequate for mixed lighting.

## Essential Adobe-documented steps

- Add a Levels adjustment layer and use its gray eyedropper on a patch that should be neutral.
- Compare alternative credible sample locations if the first correction looks wrong.
- Lower adjustment opacity when neutralization is too strong.
- If a residual tonal cast remains, add a Color Balance adjustment layer; inspect midtones first, then shadows and highlights.
- Move complementary-color sliders only as required. Preserve Luminosity keeps the correction from unnecessarily changing brightness.
- Keep masks and correction layers editable.

## Adapt to the image

- Adapt sample position, tonal range, Cyan/Red, Magenta/Green, Yellow/Blue amounts, opacity, and mask.
- Adobe documents Color Balance sliders from -100 to +100; these are bounds, not suggested starting values.

## Visual verification

- Check multiple neutral references and important material or skin colors before and after.
- Reject a correction that makes the reference neutral while making the subject less credible.

## Current MCP mapping

- **feasibility:** documented_only_for_gray_eyedropper_and_color_balance; no_verified_exact_execution_path
- **tools:** ["photoshop_get_state", "photoshop_get_preview", "photoshop_select_layer_by_name", "photoshop_set_layer_opacity"]
- **parameters:** {"photoshop_set_layer_opacity": {"opacity": "0–100 for an already existing correction layer", "document_id": "positive target id"}, "missing_native_controls": ["Levels gray eyedropper or neutral-reference sampling", "Color Balance adjustment creation and tonal sliders", "preserve_luminosity for Color Balance"]}
- **limits:** ["No Color Balance or gray-eyedropper tool appears among the current128 advertised tools.", "photoshop_auto_levels is available but performs a direct automatic pixel adjustment; it accepts neither a neutral sample nor an amount and rasterizes text/SmartObjects. It is not the Adobe neutral-reference workflow.", "Exposure, Vibrance, global Hue/Saturation, and Curves presets are different operations, not substitutes for a promised Color Balance or gray-point correction.", "Generic execute_script availability alone does not validate an editable Color Balance ActionManager descriptor. No such verified implementation was found in the inspected repository. A future script requires primary API evidence and a fixture test before being advertised as operational."]
- **server_contract_notes:** ["Read photoshop_get_state; capture and pass a positive document_id; select the intended layer by exact unique name when needed; inspect photoshop_get_preview after the meaningful change. All current live schemas reject additional properties.", "If the exact correction is necessary, report this gap or use a separately verified manual/script path. Do not invent photoshop_color_balance, a gray-point parameter on auto_levels, or an untested brush/sample function."]
- **implementation_evidence:** ["validation/environment-20261109/discovery.json (live 128 tools, server 1.7.37,2026-11-09)", "photoshop-mcp/src/tools/adjustment-tools.ts:94–118 (Auto Levels without inputs; destructive side effects)", "photoshop-mcp/src/api/extendscript.ts:2345–2360 (Auto Levels implementation)", "photoshop-mcp/src/api/extendscript.ts:2275–2282 (comment distinguishes Color Balance from Hue/Saturation; not an editable Color Balance tool)", "photoshop-mcp/src/tools/action-tools.ts:38–74 (generic JSX does not prove a specific descriptor)"]

## Historical execution report, not an installation test

- **status:** not_run
- **checked_on:** 2026-11-09
- **reason:** Not executed in the initial development batch; no runtime validation is bundled.

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/remove-unwanted-color-cast
- **title:** Correct an unwanted color cast
- **checked_on:** 2026-11-09
- **content_read:** transcript
- **coverage:** Read full visible Learn transcript and written recap. Desktop Color Balance Help provides the optional tonal-range refinement.
- **secondary_urls:** ["https://helpx.adobe.com/photoshop/desktop/adjust-color/color-corrections/apply-color-balance-and-photo-filter-adjustments.html"]
- **source_ids:** ["cr-learn-color-cast", "cr-help-color-balance"]

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
