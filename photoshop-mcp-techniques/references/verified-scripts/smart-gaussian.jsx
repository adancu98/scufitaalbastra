// Pin document_id and inspect the intended layer before execution.
// Example radius only; adapt it to the image and requested result.
var radiusPx = 5;
if (app.activeDocument.activeLayer.kind !== LayerKind.SMARTOBJECT) {
    throw new Error('Expected an existing Smart Object; do not rasterize to continue.');
}
var blurDescriptor = new ActionDescriptor();
blurDescriptor.putUnitDouble(charIDToTypeID('Rds '), charIDToTypeID('#Pxl'), radiusPx);
executeAction(charIDToTypeID('GsnB'), blurDescriptor, DialogModes.NO);
var layerReference = new ActionReference();
layerReference.putEnumerated(charIDToTypeID('Lyr '), charIDToTypeID('Ordn'), charIDToTypeID('Trgt'));
var layerDescriptor = executeActionGet(layerReference);
var objectInfo = layerDescriptor.getObjectValue(stringIDToTypeID('smartObjectMore'));
var filters = objectInfo.getList(stringIDToTypeID('filterFX'));
return 'kind=' + app.activeDocument.activeLayer.kind + ';smart_filter_count=' + filters.count;
