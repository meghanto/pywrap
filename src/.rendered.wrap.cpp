


#include <pybind11/pybind11.h>
#include "funcs.hpp"

namespace py = pybind11;

using namespace pybind11::literals;

PYBIND11_MODULE(wrap,m) {
    m.doc() = "Doc string for module!"; // optional
    m.def("add", &add, "A function which adds two integers");
}
