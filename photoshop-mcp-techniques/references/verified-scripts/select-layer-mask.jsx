// Pin document_id on photoshop_execute_script before executing this snippet.
// Tested on an existing raster-layer mask in Photoshop27.11.0.
// This selects the mask channel only; it does not preserve/multiply old mask values.
var maskReference = new ActionReference();
maskReference.putEnumerated(charIDToTypeID('Chnl'), charIDToTypeID('Chnl'), charIDToTypeID('Msk '));
var maskDescriptor = new ActionDescriptor();
maskDescriptor.putReference(charIDToTypeID('null'), maskReference);
maskDescriptor.putBoolean(charIDToTypeID('MkVs'), false);
executeAction(charIDToTypeID('slct'), maskDescriptor, DialogModes.NO);
return 'Explicit mask channel selected';
