# sage_setup: distribution = sagemath-modules
# Automatically generated by /tmp/build-env-2d6tbj2v/lib/python3.10/site-packages/sage_setup/autogen/interpreters/internal/generator.py.  Do not edit!

from cpython.ref cimport PyObject

from sage.ext.fast_callable cimport Wrapper

from sage.rings.real_mpfr cimport RealNumber
from sage.libs.mpfr cimport *
from sage.rings.complex_mpfr cimport ComplexNumber
from sage.libs.mpc cimport *

cdef class Wrapper_cc(Wrapper):
    cdef object domain
    cdef ComplexNumber domain_element
    cdef int _n_args
    cdef mpc_t* _args
    cdef int _n_constants
    cdef mpc_t* _constants
    cdef object _list_py_constants
    cdef int _n_py_constants
    cdef PyObject** _py_constants
    cdef int _n_stack
    cdef mpc_t* _stack
    cdef int _n_code
    cdef int* _code
    cdef object _domain
    cdef bint call_c(self,
                     mpc_t* args,
                     mpc_t result) except 0
