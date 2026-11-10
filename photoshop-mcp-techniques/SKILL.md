---
name: photoshop-mcp-techniques
description: Choose and apply source-backed Photoshop techniques through the user's Photoshop MCP server for image edits, selections, masks, layers, color, retouching, composites, type, Smart Objects, generative edits, resizing and export. Use for Photoshop work; do not route photographic work into Illustrator or apply unrelated enhancements to a simple edit.
---

# Photoshop techniques

Use the smallest intervention that achieves the requested result. Techniques are conditional options, not required effects. Resizing alone does not imply retouching, grading, sharpening, generation, or a style change.

For substantial creative design briefs or work assigned to ScufitaAlbastra, use the installed [ScufitaAlbastra workflow](../scufita-albastra/SKILL.md) for art direction, connected generation, visual review and editable PSD delivery. This library remains the technical source of truth; simple edits stay in the direct technique workflow.

## Before editing

1. Identify the requested output, target, constraints and acceptance criteria. Read [preferences.json](references/preferences.json), applying only entries whose scope matches. Current instructions override older preferences.
2. Discover live tools and prompts; use advertised schemas, not remembered names/parameters. Bootstrap with `photoshop_ping` once per MCP session. Read `photoshop_get_capabilities` once per session before suggesting version-dependent/AI features.
3. Read `photoshop_get_state` before mutations. With multiple documents, list them and capture a positive `document_id`; pin mutations, previews, saves and closes. Never infer the intended target from the front tab. Preserve unrelated documents.
4. Read the [technique index](references/index.md), then only the relevant cards. Check their separate Adobe, MCP and runtime evidence. Read [compatibility.md](references/compatibility.md) when bridging tutorials to tools, preserving editability or checking uncertain features. Server initialize instructions remain the technical contract.

## Select and execute

- Prefer a matching `photoshop_recipe_*` for a multi-step requested outcome, after checking side effects. Use an atomic tool for a single precise change. The web recipe includes sharpening: do not use it merely to resize or export unchanged pixels.
- Adapt selections, curve strength, mask transitions, crop bounds, transforms, type and export settings to this image. Coordinates/dimensions are pixels; font sizes are points. Do not copy tutorial shortcuts or fixed values as universal defaults.
- Preserve originals. Prefer masks, adjustment layers and Smart Objects when the actual tool supports them. Some atomic color/filter/crop tools destroy pixels or rasterize Smart Objects. If an editable operation lacks a native tool, use a verified scoped script only when permitted, or state the missing capability. Do not invent a tool or silently substitute a destructive operation.
- Judge composition against its context: focal hierarchy, product scale, edges, perspective, lighting, believable color and viewing distance. Successful execution does not prove aesthetic quality.
- Generative flags establish version-based possibility, not login, credits, model access or successful generation. Consult the card and actual feature response. Neural Filters additionally require the reachable UXP bridge. Preserve authentic product details when the brief requires real photography.

### Strict background-removal exception

For remove-background/cut-out/isolate/transparent-background intent, follow exactly: `photoshop_get_state` once → `photoshop_recipe_remove_background` once → `photoshop_get_preview` once → stop. Do not rasterize, duplicate, hide, select subject, create/apply masks, delete layers, use scripts or use generative removal as a workaround for this intent. If the recipe fails, report its envelope. The glossary's manual fallback does not override this strict contract. Ordinary selections/masks for other intents are separate techniques.

Resolve the intended document before that three-call sequence. Do not insert a generic helper's extra state/list/script calls between its steps. The knowledge-project validation helper is not a background-removal wrapper.

For gradient-mask work, read the card's runtime gates before using a recipe on an existing mask: a confirmed channel-targeting defect can paint RGB pixels. The tested explicit-mask-channel preparation avoids that observed case; it still replaces mask values instead of multiplying an isolation mask.

## Verify and retain experience

- Inspect `photoshop_get_preview` after meaningful stages and final export. Check overall composition and relevant detail. If a critical edge is not visible, do not mark it passed.
- Verify dimensions, aspect ratio, live type, layer/mask presence, Smart Object kind, profile and file readability as applicable. For print, distinguish pixels, physical size, effective source resolution and printer requirements. PPI metadata does not create detail.
- Preserve structured errors, reread state and recover one bounded step. A timeout does not stop Photoshop: wait for successful ping before state queries; at most one controlled longer-timeout execute-script retry. Never follow an error hint that violates the background-removal contract.
- Test new workflows on disposable copies. A recipe is validated only for the recorded input, parameters, environment and inspected result; do not generalize one fixture pass to every image.
- Record useful results/errors in `references/experience.jsonl`: date, card ID, tool/recipe, versions, fixture, parameters, raw log/preview paths, visual observations and limits. Update runtime status only with actual evidence. Keep explicit user corrections in `preferences.json` with scope/provenance; a project constraint is not a universal style rule.
- For expansion, read [progress.json](references/progress.json), process the next bounded batch, and preserve pending/inaccessible pages and transcript limits. Write practical paraphrases with Adobe links/dates. Do not claim the whole catalog was studied.

This persistent library supports future work; files and test records do not establish autonomous learning or permanent background execution.
