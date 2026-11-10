# Extend an image boundary with Generative Expand when generated surroundings are acceptable

ID: `generative-expand` · Theme: `generative`

## Problem

A requested aspect ratio needs extra image area while retaining the existing subject.

## Use when

- The requested format needs more surrounding scene than the source contains and new generated surroundings are acceptable.
- Ordinary crop, canvas extension or placement cannot sufficiently meet the request.

## Avoid when

- Do not substitute generation for a simple resize.
- Do not describe generated scene or reconstructed missing product parts as a genuine photograph of that content.

## Preconditions

- Inspect the source and decide the exact output aspect ratio and preserved content.
- Check desktop version, current MCP support, account, internet and model/credit conditions separately before generation.

## Limits

- The tutorial's 4:5 ratio and three variations are examples, not universal output requirements.
- A crop boundary represents proportions, not centimeters or inches. Current model support must be discovered rather than inferred from the tutorial.

## Essential Adobe-documented steps

- Choose the Crop tool's Generative Expand mode and set the needed aspect ratio.
- Extend the boundary while keeping all source content that must be preserved inside it; position the original deliberately.
- Use an optional prompt only if the needed new area requires explicit direction; otherwise contextual expansion may suffice.
- Generate and inspect variations. Preserve the resulting generative layer and stop once the required area is usable.

## Adapt to the image

- Final pixel dimensions and ratio; expansion amount on each edge; original image position; prompt; model; variation and credit budget.

## Visual verification

- Compare with the original to confirm important source content remains.
- Inspect horizon continuity, perspective, repeated structures and transitions at expansion seams. Check the enlarged output's actual dimensions.

## Current MCP mapping

- **feasibility:** partial_native_exact_geometry_unavailable
- **tools:** ["photoshop_get_capabilities", "photoshop_generative_expand", "photoshop_get_preview"]
- **parameter_constraints:** {"prompt": "Optional prompt defaults to extend the background naturally; empty strings are replaced by that phrase. Native blank prompting is not exposed.", "direction": "Only left,right,top,bottom,all are accepted.", "unexposed_controls": "No expansion amount, per-edge pixel amounts, target width/height, aspect ratio, original placement, model, variation or budget parameter. The exact4:5 Adobe example cannot be promised via this tool alone.", "implementation": "Invokes one of generativeExpand/expandCanvas/generativeCanvasExpand with prompt+direction. It does not explicitly resize the canvas or set a crop boundary beforehand.", "wait": "Completion uses the same history-count heuristic and may report ok:true while wait.completed:false; inspect resulting geometry and pixels before reporting success."}
- **side_effects:** ["May enlarge the canvas with generated content and consume credits; all output dimensions and preserved source content need post-inspection.", "Do not use to replace a simple resize or reconstruct missing authentic product details.", "Any exact-geometry script/manual lane would require its own implementation, authorization and disposable-copy validation; no such lane was validated here."]
- **sources_inspected:** ["src/tools/generative-tools.ts:218", "src/tools/generative/_shared.ts", "src/api/extendscript.ts:3995", "src/platform/capabilities.ts"]
- **capability_observed:** {"generative_expand": true, "generative_fill_guard_used_by_handler": true, "actual_generation": "not_run", "account_and_credits": "not_verified"}

## Historical execution report, not an installation test

- **status:** not_run
- **checked_on:** 2026-11-09
- **reason:** Not executed in the initial development batch; no runtime validation is bundled.

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/expand-image-generative-fill
- **title:** How to expand images with generative AI in Photoshop
- **checked_on:** 2026-11-09
- **content_read:** transcript
- **coverage:** Full available transcript read, including ratio, repositioning, optional prompt and generative layer comparison. Video not played.

- {"url": "https://helpx.adobe.com/creative-cloud/apps/generative-ai/creative-cloud-generative-ai-features.html", "title": "Creative Cloud Generative AI features", "content_read": "article_text", "coverage": "Generative Expand classification and variable plan/model conditions."}
- {"url": "https://helpx.adobe.com/photoshop/desktop/generative-ai/frequently-asked-questions-about-generative-ai-features.html", "title": "Generative AI features FAQ", "content_read": "article_text", "coverage": "Internet and layered-output prerequisites; do not hardcode older cost or resolution statements."}

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
