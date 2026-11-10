# Compatibility and conflicts

Checked2026-11-09: local MCP master ba36d8f2a28ecc56686568f3c0191e388336d498,v1.7.37, live tools/list, Photoshop27.11.0. Evidence: upstream source inspection and sanitized historical summaries in [validation-history.json](validation-history.json). Raw local recordings are not distributed.

## Resolutions before integration

| Sources | Difference | Resolution |
|---|---|---|
| llms.txt vs AGENTS.md/live discovery | Old index says122 tools/23prompts; live128/24 | Use current schema/implementation, not stale counts. |
| Recipe glossary vs initialize strict rule | Glossary offers manual selection after background-removal version failure; initialize forbids that workaround | Preserve state→remove-background recipe→preview→stop; report errors. Selection/mask cards apply to other intents. |
| Adobe editable adjustments vs native hue/saturation/brightness/auto-levels tools | These atomics change pixels and may rasterize text/Smart Objects | Curves/exposure/vibrance create adjustment layers. Editable Hue/Saturation/Color Balance need a verified script or manual operation; native support is partial. A similar effect is not an equivalent tool. |
| Adobe Smart Filters vs MCP filters | Sharpen/noise and some filter snippets rasterize Smart Objects | Conversion to Smart Object does not prove a subsequent filter is editable. Inspect/test each actual path. |
| Adobe non-destructive Crop option vs MCP crop | MCP crop deletes outside pixels | Use disposable copies; do not advertise non-destructive cropping or invented straighten parameters. |
| Default-export guidance vs required save/export path | Some atomics require a path | Prefer recipe relative paths under configured export root; resolve that root for atomics. Use other destinations only within user-authorized scope. |

## Platform and version limits

- The development environment reported generative_fill/remove/expand/upscale flags true, largely from version thresholds. They do not test login, credits, model access or generation. Generative execution remains not_run.
- The development environment reported neural_filters:false and uxp_bridge_reachable:false; inspect your own connection. The library does not install the optional bridge.
- `/learn/photoshop/web/` in a URL alone does not identify Photoshop on the web. Read the actual platform/UI text; explicitly web/mobile tutorials are conceptual support, not desktop MCP instructions.
- An inaccessible video is not analyzed. Mark whether written steps or a transcript were actually read and what remains unavailable.
- Transform shortcut behavior varies. Preserve proportions numerically with actual MCP parameters instead of copying legacy Shift instructions.
- PPI metadata does not create detail.300ppi is not a universal wall-print requirement; consider source pixels, physical size, viewing distance and printer requirements.
- Adobe generative models, credit charges and output resolution change. Do not encode an old one-credit/1024px statement as a current guarantee; verify the applicable feature/plan when generation is requested.

## Additional implementation findings and runtime gates

- Confirmed in Photoshop on a1200×800 copy: `recipe_gradient_fade` on an existing mask with RGB selected painted the RGB pixels instead of the mask. Preview/run: the historical validation summary. Do not use this unprepared path. Explicitly selecting the mask channel through the tested `verified-scripts/select-layer-mask.jsx` before the recipe avoided that case (`12-safe-mask-gradient`). The recipe still replaces mask values, so it is not an intersection/multiplication with a subject isolation mask. A new reveal-all mask worked in `03-gradient`.
- `angle_deg` is computed/reported but does not change endpoints in the inspected gradient implementation; only the four actual axis directions are mapped. Do not advertise arbitrary-angle support.
- `organize_layers` can regroup interleaved layers and change appearance. The simple image+type fixture preserved identical preview pixels; that is not a guarantee for clipped/blended/interleaved artwork.
- `get_layers` is flattened and lacks mask/clipping ancestry evidence; `create_layer_mask` may report success after a no-op. Inspect the actual layer descriptor and visual result. Fixture masks and clipping were separately confirmed by `hasUserMask` and `grouped` descriptors.
- Native Curves `auto_tone` is the fixed two-endpoint mapping(12,0)→(243,255), not image analysis or a custom S-curve. Custom points are not exposed by this tool.
- Generative Fill rejects an empty prompt although Adobe supports empty-prompt fill; Expand lacks exact target ratio/dimension/model controls. `ok:true` may report invocation while `details.wait.completed:false`; do not mark generation complete from the envelope alone.
- ExtendScript here lacks the native `JSON` global. Custom code requires an explicit `return` to report a value. A reporting failure can occur after the edit already happened: get_state/inspect first rather than repeating the edit. Initial Smart Filter test captured this error and recovered without repeating the blur.

### Runtime labels

The initial [server inventory](server-inventory.json) records128 tools,17 recipes and24 prompts and distinguishes inspected interfaces from executed recipes. Re-discover live tools before use.

Adobe documented = actual text/transcript read, URL/date and limits recorded. MCP mapped = advertised tools plus implementation inspected, possibly partial/destructive/script-only/manual-only. Runtime tested = executed with raw logs. Visually validated additionally needs inspected previews and recorded observations. A schema match or success response alone is not visual validation.

These are historical technical observations, not tests performed by cloning this package. Verify your own document, Photoshop version, bridge and live tool schemas.
