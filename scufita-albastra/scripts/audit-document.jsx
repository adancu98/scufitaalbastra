// Prepend: var SCUFITA_DOCUMENT_ID = <positive pinned document id>;
// Read-only inspection. Run through photoshop_execute_script with document_id pinned.
if (typeof SCUFITA_DOCUMENT_ID !== 'number' || !isFinite(SCUFITA_DOCUMENT_ID) || SCUFITA_DOCUMENT_ID <= 0 || Math.floor(SCUFITA_DOCUMENT_ID) !== SCUFITA_DOCUMENT_ID) {
    return { ok: false, code: 'explicit_document_id_required', message: 'Set a positive integer SCUFITA_DOCUMENT_ID.' };
}
if (!app.documents.length || app.activeDocument.id !== SCUFITA_DOCUMENT_ID) {
    return { ok: false, code: 'document_mismatch', message: 'The active document must match the pinned document id.' };
}
try {
    var auditDoc = app.activeDocument;
    var auditSummary = { layers: 0, groups: 0, text_layers: 0, smart_objects: 0, user_masks: 0, vector_masks: 0, adjustment_layers: 0 };
    function auditKey(name) { return stringIDToTypeID(name); }
    function auditBoolean(descriptor, name) {
        var key = auditKey(name);
        return descriptor.hasKey(key) ? descriptor.getBoolean(key) : null;
    }
    function auditKeys(descriptor) {
        var names = [], i, key, name;
        for (i = 0; i < descriptor.count; i++) {
            key = descriptor.getKey(i);
            try { name = typeIDToStringID(key); } catch (ignoredStringKey) { name = ''; }
            if (!name) { try { name = typeIDToCharID(key); } catch (ignoredCharKey) { name = String(key); } }
            names.push(name);
        }
        return names;
    }
    function auditBounds(layer) {
        var b = layer.bounds;
        return { left: b[0].as('px'), top: b[1].as('px'), right: b[2].as('px'), bottom: b[3].as('px') };
    }
    function auditTree(container, parents) {
        var rows = [], i, layer, row, ref, descriptor, key, info;
        for (i = 0; i < container.layers.length; i++) {
            layer = container.layers[i];
            auditSummary.layers++;
            row = { id: layer.id, name: layer.name, type: layer.typename, parent_path: parents.slice(0), visible: layer.visible, opacity: layer.opacity, bounds_px: auditBounds(layer) };
            if (layer.typename === 'LayerSet') { row.kind = 'GROUP'; auditSummary.groups++; }
            else { row.kind = String(layer.kind); }
            ref = new ActionReference();
            ref.putIdentifier(charIDToTypeID('Lyr '), layer.id);
            descriptor = executeActionGet(ref);
            row.user_mask = auditBoolean(descriptor, 'hasUserMask');
            row.user_mask_enabled = auditBoolean(descriptor, 'userMaskEnabled');
            row.vector_mask = auditBoolean(descriptor, 'hasVectorMask');
            row.vector_mask_enabled = auditBoolean(descriptor, 'vectorMaskEnabled');
            if (row.user_mask === true) { auditSummary.user_masks++; }
            if (row.vector_mask === true) { auditSummary.vector_masks++; }
            try { row.clipped_to_below = layer.grouped; } catch (ignoredGrouped) { row.clipped_to_below = null; }
            if (layer.typename === 'ArtLayer' && layer.kind === LayerKind.TEXT) {
                auditSummary.text_layers++;
                row.text = { contents: layer.textItem.contents, font: layer.textItem.font, size_pt: layer.textItem.size.as('pt'), kind: String(layer.textItem.kind) };
                try { row.text.position_px = [layer.textItem.position[0].as('px'), layer.textItem.position[1].as('px')]; } catch (ignoredTextPosition) {}
            }
            key = auditKey('smartObject');
            if (descriptor.hasKey(key)) {
                auditSummary.smart_objects++;
                info = descriptor.getObjectValue(key);
                row.smart_object = { descriptor_keys: auditKeys(info), linked: auditBoolean(info, 'linked') };
                key = auditKey('fileReference');
                if (info.hasKey(key)) { try { row.smart_object.file_reference = info.getString(key); } catch (ignoredReference) {} }
                key = auditKey('link');
                if (info.hasKey(key)) { try { row.smart_object.link_path = info.getPath(key).fsName; } catch (ignoredLink) {} }
                key = auditKey('smartObjectMore');
                if (descriptor.hasKey(key)) {
                    info = descriptor.getObjectValue(key);
                    row.smart_object.more_descriptor_keys = auditKeys(info);
                    key = auditKey('filterFX');
                    if (info.hasKey(key)) { try { row.smart_object.smart_filter_count = info.getList(key).count; } catch (ignoredFilters) {} }
                }
            }
            key = auditKey('adjustment');
            if (descriptor.hasKey(key)) {
                row.has_adjustment_descriptor = true;
                // Fill layers also have an adjustment descriptor; do not count them as tonal adjustments.
                if (row.kind.indexOf('SOLIDFILL') < 0 && row.kind.indexOf('GRADIENTFILL') < 0 && row.kind.indexOf('PATTERNFILL') < 0) { auditSummary.adjustment_layers++; }
            }
            if (layer.typename === 'LayerSet') { row.children = auditTree(layer, parents.concat([layer.name])); }
            rows.push(row);
        }
        return rows;
    }
    var auditResult = { ok: true, document_id: auditDoc.id, name: auditDoc.name, width_px: auditDoc.width.as('px'), height_px: auditDoc.height.as('px'), resolution_ppi: auditDoc.resolution, mode: String(auditDoc.mode), bits_per_channel: String(auditDoc.bitsPerChannel), saved: auditDoc.saved, active_layer_id: auditDoc.activeLayer.id };
    try { auditResult.profile = auditDoc.colorProfileName; } catch (ignoredProfile) { auditResult.profile = null; }
    try { auditResult.path = auditDoc.fullName.fsName; } catch (ignoredUnsavedPath) { auditResult.path = null; }
    auditResult.layers = auditTree(auditDoc, []);
    auditResult.summary = auditSummary;
    auditResult.limits = 'Structure inspection does not verify aesthetics, text overflow, mask quality, or Smart Object contents.';
    return auditResult;
} catch (auditError) {
    return { ok: false, code: 'audit_failed', document_id: SCUFITA_DOCUMENT_ID, message: String(auditError) };
}
