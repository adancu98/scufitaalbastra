# Editable Photoshop production

Read the technical library's [compatibility reference](../../photoshop-mcp-techniques/references/compatibility.md) and the relevant technique cards. Use current MCP schemas, including positive document IDs, rather than copying historical IDs or raw calls from test logs.

## Build an editable master

- Plan physical size, pixel dimensions, viewing context and output requirements separately. PPI metadata does not add pixels or recover detail. Ask the printer's requirements when necessary; 300 ppi is not a universal wall-art default.
- Keep original source assets accessible. Put substantial imported/generated imagery into independent Smart Objects when supported and verify the resulting layer kind. Preserve authentic product/logo assets when the brief requires fidelity.
- Create final text through Photoshop text tools with exact strings. Discover installed fonts and use actual PostScript names. Verify Romanian glyphs and actual bounds. A generator's text rendering does not prove the saved PSD has live type.
- Use native shapes/vector masks for suitable simple geometry, masks for editable isolation and adjustment layers for suitable tonal changes. Name useful layers and groups without automatically regrouping an existing artwork, which can change blend/clipping behavior.
- Preserve original masks. The library documents a gradient-mask channel defect and destructive filter paths. Converting a layer to a Smart Object does not make every subsequent atomic filter non-destructive.
- Save the master as PSD with layers. Export a separate preview. Flattening a duplicate for preview is different from flattening the master. Use PSB only if actual format limits require it and disclose the change.

## Evidence helpers

`audit-document.jsx` is a read-only inspector. Bind `var SCUFITA_DOCUMENT_ID = <positive numeric ID>;` before its contents, pass the same positive `document_id` to `photoshop_execute_script`, and use the returned tree to check ancestry, live type, real masks, adjustments and Smart Objects. Inspect failures instead of reporting unknown properties as passed. The script does not save, select layers or change pixels.

`export-review-crop.jsx` requires the same document-ID binding plus:

```javascript
var SCUFITA_CROP = {left: 0, top: 0, right: 600, bottom: 300, path: '/absolute/authorized/review/type.jpg'};
```

Choose the actual relevant bounds; this is an example, not a default. It crops a temporary merged duplicate and exports at the crop's original pixel dimensions, closes only that duplicate and restores the prior active document. Use an authorized destination directory that already exists and a new filename. Do not pass it into the background-removal sequence. A crop from the full document supports pixel-level inspection; zooming an already reduced preview does not.

`fetch_asset.py` transfers an explicitly authorized completed provider result URL to the local Photoshop workspace. Run `python3 scripts/fetch_asset.py --help` for flags. Pass URLs as properly quoted arguments without exposing signed queries in logs. It validates HTTPS, response MIME, format signatures, decoded pixels/dimensions, size and a new destination file, then prints a manifest with SHA-256. It uses Pillow when installed or the native macOS `sips` decoder here. It is an asset-import step, not a way to bypass media-display restrictions. Preserve provider widgets for presenting generated media.

## Before delivery

1. Save the master. Record its actual path and dimensions.
2. Reopen the saved file in a dedicated verification tab (preserving unrelated tabs), inspect its layer tree, exact critical text, masks and Smart Objects required by this design. Structural evidence supports editability; it does not prove the design looks good.
3. Inspect the overall preview and relevant detail. When safe on a disposable verification copy, changing a text word or moving an asset and undoing it can demonstrate live editability. Never do this test on an unrelated source document.
4. Check that the preview matches the saved master. Record any unverified print settings or missing source resolution. Separate a composition proof from a production master.
5. Return the PSD and a visible preview with a concise summary of completed checks and material limits. Do not call a single flattened image in a PSD a fully editable design.

For substantial jobs, keep compact `assets.json` and `review.json` alongside the project artifacts. Include real source/model/job paths and observations, not invented provenance or an empty checklist presented as completed work. This configuration has no approved reference pack yet; the first accepted designs can form one.
