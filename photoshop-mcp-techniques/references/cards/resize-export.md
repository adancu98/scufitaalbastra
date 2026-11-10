# Resize or set print resolution, then export only as required

ID: `resize-export` · Theme: `export`

## Problem

An image must meet specified pixel dimensions, a physical output size or a delivery format without unnecessary visual changes.

## Use when

- Resize for an explicit screen/web dimension, or set physical-size/PPI metadata for a defined print workflow.
- Export a separate delivery copy in the required format and color space.

## Avoid when

- Do not add retouch, color grading, sharpening or effects to a resize-only request.
- Do not claim extra captured detail after upsampling, or prescribe 300 PPI to every large-format print.

## Preconditions

- Read source pixel dimensions, profile and target requirements.
- Distinguish changing pixel count, changing print-size/PPI allocation and adding canvas space; they are different operations.

## Limits

- PPI metadata does not determine on-screen pixel dimensions.
- Resampling adds or removes pixels; substantial enlargement may soften detail. The tutorial's 300-PPI advice is a typical desktop inkjet example, not a universal mural specification.

## Essential Adobe-documented steps

- For pixel resizing, link width and height, use pixel units and enable Resample; enter the needed dimension and verify the result.
- For print-size/PPI allocation without changing pixel count, disable Resample and set the physical size or resolution intentionally.
- Save/export a separate version when the original must remain untouched.
- If delivery requires Export As, choose the needed format and quality; convert to and embed sRGB only when appropriate for that delivery.

## Adapt to the image

- Target pixels or physical units; aspect-ratio policy; resampling method; PPI; format; JPEG quality; transparency; output profile; profile embedding.

## Visual verification

- Verify output pixel dimensions, aspect ratio, profile and transparency as applicable.
- Inspect fine detail, edges and text in the actual exported file. Check the file opens; a successful export response alone does not validate visual quality.

## Current MCP mapping

- **feasibility:** native_pixel_resize_and_export_partial_print_profile_controls
- **tools:** ["photoshop_resize_image", "photoshop_export_as", "photoshop_save_document", "photoshop_recipe_prepare_for_web", "photoshop_recipe_export_social_variants", "photoshop_execute_script"]
- **parameter_constraints:** {"pixel_resize": "width,height>=1px required; BICUBIC resampling always, current resolution retained. No constrain-ratio toggle: calculate the second dimension proportionally when appropriate. No interpolation choice or resample:false/PPI-only control.", "export_as": "path required, PNG/JPEG/WEBP/AVIF, quality0–100(default80), optional artboard_id; no width/height/profile/conversion/embedding/transparency parameter. PNG/JPEG use Save for Web defaults; they do not explicitly set conversion or profile embedding.", "save_document": "path required; PSD/JPEG/PNG; JPEGquality1–12(default8). PSD/JPEG save snippets embed existing profile but do not convert color space.", "web_recipe": "max_dimension_px64–8192(default2048), jpeg/png, quality1–12(default9), optional path. It duplicates a merged source, attempts sRGB conversion, downscales only if larger, then attempts fixed UnsharpMask30%,0.6px,0. Source unchanged; both profile and sharpen errors are swallowed.", "social_recipe": "Requested supported platform slugs only. Center-crops and resizes; does not recompose important subjects. Not suitable when crop would remove essential content.", "missing_controls": "Resolution-only changes with no resampling, chosen interpolation, exact print setup or explicit profile handling need an inspected script/manual path and separate validation."}
- **side_effects:** ["resize_image resamples the whole document and all layers; work on a copy where original preservation is required.", "Web recipe includes sharpening even if not requested and may succeed despite failed profile conversion. Do not use it for resize-only or unchanged-pixel export.", "export_as writes a copy but may overwrite the requested path. Reopen/inspect actual exported dimensions, profile, transparency and visual quality; a tool response alone is insufficient.", "Artboard exports use duplicate+crop; WEBP/AVIF rely on available native save option constructors, not just version labels."]
- **sources_inspected:** ["src/api/extendscript.ts:242", "src/api/extendscript.ts:1340", "src/api/extendscript.ts:1609", "src/api/extendscript.ts:4823", "src/tools/export-tools.ts", "src/tools/recipes/prepare-for-web.ts", "src/tools/recipes/export-social-variants.ts"]

## Historical execution report, not an installation test

- **status:** historical_report_not_reproduced_here
- **reported_status:** validated_screen_resize_export_paths
- **reported_checked_on:** 2026-11-09
- **reported_environment:** {"photoshop": "27.11.0", "mcp": "1.7.37", "commit": "ba36d8f2a28ecc56686568f3c0191e388336d498"}
- **observations:** ["1920×800 resized to960×400 without a style change; PNG opens at960×400.", "Explicit web-optimization recipe exported640×267 JPEG with embedded ICC; source document preview stayed identical."]
- **limits:** ["Atomic PNG export has no ICC in this test; do not promise profile conversion/embedding.", "Web recipe includes sharpening; it is not used merely for resizing.", "PPI-only changes, CMYK/print conversion, PDF and enlargement detail were not tested.", "Historical development summary only. Raw logs, local paths and fixture files are not distributed; installation does not run or certify this operation."]

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/image-resizing-basics
- **title:** Change the image size
- **checked_on:** 2026-11-09
- **content_read:** transcript
- **coverage:** Resize and resolution chapters read, including link proportions, Resample, PPI meaning and preserving the original. Other chapters not ingested into this card.

- {"url": "https://helpx.adobe.com/photoshop/desktop/save-and-export/export-files-to-different-formats/export-settings-and-export-location-preferences.html", "title": "Export settings and export location preferences", "content_read": "article_text", "coverage": "Export sizing, quality, transparency and sRGB conversion/profile embedding sections."}

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
