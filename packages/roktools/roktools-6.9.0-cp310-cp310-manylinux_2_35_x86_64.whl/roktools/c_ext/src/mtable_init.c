#include <Python.h>

#include "foo.h"
#include "hatanaka.h"

static PyMethodDef module_methods[] = {
    { "foo",         (PyCFunction)foo, METH_VARARGS | METH_KEYWORDS,
      "Conversion from lon/lat/height to Cartesian (XYZ)\n\n"
      ":param v1: Value 1\n"
      ":param v2: Value 2\n"
      ":param v3: Value 3\n"
      ":param v4: Value 4\n"
      ":param v5: Value 5\n\n"
      ":return: Array with the input\n\n"
      "Example:\n\n"
      ">>> foo(0.0, 1.0, 2.0, 3.0, 4.0)\n"
      "[0.0, 1.0, 2.0, 3.0, 4.0]\n" },
    { "read_crx",         (PyCFunction)read_crx, METH_VARARGS | METH_KEYWORDS,
      "Read a Hatanaka (gzip uncompressed) file and generate a numpy array\n\n"
      ":param filename: Name of the Hatanaka file to process\n"
      ":return: Numpy array\n\n"},
      {NULL, NULL, 0, NULL},  /* Sentinel */
};

/*----------------------------------------------------------------------------*/

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "c_ext", /* name of the module*/
    "C extension methods",
    -1,  // size of per-interpreter state of the module,
         // or -1 if the module keeps state in global variables.
    module_methods
};


PyMODINIT_FUNC PyInit_c_ext(void) {

    PyObject* m = NULL;

//     // Classes
//     if (PyType_Ready(HatanakaReaderType) < 0) {
//         goto end;
//     }

    m = PyModule_Create(&module);
    if (m == NULL) {
        goto end;
    }

//     Py_INCREF(HatanakaReaderType);
//     PyModule_AddObject(m, "HatanakaReader", (PyObject*)HatanakaReaderType);

end:
    return m;
}
