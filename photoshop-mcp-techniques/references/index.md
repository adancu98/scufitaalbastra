# Photoshop technique index

Read only relevant cards. A simple resize does not require sharpening, retouching or generation. Runtime reports are historical summaries; raw local evidence is not distributed and installation does not validate your Photoshop environment.

| Technique | Theme | Current MCP feasibility | Runtime report |
|---|---|---|---|
| [Geometric selections and selection arithmetic](cards/geometric-selections.md) | selections | partial_native | historical_report_not_reproduced_here |
| [Select the principal subject automatically](cards/select-subject.md) | selections | native_subject_selection_only | historical_report_not_reproduced_here |
| [Refine soft and contaminated selection edges](cards/refine-selection-edges.md) | selections | partial_native_global_modifiers_only | not_run |
| [Hide and reveal content with an editable layer mask](cards/editable-layer-masks.md) | masks | partial_native_mask_creation_not_interactive_painting | historical_report_not_reproduced_here |
| [Create a gradual transition on a layer mask](cards/gradient-mask-blend.md) | masks | native_linear_gradient_with_preservation_and_targeting_limits | historical_report_not_reproduced_here |
| [Organize related layers into meaningful groups](cards/organize-layer-groups.md) | layers | partial_native_recipe_not_semantic_grouping | historical_report_not_reproduced_here |
| [Limit a layer or adjustment with a clipping mask](cards/clipping-masks.md) | layers | native_clipping_create_and_release | historical_report_not_reproduced_here |
| [Correct tonal ranges with an editable Curves layer](cards/curves-adjustment-layer.md) | color | partial_native_editable_presets; custom_points_script_candidate_not_tested | historical_report_not_reproduced_here |
| [Neutralize an unwanted color cast, then refine tonal color balance](cards/neutralize-color-cast.md) | color | documented_only_for_gray_eyedropper_and_color_balance; no_verified_exact_execution_path | not_run |
| [Adjust a color range with Hue/Saturation and a spatial mask](cards/targeted-hue-saturation.md) | color | partial_native_destructive_global_HSL; editable_global_layer_script_candidate_not_tested; targeted_range_and_mask_editing_not_verified | not_run |
| [Repair small blemishes on a separate retouch layer](cards/spot-heal-separate-layer.md) | retouch | Spot Healing_documented_only; selected_content_aware_repair_available_destructively_on_a_copy | not_run |
| [Clone controlled source detail onto an editable retouch layer](cards/clone-stamp-controlled-repair.md) | retouch | documented_only_no_dedicated_tool_or_verified_brush_script | not_run |
| [Crop and straighten while preserving intended framing](cards/crop-straighten-composition.md) | composition | native_destructive_rectangular_crop; no_native_nondestructive_or_document_straighten_control | historical_report_not_reproduced_here |
| [Align a layer with proportional transforms; use perspective correction only when needed](cards/transform-perspective-alignment.md) | composition | native_proportional_scale_move_rotate; perspective_and_PerspectiveWarp_not_exposed_or_verified | historical_report_not_reproduced_here |
| [Place and transform an asset as an editable Smart Object](cards/smart-object-place-transform.md) | smart-objects | native_with_kind_verification | historical_report_not_reproduced_here |
| [Apply a purposeful filter as a re-editable Smart Filter](cards/smart-filters.md) | smart-objects | script_or_manual_only_for_editable_filter | historical_report_not_reproduced_here |
| [Create readable text on editable Type layers](cards/editable-type.md) | text | native | historical_report_not_reproduced_here |
| [Use Generative Fill for an explicitly needed local content change](cards/generative-fill.md) | generative | partial_native_unverified_service_access | not_run |
| [Extend an image boundary with Generative Expand when generated surroundings are acceptable](cards/generative-expand.md) | generative | partial_native_exact_geometry_unavailable | not_run |
| [Resize or set print resolution, then export only as required](cards/resize-export.md) | export | native_pixel_resize_and_export_partial_print_profile_controls | historical_report_not_reproduced_here |

See [compatibility](compatibility.md), [progress](progress.json), [sources](sources.json), [preferences](preferences.json), [historical validation](validation-history.json) and [experience](experience.jsonl). The complete Adobe catalog has not been studied.
