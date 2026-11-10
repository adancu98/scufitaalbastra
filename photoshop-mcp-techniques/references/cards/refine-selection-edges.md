# Refine soft and contaminated selection edges

ID: `refine-selection-edges` · Theme: `selections`

## Problem

Improve a selection whose soft edges retain background fringes or omit fine subject detail.

## Use when

- Close inspection reveals missing hair, foliage, fabric edges, or visible background contamination.
- The target will be composited against a background that makes those defects noticeable.

## Avoid when

- Do not refine an already adequate selection merely because the command exists.
- Do not shrink an entire mask aggressively to conceal a few local errors.
- Do not bypass the server's remove-background stop/error contract with this tutorial.

## Preconditions

- Start with a relevant selection or editable mask and identify the intended target layer.
- Confirm which refinement controls the current MCP actually exposes; a Photoshop UI brush is not automatically an MCP capability.

## Limits

- Radius, edge shift, and brush-based edge inspection solve different problems.
- Global changes may damage correct hard edges while improving a different soft edge.
- No MCP execution or video-frame analysis is claimed by this research card.

## Essential Adobe-documented steps

- Evaluate the initial selection using an overlay color that contrasts with the subject and a preview over the intended composite.
- Adjust edge detection only where the soft transition requires it.
- Use edge shift for observed fringes and local add/subtract corrections for localized mistakes.
- Where available, apply an edge-refinement brush only over the defective soft boundaries.
- Retain an editable layer-mask output when the verified route supports it.

## Adapt to the image

- Adapt radius to the pixel scale of the soft boundary, not the full canvas size.
- Choose edge shift conservatively from the visible fringe width.
- Use local brush sizes that distinguish the defect from nearby correct detail.

## Visual verification

- Inspect the edge at close view and at intended viewing size over the destination background.
- Look for halos, missing fine details, hard cutouts, and accidental holes.
- Compare against the source to ensure preserved details remain credible.

## Current MCP mapping

- **feasibility:** partial_native_global_modifiers_only
- **tools:** ["photoshop_expand_selection", "photoshop_contract_selection", "photoshop_feather_selection", "photoshop_get_selection_bounds", "photoshop_get_preview", "photoshop_execute_script"]
- **parameters:** {"document_id": "Pin the document containing the inspected active selection.", "pixels": "Expand, contract, or feather require a finite pixel value >=1; handlers round to a minimum integer1. These are absolute selection modifiers, not the tutorial's percent Shift Edge setting.", "script": "Only for a missing operation with a scoped, independently checked implementation; this mapping supplies no tested Refine Edge Brush or Select and Mask script."}
- **limits:** ["No atomic refine_selection, Select and Mask workspace, Refine Edge Brush, Refine Hair, Smart Radius, Color/Object Aware mode, Decontaminate Colors, or interactive mask-view controls appear in this live catalog.", "Expand/contract/feather globally change the existing selection. They do not classify hair/foliage edges, replace a local refinement brush, or preserve every currently correct edge automatically.", "The tutorial's selection-to-layer-mask output can use create_layer_mask for a suitable ordinary masking intent, but that operation is a separate card and does not prove the refinement itself is equivalent.", "If the image needs edge classification or local brush correction unavailable through verified MCP controls, report the partial capability or use a permitted, separately verified script/manual route. Do not invent a native refinement tool."]
- **server_contract_notes:** ["Read state before action, inspect the actual edge defect, then choose only the modifier required. A global contraction must not be a default response to one local fringe.", "Do not use refinement atomics or scripts to continue an explicit background-removal intent after its strict recipe workflow has stopped or failed.", "A successful edge-modifier response is runtime evidence only. Close visual inspection of the important edge is required before recording the partial workflow as visually validated."]
- **implementation_evidence:** ["validation/environment-20261109/discovery.json: expand/contract/feather tools present; no Refine Edge Brush, Refine Hair, or full Select and Mask atomic tool among128 names.", "photoshop-mcp/src/tools/selection-tools.ts:37-41,105-166,450-535: pixel rounding and selection-modifier schema/handlers.", "photoshop-mcp/src/api/extendscript.ts:297-304,2745-2850: Action Manager Expand/Contract/Feather operations, without edge classification.", "photoshop-mcp/src/prompts/instructions.ts: background-removal exception and preview verification contract."]

## Historical execution report, not an installation test

- **status:** not_run
- **checked_on:** 2026-11-09
- **reason:** Not executed in the initial development batch; no runtime validation is bundled.

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/make-precise-selections-in-select-mask
- **title:** How to refine a selection with Select and Mask
- **checked_on:** 2026-11-09
- **content_read:** transcript
- **coverage:** Read accessible transcript and written summary, including overlays, Radius/Smart Radius, Shift Edge, local tools, Refine Hair, Refine Edge Brush, and layer-mask output; video not played.
- **sections_read:** ["Viewing and evaluating selections with overlays", "Using edge detection and global refinements", "Refining soft edges with selection tools", "Outputting the refined selection as a layer mask"]
- **supplemental_sources:** [{"url": "https://www.adobe.com/learn/photoshop/web/select-hair", "title": "Select hair like a pro", "content_read": "written_steps", "coverage": "Read article's initial selection, view modes, Refine Edge Brush, corrections, and layer-mask output."}]

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
