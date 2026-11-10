# Select the principal subject automatically

ID: `select-subject` · Theme: `selections`

## Problem

Obtain an initial selection of the photograph's main subject without tracing every boundary manually.

## Use when

- The requested edit concerns the principal subject, such as a local color or tone correction.
- Automatic selection can provide a useful starting point for a selection that will be inspected.

## Avoid when

- Do not assume the principal subject is the specific object requested in a multi-object scene.
- For the server's remove-background intent, follow its dedicated recipe contract instead of reproducing this tutorial's Select Subject plus mask chain.

## Preconditions

- Make the subject-containing layer the intended target.
- Check the installed Photoshop capabilities and the live MCP tool schema before using AI-assisted selection.

## Limits

- The tutorial describes Cloud and Device processing choices; this research does not prove that MCP exposes that preference or that cloud processing is available to this account.
- Low contrast, reflections, and thin details can produce imperfect or soft boundaries.

## Essential Adobe-documented steps

- Target the layer containing the requested subject.
- Run Select Subject through the verified supported route.
- Inspect the subject selection and its excluded interior areas.
- Use the selection for the requested local operation, or refine a demonstrated defect before proceeding.

## Adapt to the image

- Adapt the decision to use this selector to subject count and visual separation from the background.
- Do not silently change global image-processing preferences to match the tutorial's example.
- Refinement strength must follow observed edge problems rather than a preset.

## Visual verification

- Inspect both the outside contour and holes between thin details at close view.
- Check that the intended subject was selected completely and unrelated objects were not included.
- Recheck the actual edit at normal viewing size; a selection's presence is not evidence of acceptable image quality.

## Current MCP mapping

- **feasibility:** native_subject_selection_only
- **tools:** ["photoshop_get_capabilities", "photoshop_select_subject", "photoshop_select_layer_by_name", "photoshop_get_selection_bounds", "photoshop_get_preview"]
- **parameters:** {"document_id": "Pin the inspected subject-containing document.", "sample_all_layers": "Optional boolean, default false. It affects the autoCutout fallback only; the first DOM selectSubject() attempt does not receive that argument.", "subject_target": "The active layer is the target; use the existing exact-name selector when the intended layer is not already active. No per-object id, cloud/device preference, or selection model parameter is exposed."}
- **limits:** ["The tool creates a pixel selection, not a mask and not the complete Select and Mask workspace.", "Handler checks Photoshop23+ when detected information is available. A version/capability flag does not establish successful subject detection or cloud account/network availability.", "The snippet tries DOM doc.selection.selectSubject(), then Action Manager autoCutout, and verifies that some selection exists. That does not establish that the requested subject or every thin detail was selected correctly.", "Photoshop's interactive Object Selection, Refine Edge Brush, and Cloud/Device preference controls are not exposed by this tool. Do not equate sample_all_layers with any of those controls."]
- **server_contract_notes:** ["Use for an ordinary principal-subject selection needed for a permitted local edit, after capabilities/state discovery and with visual inspection.", "For remove-background/cut-out/isolate/transparent-background intent, this atomic tool is expressly forbidden by initialize instructions. Use the dedicated recipe exactly once after one get_state, then one preview and stop.", "The handler internally calls connection.ping(); this implementation detail is distinct from the host's once-per-session photoshop_ping bootstrap and is not a reason for the agent to add repeated ping calls."]
- **implementation_evidence:** ["validation/environment-20261109/discovery.json: photoshop_select_subject schema exposes only sample_all_layers plus document_id.", "photoshop-mcp/src/tools/selection-tools.ts:333-354,786-825: selection-only description, version check, fallback argument, parsed result.", "photoshop-mcp/src/api/extendscript.ts:2960-3009: DOM selectSubject and autoCutout fallback, selection-existence check.", "photoshop-mcp/src/prompts/instructions.ts: background-removal hard rule and AI-capability discovery requirement."]

## Historical execution report, not an installation test

- **status:** historical_report_not_reproduced_here
- **reported_status:** executed_partial_visual_check
- **reported_checked_on:** 2026-11-09
- **reported_environment:** {"photoshop": "27.11.0", "mcp": "1.7.37", "commit": "ba36d8f2a28ecc56686568f3c0191e388336d498"}
- **observations:** ["Select Subject produced non-empty bounds; a selected-area Curves adjustment and mask were created on the photo copy.", "Overall product remains readable."]
- **limits:** ["1200px preview cannot establish spoke/gap/foliage boundary accuracy of the1920px source. Fine edges are explicitly not validated.", "Historical development summary only. Raw logs, local paths and fixture files are not distributed; installation does not run or certify this operation."]

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/select-subject-one-click
- **title:** How to select a subject with one click in Photoshop
- **checked_on:** 2026-11-09
- **content_read:** transcript
- **coverage:** Read accessible transcript from introduction through final workflow tips and written summary; did not play the video.
- **sections_read:** ["Selecting a main subject with select subject", "Understanding select subject settings and preferences", "Creating detailed masks for complex subjects", "Refining composites and final workflow tips"]
- **supplemental_sources:** [{"url": "https://helpx.adobe.com/photoshop/desktop/make-selections/automatic-color-based-selections/detect-subject-using-select-subject.html", "title": "Detect subject using Select Subject", "content_read": "article_text", "coverage": "Read desktop command overview and advice to use Object Selection for one specific object among multiple subjects."}]

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
