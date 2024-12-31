#include <pybind11/pybind11.h>
#include <iostream>

using namespace std;

int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(KIG2013_G9_cpptopython, m) {
    m.doc() = R"pbdoc(
        A demonstration of using C++ code
        in Python by packaging the former
        in a Python package using pybind11.

        ----------------------------------

        For use of:
        KIG2013 Programming Assignment

        ----------------------------------

        By:
        23006148/1 Kwong Ye Kun G9
    )pbdoc";

    m.def("add", &add, "A function which adds two numbers.");
}