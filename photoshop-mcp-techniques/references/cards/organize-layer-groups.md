# Organize related layers into meaningful groups

ID: `organize-layer-groups` · Theme: `layers`

## Problem

Make a layered document easier to target and maintain without flattening its editable elements.

## Use when

- Several layers represent one logical component and need coordinated management.
- Layer names or structure make reliable future targeting difficult.

## Avoid when

- Do not reorganize a user's document merely to perform a small unrelated edit.
- Do not merge or flatten layers as a substitute for grouping.
- Do not rename or move unrelated components outside the current task.

## Preconditions

- Inspect existing layer names, order, relationships, and document appearance.
- Determine the smallest set of related layers that actually benefits from grouping.

## Limits

- A group is an organizational container; it does not by itself validate the design.
- Moving a layer or group can alter stacking relationships, so the rendered result must be compared.
- The tutorial teaches manual grouping, while an MCP organize recipe may implement its own naming and grouping rules.

## Essential Adobe-documented steps

- Select the related layers while preserving their internal order.
- Create one meaningful group and name it according to its content or role.
- Move additional related layers into it only where appropriate.
- Address the group for coordinated visibility or movement; enter the group when editing an individual member.

## Adapt to the image

- Adapt group boundaries to the document's real semantic components.
- Use names that remain understandable in later turns.
- Keep nesting shallow unless distinct components require it; this is a library convention, not an Adobe requirement.

## Visual verification

- Compare before and after previews; pure organization should retain the intended appearance.
- Confirm all intended members are present in the correct order and unrelated layers remain outside.
- Verify that targeting one member is still possible and that coordinated group controls affect only the expected content.

## Current MCP mapping

- **feasibility:** partial_native_recipe_not_semantic_grouping
- **tools:** ["photoshop_recipe_organize_layers", "photoshop_rename_layer", "photoshop_get_layers", "photoshop_select_layer_by_name", "photoshop_execute_script", "photoshop_get_preview"]
- **parameters:** {"document_id": "Pin the inspected target document.", "naming_scheme": "type_index, content_summary, or preserve. content_summary uses the text content for text-layer slugs; it does not recognize image semantics.", "auto_group": "Default true. Set false for a rename-only organization that must preserve existing interleaving; still verify the result.", "rename_name": "For one requested rename, select the intended layer and use photoshop_rename_layer with name; duplicate names make future first-match targeting ambiguous."}
- **limits:** ["The recipe operates on top-level non-group layers and skips existing LayerSets. It is not recursive semantic organization of an existing complex document.", "When auto_group is true it creates new kind-based groups and moves layers into them. It does not explicitly restore cross-kind interleaving, clipping chains, or adjustment scope. The tool description's promise that visual output stays identical is not established by this implementation and needs image comparison.", "Move failures inside auto-grouping are caught and ignored, while group_count can still report created groups. Counts are not proof that every expected layer was moved.", "There is no native create-group/group-selected-layers/move-layer-into-group tool in this live catalog. Exact semantic grouping needs a permitted, scoped script for the missing operation or a manual route; no script has been validated by this mapping.", "A rename-only recipe avoids the recipe's reordering step but does not satisfy a request to create meaningful component groups by itself.", "get_layers flattens the recursive listing without parent ids or clipping membership. A successful group count plus this list cannot prove the preserved semantic tree or adjustment scope."]
- **server_contract_notes:** ["Prefer the existing recipe only when its actual naming and kind-grouping behavior fits the requested outcome. Do not reorganize unrelated content for a small edit.", "Use atomic rename for a single name change. Use execute_script only for the truly missing semantic-group operation, and preserve original order/relationships with scoped visual verification.", "Before/after preview comparison is required; do not accept a success count or the recipe description as evidence of unchanged appearance."]
- **implementation_evidence:** ["validation/environment-20261109/discovery.json: recipe properties, rename/name-selector tools, and absence of semantic group atomics.", "photoshop-mcp/src/tools/recipes/organize-layers.ts:55-65: collects top-level non-LayerSet layers only.", "photoshop-mcp/src/tools/recipes/organize-layers.ts:67-127: kind-based classification and naming, text slug behavior.", "photoshop-mcp/src/tools/recipes/organize-layers.ts:129-145: creates groups and moves kind-matched layers, ignores move exceptions.", "photoshop-mcp/src/api/extendscript.ts:1629-1677: flattened recursive layer listing without parent or grouped fields.", "photoshop-mcp/src/tools/layer-tools.ts:229-242: exact-name recursive depth-first matching, first duplicate wins."]

## Historical execution report, not an installation test

- **status:** historical_report_not_reproduced_here
- **reported_status:** validated_simple_fixture_only
- **reported_checked_on:** 2026-11-09
- **reported_environment:** {"photoshop": "27.11.0", "mcp": "1.7.37", "commit": "ba36d8f2a28ecc56686568f3c0191e388336d498"}
- **observations:** ["Image and live-text layers were placed in Images/Text groups; layer-set structure inspected.", "Before/after organization previews have identical pixels."]
- **limits:** ["No guarantee for interleaved, clipped, blended or semantically organized production layers.", "Historical development summary only. Raw logs, local paths and fixture files are not distributed; installation does not run or certify this operation."]

## Adobe source evidence

- **url:** https://www.adobe.com/learn/photoshop/web/organize-layers-with-layer-groups
- **title:** Tip: Organize your layers with layer groups
- **checked_on:** 2026-11-09
- **content_read:** transcript
- **coverage:** Read full accessible transcript and summary from selecting related layers to creating, naming, adding members, visibility, and moving grouped versus individual content. Video not played.
- **sections_read:** ["Understanding the purpose of layer organization", "Creating and naming layer groups", "Managing and moving grouped layers"]
- **supplemental_sources:** [{"url": "https://helpx.adobe.com/uk/photoshop/desktop/create-manage-layers/transform-manipulate-layers/group-and-ungroup-layers.html", "title": "Group and ungroup layers", "content_read": "article_text", "coverage": "Read grouping, ungrouping, and adding layers to groups."}]

Applicability and acceptance criteria are practical synthesis. Use the cited source coverage and current MCP capabilities; unavailable video content is not assumed analyzed.
