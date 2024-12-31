#include <pybind11/pybind11.h>
#include <iostream>

using namespace std;

int add(int i, int j) {
    return i + j;
}

int subtract(int i, int j) {
    return i - j;
}

int multiply(int i, int j) {
    return i * j;
}

double divide(int i, int j) {
    return i / j;
}

double arr[10];
int isnum[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int i = 0;

void arrinput(double num) {
    if (isnum[i] == 0) {
        isnum[i] = 1;
        arr[i] = num;
        i += 1;
    } else {
        cout << "No space left in input array!";
    }
}

void arrdelete() {
    if (isnum[i - 1] == 1) {
        isnum[i - 1] = 0;
        arr[i - 1] = 0;
        i -= 1;
    } else {
        cout << "Array is already empty!";
    }
}

double getvalue(int index) {
    return arr[index];
}

PYBIND11_MODULE(python_example_wierdre, m) {
    m.doc() = R"pbdoc(
        Pybind11 example plugin by Wierdre
        ----------------------------------

        .. currentmodule:: python_example_wierdre

        .. autosummary::
           :toctree: _generate

           add
           subtract
    )pbdoc";

    m.def("add", &add, "add function");
    m.def("subtract", &subtract, "subtract function");
    m.def("multiply", &multiply, "multiply function");
    m.def("divide", &divide, "divide function");
}