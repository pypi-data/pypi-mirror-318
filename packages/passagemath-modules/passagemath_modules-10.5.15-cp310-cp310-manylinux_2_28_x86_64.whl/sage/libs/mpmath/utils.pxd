# sage_setup: distribution = sagemath-modules
from sage.libs.mpfr.types cimport mpfr_t

cdef mpfr_to_mpfval(mpfr_t)
