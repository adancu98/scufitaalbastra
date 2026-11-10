# Use Generative Fill for an explicitly needed local content change

ID: `generative-fill` · Theme: `generative`

## Problem

A requested local addition, replacement or contextual fill needs newly generated image content.

## Use when

- The intended result permits generated content and cannot be achieved sufficiently by an ordinary requested edit.
- A defined selected region and a clear content objective exist.

## Avoid when

- Do not generate substitute vehicles, products or factual details when authentic photography is required.
- Do not run generations merely to test availability; capability discovery and account checks precede any credit-consuming execution.

## Preconditions

- Check installed Photoshop, current MCP capabilities, selected document/layer, active selection, online access and Adobe account entitlement independently.
- Verify the available model and its current credit terms; the presence of a tool or a version-based capability flag does not prove account access.

## Limits

- Output is invented content and needs inspection; a plausible preview is not proof of product accuracy.
- Model names, availability and credit consumption change. The current desktop Help lists newer models and retirement of Gemini 2.5 in v27.11+, so do not reuse older tutorial model assumptions.

## Essential Adobe-documented steps

- Define the smallest suitable selection, leaving enough context for the intended replacement.
- Invoke Generative Fill with a concise content description, or a blank prompt for contextual filling when appropriate.
- Choose a variation only after inspecting its content and its junction with the source.
- Keep the generative layer and original content separate; stop when the requested change is sufficient.

## Adapt to the image

- Selection bounds and shape; prompt; available model; variation; generation/output size; extent of context; allowed credit budget.

## Visual verification

- Inspect seams, lighting, perspective, repeated textures and malformed objects, plus all important unchanged source details.
- Compare the layer off/on and inspect the final output at actual delivery scale.

## Current MCP mapping

- **feasibility:** partial_native_unverified_service_access
- **tools:** ["photoshop_get_capabilities", "photoshop_generative_fill", "photoshop_select_rectangle", "photoshop_get_preview"]
- **parameter_constraints:** {"prompt": "Native handler trims and rejects an empty prompt as generative_unavailable:prompt is required. Adobe's blank-prompt contextual fill is not supported by this native tool.", "selection": "An active pixel selection is mandatory; establish it with a suitable verified selection tool for this content.", "unexposed_controls": "No model picker, generation size, variation selection or credit-budget parameter is advertised. Do not pass invented parameters or claim this tool selects a current Adobe/partner model.", "version": "Capability implementation gates generative_fill at major>=25, although tool prose saysPS24+. Use actual live feature flag and implementation, not the looser description.", "wait": "The action is attempted via fallback event IDs and uses a history-count completion heuristic. Returned ok:true can coexist with details.wait.completed:false; success can mean invoked rather than completed."}
- **side_effects:** ["May consume Adobe credits and create/modify content. Account/model access is not tested.", "May deselect the selection after invocation.", "Not a fallback for strict background removal; do not generate factual product details when authentic photography is required."]
- **sources_inspected:** ["src/tools/generative-tools.ts:178", "src/tools/generative/_shared.ts", "src/platform/capabilities.ts", "src/api/extendscript.ts:3814", "src/api/extendscript.ts:3903"]
- **capability_observed:** {"generative_fill": true, "actual_generation": "not_run", "account_and_credits": "not_verified"}

## Historical execution report, not an installation test

- **status:** not_run
- **checked_on:** 2026-11-09
- **reason:** Not executed in the initial development batch; no runtime validation is bundled.

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/the-unlock-add-to-a-scene-with-generative-fill
- **title:** Add to a scene with Generative Fill
- **checked_on:** 2026-11-09
- **content_read:** written_steps
- **coverage:** Three written step sections read. All embedded clips explicitly say Transcript not available; no video analysis claimed.

- {"url": "https://helpx.adobe.com/photoshop/desktop/create-open-import-images/create-images/edit-images-with-generative-fill.html", "title": "Edit images with Generative Fill", "content_read": "article_text", "coverage": "Desktop workflow, current model picker and model retirement note."}
- {"url": "https://helpx.adobe.com/photoshop/desktop/generative-ai/frequently-asked-questions-about-generative-ai-features.html", "title": "Generative AI features FAQ", "content_read": "article_text", "coverage": "Online connection, subscriber/trial access and generative layers; older cost/resolution claims require qualification."}
- {"url": "https://helpx.adobe.com/creative-cloud/apps/generative-ai/creative-cloud-generative-ai-features.html", "title": "Creative Cloud Generative AI features", "content_read": "article_text", "coverage": "October 1, 2026 standard/premium and plan/model-dependent credit distinctions."}

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
