# Correct tonal ranges with an editable Curves layer

ID: `curves-adjustment-layer` · Theme: `color`

## Problem

A photograph has weak contrast or poorly separated shadows, midtones, and highlights.

## Use when

- Use when a simpler exposure adjustment cannot isolate the tonal range needing correction.
- Use channel curves only when a specific color cast also needs correction.

## Avoid when

- Do not apply a stylized S-curve automatically to a resize or export request.
- Avoid forcing contrast when it removes useful product detail.

## Preconditions

- Inspect image mode and histogram; the documented 0–255 coordinates describe RGB, not CMYK ink percentages.
- Choose the intended image layer and adjustment scope.

## Limits

- Curves redistributes existing tones; it cannot recover detail already absent from the source.
- One control point also influences neighboring tonal ranges.

## Essential Adobe-documented steps

- Add a Curves adjustment layer instead of applying Image > Adjustments directly.
- Start with the composite RGB channel. Add a small number of control points in the tonal range requiring correction.
- Raise a point to brighten that range or lower it to darken; refine other ranges only when needed.
- Use the adjustment mask to restrict the correction, and reduce opacity if the result is excessive.
- Keep the adjustment editable in the layered master.

## Adapt to the image

- Choose control-point input/output coordinates from the actual image, not a universal preset.
- Adapt channel, adjustment strength, opacity, and mask coverage.

## Visual verification

- Compare before/after at fit view and inspect important dark and bright detail at 100%.
- Check neutral colors and clipping; a stronger curve is not automatically a better result.

## Current MCP mapping

- **feasibility:** partial_native_editable_presets; custom_points_script_candidate_not_tested
- **tools:** ["photoshop_adjust_curves", "photoshop_select_layer_by_name", "photoshop_set_layer_opacity", "photoshop_get_state", "photoshop_get_layers", "photoshop_get_preview", "photoshop_execute_script"]
- **parameters:** {"photoshop_adjust_curves": {"preset": ["neutral", "auto_tone"], "document_id": "positive target id"}, "photoshop_set_layer_opacity": {"opacity": "0–100; adapt to image", "document_id": "positive target id"}, "photoshop_execute_script": {"code": "Reviewed self-contained JSX with explicit return; required only for a missing custom-point operation", "timeout_ms": "1000–600000; omit unless justified", "document_id": "positive target id"}, "image_dependent": "Custom input/output points, channels, mask scope, and layer opacity are not native Curves parameters."}
- **limits:** ["Native Curves exposes only preset, not curve points, channel, or mask coordinates.", "auto_tone is implemented as a fixed two-endpoint mapping (12,0) to (243,255), not an image-analyzed Auto Tone and not an S-curve with interior points. neutral uses (0,0) to (255,255).", "The native operation creates an adjustment layer and preserves underlying pixels. It does not by itself limit the effect to one image layer.", "A custom composite curve descriptor is structurally supported by inspected ActionDescriptor code, but changing its point list or channel is a script candidate until executed and visually inspected. Do not assume an internal __mcp helper is globally callable."]
- **server_contract_notes:** ["Read photoshop_get_state; capture and pass a positive document_id; select the intended layer by exact unique name when needed; inspect photoshop_get_preview after the meaningful change. All current live schemas reject additional properties.", "Prefer the native tool for its actual two presets. A request for custom points is not covered by that preset interface, so a scoped script may be considered and tested on a copy. Do not silently replace a precise request with auto_tone."]
- **implementation_evidence:** ["validation/environment-20261109/discovery.json (live 128 tools, server 1.7.37,2026-11-09)", "photoshop-mcp/src/tools/adjustment-tools.ts:132–153 (preset-only schema)", "photoshop-mcp/src/api/extendscript.ts:779–818 (actual two-point Curves descriptor)", "photoshop-mcp/src/api/extendscript.ts:2386–2401 (creates adjustment layer)", "photoshop-mcp/src/tools/action-tools.ts:38–74 (custom JSX escape hatch, explicit return)"]

## Historical execution report, not an installation test

- **status:** historical_report_not_reproduced_here
- **reported_status:** validated_native_preset_only
- **reported_checked_on:** 2026-11-09
- **reported_environment:** {"photoshop": "27.11.0", "mcp": "1.7.37", "commit": "ba36d8f2a28ecc56686568f3c0191e388336d498"}
- **observations:** ["Before/after visual comparison shows stronger contrast; a live Curves layer and mask sit above untouched source pixels."]
- **limits:** ["auto_tone is the fixed endpoint mapping, not adaptive analysis; custom points, local range tuning and neutral-reference matching were not validated.", "Historical development summary only. Raw logs, local paths and fixture files are not distributed; installation does not run or certify this operation."]

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/brighten-photo-basics
- **title:** Make an image brighter or darker
- **checked_on:** 2026-11-09
- **content_read:** article_text
- **coverage:** Learn article documents adjustment-layer exposure correction and masks; desktop Help supplies Curves graph behavior.
- **secondary_urls:** ["https://helpx.adobe.com/photoshop/desktop/adjust-color/color-corrections/adjust-color-and-tone-with-curves.html"]
- **source_ids:** ["cr-learn-exposure", "cr-help-curves"]

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
