PyObject *xmlsec_TmplSignatureCreate(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplSignatureEnsureKeyInfo(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplSignatureAddReference(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplSignatureAddObject(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplSignatureGetSignMethodNode(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplSignatureGetC14NMethodNode(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplReferenceAddTransform(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplObjectAddSignProperties(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplObjectAddManifest(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplManifestAddReference(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplEncDataCreate (PyObject *self, PyObject *args);
PyObject *xmlsec_TmplEncDataEnsureKeyInfo(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplEncDataEnsureEncProperties(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplEncDataAddEncProperty(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplEncDataEnsureCipherValue(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplEncDataEnsureCipherReference(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplEncDataGetEncMethodNode(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplCipherReferenceAddTransform(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplReferenceListAddDataReference(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplReferenceListAddKeyReference(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplKeyInfoAddKeyName(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplKeyInfoAddKeyValue(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplKeyInfoAddX509Data(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplKeyInfoAddRetrievalMethod(PyObject *self, PyObject *args); //New
PyObject *xmlsec_TmplRetrievalMethodAddTransform(PyObject *self, PyObject *args); //New
PyObject *xmlsec_TmplKeyInfoAddEncryptedKey(PyObject *self, PyObject *args);
PyObject *xmlsec_TmplTransformAddHmacOutputLength(PyObject *self, PyObject *args); //New
PyObject *xmlsec_TmplTransformAddRsaOaepParam(PyObject *self, PyObject *args); //New
PyObject *xmlsec_TmplTransformAddXsltStylesheet(PyObject *self, PyObject *args); //New
PyObject *xmlsec_TmplTransformAddC14NInclNamespaces(PyObject *self, PyObject *args); //New
PyObject *xmlsec_TmplTransformAddXPath(PyObject *self, PyObject *args); //New
PyObject *xmlsec_TmplTransformAddXPath2(PyObject *self, PyObject *args); //New
PyObject *xmlsec_TmplTransformAddXPointer(PyObject *self, PyObject *args); //New
