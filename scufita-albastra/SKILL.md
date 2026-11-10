---
name: scufita-albastra
description: Create polished, editable Photoshop designs as ScufitaAlbastra, combining Adobe-backed techniques, art direction, connected image models and visual review. Use for substantial Photoshop design briefs, posters, product composites and campaign graphics, or when ScufitaAlbastra is invoked; route simple edits directly to Photoshop techniques.
---

# ScufitaAlbastra

Deliver a visually considered Photoshop design and an honestly described, editable PSD. A generated concept is a visual target; build the final document from independent assets, live text, masks and suitable native effects. Quality is demonstrated by the artwork and its structure, not by a successful command or the word “premium”.

## Choose the mode

- For a resize, export, cutout or precise correction, use [Photoshop MCP Techniques](../photoshop-mcp-techniques/SKILL.md) directly. Do not introduce concept generation, unrelated enhancements or this skill's full production workflow.
- For a substantial design brief, use the workflow below. Consult only the references needed for the task.
- For teaching, explain the relevant choice and demonstrate it in the requested document or a clearly identified disposable practice file. Do not silently turn a request for an explanation into edits.
- Configuration and learning work do not restart an earlier cancelled artwork. Read the technical library's scoped [preferences](../photoshop-mcp-techniques/references/preferences.json) and this skill's [preferences](references/preferences.json); current user instructions take precedence.

## Design and build

1. Establish the result, audience/viewing context, format, exact content, supplied assets and required editability. Resolve only missing information that materially affects the result. Use reasonable reversible choices where possible.
2. For open creative work, read [design and review](references/design-and-review.md). Explore a few genuinely different directions internally; select one against the brief and available references. Continue unless the user requested an approval checkpoint or an actual tool/permission requires one.
3. Make a concise composition and layer plan. Distinguish original products/logos, generated imagery, live type, native geometry and adjustments. References guide hierarchy, atmosphere and craft; do not copy a third party's whole design.
4. Read [model routing](references/model-routing.md) when generation or reference editing contributes to the result. The configured primary profile is GPT Image 2.6 Sunburst; Nano Banana 2.1 is the alternative. Discover current tools and model constraints. Configuration is not proof of runtime access, credits or image quality. Do not fabricate a working integration for optional models.
5. Follow [Photoshop MCP Techniques](../photoshop-mcp-techniques/SKILL.md) for state, document IDs, technique cards, server contract and runtime gates. Read [production and delivery](references/production-and-delivery.md) for substantial PSD authoring. Preserve unrelated documents and keep the intended source editable. Generated assets go into separate suitable layers/Smart Objects; final critical text is real Photoshop type.
6. Inspect overall preview and relevant detail after meaningful stages. Compare the actual result with the brief and visual target. Fix concrete weaknesses with bounded edits. If a critic is delegated, give it the brief and actual images without telling it the desired verdict; otherwise do a separate review pass yourself.
7. Save the editable master, reopen the saved deliverable and audit its relevant structure. Deliver a preview and brief evidence-based status. Claim print readiness, visual approval or full editability only to the extent actually checked.

## Persistence and boundaries

- Use the existing Adobe library selectively. Its catalog is incomplete; preserve its progress and source/runtime distinctions. Do not claim all Adobe tutorials were learned.
- Keep existing native background-removal routing and all technique-specific compatibility gates. Do not insert the audit/crop helpers into the strict three-call cutout sequence.
- Keep an asset manifest (origin/provider/model, request/job ID if present, actual dimensions, local path, transparency and intended role) and a review record for substantial work. Record explicit user preferences with scope; rejected artwork is not an approved style reference.
- The [model registry](references/model-registry.json) records observed connector availability separately from runtime testing. Local Qwen/Ming, Ideogram and Recraft are optional candidates until actually connected and tested. Do not download large checkpoints or subscribe to providers merely because their names occur there.
- Use supplied authentic product imagery when fidelity is required. Do not regenerate product geometry, logos, labels or factual details to make a composition easier.
- Use the agent's image understanding on native Photoshop previews for visual review. No additional paid critic model is required. Generated concepts, source knowledge, structural checks and human approval are different evidence.

## Helpers

Read [production and delivery](references/production-and-delivery.md) before running a helper. Helpers are scoped to an explicitly pinned document or an authorized local asset and do not replace visual inspection.

- `scripts/audit-document.jsx`: recursive read-only document/layer evidence.
- `scripts/export-review-crop.jsx`: full-pixel detail crop from a temporary merged copy; preserves the source.
- `scripts/fetch_asset.py`: download a completed, authorized provider result to local Photoshop assets with format/size checks.

Install these skills into your own Codex environment. Model routing does not change the chat's underlying model, train its weights or provide autonomous background work.
