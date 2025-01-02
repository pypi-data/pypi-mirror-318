#include <Python.h>

#include "../include/helpers.h"

#include "foo.h"

PyObject *foo(PyObject* self, PyObject* args, PyObject* kwargs) {

    static char* arguments[6] = { "" /* lon */, "" /* lat */, "" /*hgt*/, "a", "e", NULL };
    PyObject* out = NULL;

    /* parse arguments */
    double values[5];

    if ( !PyArg_ParseTupleAndKeywords(args, kwargs, "ddd|dd", arguments, &values[0], &values[1], &values[2], &values[3], &values[4]) ) {
        goto end;
    }

    out = convert_to_pylist(values, 5);

end:
    return out;
}
