from libc.math cimport sin

cdef double c_sin(double x):
     return sin(x)

def get_c_sin(x):
    return c_sin(x)

