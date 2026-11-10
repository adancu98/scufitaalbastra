// Prepend SCUFITA_DOCUMENT_ID and SCUFITA_CROP={left,top,right,bottom,path}.
// Pin the same document_id on photoshop_execute_script. Writes one new JPEG only.
if (typeof SCUFITA_DOCUMENT_ID !== 'number' || !isFinite(SCUFITA_DOCUMENT_ID) || SCUFITA_DOCUMENT_ID <= 0 || Math.floor(SCUFITA_DOCUMENT_ID) !== SCUFITA_DOCUMENT_ID) {
    return { ok: false, code: 'explicit_document_id_required', message: 'Set a positive integer SCUFITA_DOCUMENT_ID.' };
}
if (!app.documents.length || app.activeDocument.id !== SCUFITA_DOCUMENT_ID) {
    return { ok: false, code: 'document_mismatch', message: 'The active document must match the pinned document id.' };
}
if (typeof SCUFITA_CROP !== 'object' || SCUFITA_CROP === null) {
    return { ok: false, code: 'crop_required', message: 'Set SCUFITA_CROP with pixel bounds and a new absolute JPEG path.' };
}
var cropSource = app.activeDocument;
var cropTemporary = null;
var cropResult = null;
var cropOldDialogs = app.displayDialogs;
try {
    var cropSpec = SCUFITA_CROP;
    var cropFields = ['left', 'top', 'right', 'bottom'];
    var cropIndex, cropValue;
    for (cropIndex = 0; cropIndex < cropFields.length; cropIndex++) {
        cropValue = cropSpec[cropFields[cropIndex]];
        if (typeof cropValue !== 'number' || !isFinite(cropValue) || Math.floor(cropValue) !== cropValue) { throw new Error('Crop coordinates must be finite integer pixels.'); }
    }
    if (cropSpec.left < 0 || cropSpec.top < 0 || cropSpec.right <= cropSpec.left || cropSpec.bottom <= cropSpec.top || cropSpec.right > cropSource.width.as('px') || cropSpec.bottom > cropSource.height.as('px')) {
        throw new Error('Crop bounds must be inside the source canvas with positive width and height.');
    }
    if (typeof cropSpec.path !== 'string' || !/^(\/|[A-Za-z]:[\\\/]|\\\\)/.test(cropSpec.path) || !/\.jpe?g$/i.test(cropSpec.path)) {
        throw new Error('Use an absolute .jpg or .jpeg output path.');
    }
    var cropOutput = new File(cropSpec.path);
    if (!cropOutput.parent.exists) { throw new Error('The output parent directory must already exist.'); }
    if (cropOutput.exists) { throw new Error('Refusing to overwrite an existing file. Choose a new review path.'); }
    var cropWidth = cropSpec.right - cropSpec.left;
    var cropHeight = cropSpec.bottom - cropSpec.top;
    app.displayDialogs = DialogModes.NO;
    cropTemporary = cropSource.duplicate('scufita-review-temporary-' + new Date().getTime(), true);
    cropTemporary.crop([UnitValue(cropSpec.left, 'px'), UnitValue(cropSpec.top, 'px'), UnitValue(cropSpec.right, 'px'), UnitValue(cropSpec.bottom, 'px')]);
    // JPEG review requires a compatible temporary document; never convert the source.
    if (cropTemporary.mode !== DocumentMode.RGB) { cropTemporary.changeMode(ChangeMode.RGB); }
    if (cropTemporary.bitsPerChannel !== BitsPerChannelType.EIGHT) { cropTemporary.bitsPerChannel = BitsPerChannelType.EIGHT; }
    if (cropTemporary.width.as('px') !== cropWidth || cropTemporary.height.as('px') !== cropHeight) { throw new Error('The temporary crop dimensions differ from the requested pixels.'); }
    var cropOptions = new JPEGSaveOptions();
    cropOptions.quality = 12;
    cropOptions.embedColorProfile = true;
    cropTemporary.saveAs(cropOutput, cropOptions, true, Extension.LOWERCASE);
    if (!cropOutput.exists || cropOutput.length <= 0) { throw new Error('No readable-size JPEG file was written.'); }
    cropResult = { ok: true, document_id: cropSource.id, path: cropOutput.fsName, source_width_px: cropSource.width.as('px'), source_height_px: cropSource.height.as('px'), crop: { left: cropSpec.left, top: cropSpec.top, right: cropSpec.right, bottom: cropSpec.bottom }, width_px: cropWidth, height_px: cropHeight, resampled: false, bytes: cropOutput.length, review_only: true, limits: 'Merged RGB 8-bit JPEG crop; transparency and editable layers remain in the untouched source, not this review file.' };
} catch (cropError) {
    cropResult = { ok: false, code: 'review_crop_failed', document_id: SCUFITA_DOCUMENT_ID, message: String(cropError) };
} finally {
    if (cropTemporary !== null) {
        try { cropTemporary.close(SaveOptions.DONOTSAVECHANGES); }
        catch (cropCloseError) { cropResult = { ok: false, code: 'temporary_close_failed', document_id: SCUFITA_DOCUMENT_ID, message: String(cropCloseError), prior_result: cropResult }; }
    }
    try { app.activeDocument = cropSource; }
    catch (cropRestoreError) { cropResult = { ok: false, code: 'source_restore_failed', document_id: SCUFITA_DOCUMENT_ID, message: String(cropRestoreError), prior_result: cropResult }; }
    app.displayDialogs = cropOldDialogs;
}
return cropResult;
