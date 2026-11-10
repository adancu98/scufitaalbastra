# Apply a purposeful filter as a re-editable Smart Filter

ID: `smart-filters` · Theme: `smart-objects`

## Problem

A blur or other supported effect is needed, but its strength or coverage may change after review.

## Use when

- A requested blur, sharpening or supported effect benefits from revisable settings.
- An effect needs a mask or before-and-after comparison.

## Avoid when

- Do not add blur, sharpening or creative filters to a request that does not need them.
- Do not treat the tutorial's background blur as a default finishing step for every photograph.

## Preconditions

- Choose the correct content layer and convert it for Smart Filters if it is not already a Smart Object.
- Check filter compatibility with the document's mode, bit depth and installed Photoshop version.

## Limits

- Not all filters support this workflow; Adobe's current Help excludes, among others, Lens Blur and Vanishing Point.
- Rasterizing a Smart Object discards the editable Smart Filter relationship. Effect order matters because the stack is processed from the bottom upwards.

## Essential Adobe-documented steps

- Select the intended layer and use Convert for Smart Filters.
- Apply only the needed supported filter; for the documented example, adjust Gaussian Blur using its live preview.
- Check the filter entry beneath the Smart Object and re-open its settings to confirm it is adjustable.
- Use filter visibility or its mask for comparison or local coverage; preserve the layered working document.

## Adapt to the image

- Radius or effect amount relative to image size and intended viewing scale; filter order; blend mode and opacity; mask coverage.

## Visual verification

- Compare effect on and off at composition scale and at detail scale.
- Check edges for halos, excessive softness and abrupt mask boundaries; confirm the filter remains separately editable.

## Current MCP mapping

- **feasibility:** script_or_manual_only_for_editable_filter
- **tools:** ["photoshop_convert_to_smart_object", "photoshop_execute_script", "photoshop_get_layers", "photoshop_save_document"]
- **not_equivalent_tools:** ["photoshop_apply_gaussian_blur", "photoshop_apply_sharpen", "photoshop_apply_smart_blur", "photoshop_apply_high_pass"]
- **parameter_constraints:** {"native_blur": "radius0.1–250px, but the native Gaussian snippet rasterizes both TEXT and SMARTOBJECT before applying pixels. It cannot implement the Adobe editable Smart Filter technique.", "script": "A separately inspected and executed Action Manager/other supported script may be used through photoshop_execute_script when permitted. Code is not validated by existing tool availability; verify the resulting filter entry and editable source on a disposable copy.", "execute_script": "code string; timeout_ms1000–600000; current document_id pin. No scripts for the strict background-removal intent."}
- **side_effects:** ["Gaussian, sharpen, noise and motion blur atomics silently rasterize a Smart Object/text layer. A successful response may omit that fact.", "Smart Blur is a named pixel-filter effect, not a synonym for Smart Filters. The high-pass/smart-blur helpers reject unsupported layer kinds and suggest rasterization; do not follow that if editability is required."]
- **sources_inspected:** ["src/tools/filter-tools.ts", "src/api/extendscript.ts:2059", "src/api/extendscript.ts:2090", "src/api/extendscript.ts:2180"]

## Historical execution report, not an installation test

- **status:** historical_report_not_reproduced_here
- **reported_status:** validated_custom_script_fixture_only
- **reported_checked_on:** 2026-11-09
- **reported_environment:** {"photoshop": "27.11.0", "mcp": "1.7.37", "commit": "ba36d8f2a28ecc56686568f3c0191e388336d498"}
- **observations:** ["Exact stored Action Manager script applied5px Gaussian Blur; result reports SMARTOBJECT and smart_filter_count=1.", "Preview shows expected blur while source stays embedded. PSD saved."]
- **limits:** ["Native photoshop_apply_gaussian_blur remains unsafe for editability because it rasterizes.", "Filter parameter re-editing, other filters and complex documents were not tested.", "Initial case01 encountered JSON-is-undefined after applying blur; state/metadata was checked and the blur was not repeated during recovery.", "Historical development summary only. Raw logs, local paths and fixture files are not distributed; installation does not run or certify this operation."]
- **verified_script:** references/verified-scripts/smart-gaussian.jsx

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/applying-filters-basics
- **title:** Apply filters — part 2: Blur an image with Smart Filters
- **checked_on:** 2026-11-09
- **content_read:** transcript
- **coverage:** Conversion, Gaussian Blur preview, revisiting settings and layered PSD preservation read; video not played.

- {"url": "https://helpx.adobe.com/photoshop/desktop/effects-filters/smart-filters/apply-and-manage-smart-filters.html", "title": "Apply and manage Smart Filters", "content_read": "article_text", "coverage": "Smart Object prerequisite, stack order, editable properties, exclusions and rasterization consequences; updated October 4, 2026."}

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
