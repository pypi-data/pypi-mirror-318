# sage_setup: distribution = sagemath-modules
# Automatically generated by /private/var/folders/9f/9p4dh6hs5yddrk7drxq8rc_80000gn/T/build-env-uux__2yw/lib/python3.10/site-packages/sage_setup/autogen/interpreters/internal/generator.py.  Do not edit!
cdef public bint rr_py_call_helper(object domain, object fn,
                                   int n_args,
                                   mpfr_t* args, mpfr_t retval) except 0:
    py_args = []
    cdef int i
    cdef RealNumber rn
    for i from 0 <= i < n_args:
        rn = domain()
        mpfr_set(rn.value, args[i], MPFR_RNDN)
        py_args.append(rn)
    cdef RealNumber result = domain(fn(*py_args))
    mpfr_set(retval, result.value, MPFR_RNDN)
    return 1



from cpython.ref cimport PyObject
cdef extern from "Python.h":
    void Py_DECREF(PyObject *o)
    void Py_INCREF(PyObject *o)
    void Py_CLEAR(PyObject *o)

    object PyList_New(Py_ssize_t len)
    ctypedef struct PyListObject:
        PyObject **ob_item

    ctypedef struct PyTupleObject:
        PyObject **ob_item

from cysignals.memory cimport check_allocarray, sig_free

from sage.ext.fast_callable cimport Wrapper

cdef extern from "interp_rr.c":
    bint interp_rr(mpfr_t* args,
        mpfr_t retval,
        mpfr_t* constants,
        PyObject** py_constants,
        mpfr_t* stack,
        int* code,
        PyObject* domain) except? 0

cdef class Wrapper_rr(Wrapper):
    # attributes are declared in corresponding .pxd file

    def __init__(self, args):
        Wrapper.__init__(self, args, metadata)
        cdef int i
        cdef int count
        cdef RealNumber rn
        self.domain = args['domain']
        count = args['args']
        self._n_args = count
        self._args = <mpfr_t*>check_allocarray(self._n_args, sizeof(mpfr_t))
        for i in range(count):
            mpfr_init2(self._args[i], self.domain.prec())
        val = args['constants']
        self._n_constants = len(val)
        self._constants = <mpfr_t*>check_allocarray(self._n_constants, sizeof(mpfr_t))
        for i in range(len(val)):
            mpfr_init2(self._constants[i], self.domain.prec())
        for i in range(len(val)):
            rn = self.domain(val[i])
            mpfr_set(self._constants[i], rn.value, MPFR_RNDN)
        val = args['py_constants']
        self._n_py_constants = len(val)
        self._list_py_constants = PyList_New(self._n_py_constants)
        self._py_constants = (<PyListObject *>self._list_py_constants).ob_item
        for i in range(len(val)):
            self._py_constants[i] = <PyObject *>val[i]; Py_INCREF(self._py_constants[i])
        count = args['stack']
        self._n_stack = count
        self._stack = <mpfr_t*>check_allocarray(self._n_stack, sizeof(mpfr_t))
        for i in range(count):
            mpfr_init2(self._stack[i], self.domain.prec())
        val = args['code']
        self._n_code = len(val)
        self._code = <int*>check_allocarray(self._n_code, sizeof(int))
        for i in range(len(val)):
            self._code[i] = val[i]
        self._domain = args['domain']

    def __dealloc__(self):
        cdef int i
        if self._args:
            for i in range(self._n_args):
                mpfr_clear(self._args[i])
            sig_free(self._args)
        if self._constants:
            for i in range(self._n_constants):
                mpfr_clear(self._constants[i])
            sig_free(self._constants)
        if self._stack:
            for i in range(self._n_stack):
                mpfr_clear(self._stack[i])
            sig_free(self._stack)
        if self._code:
            sig_free(self._code)

    def __call__(self, *args):
        if self._n_args != len(args): raise ValueError
        cdef RealNumber rn
        cdef mpfr_t* c_args = self._args
        cdef int i
        for i from 0 <= i < len(args):
            rn = self.domain(args[i])
            mpfr_set(self._args[i], rn.value, MPFR_RNDN)
        cdef RealNumber retval = (self.domain)()
        interp_rr(c_args
            , retval.value
            , self._constants
            , self._py_constants
            , self._stack
            , self._code
            , <PyObject*>self._domain
            )
        return retval

    cdef bint call_c(self,
                     mpfr_t* args,
                     mpfr_t result) except 0:
        interp_rr(args
            , result
            , self._constants
            , self._py_constants
            , self._stack
            , self._code
            , <PyObject*>self._domain
            )

        return 1

from sage.ext.fast_callable import CompilerInstrSpec, InterpreterMetadata
metadata = InterpreterMetadata(by_opname={
  'load_arg':
  (CompilerInstrSpec(0, 1, ['args']), 0),
  'load_const':
  (CompilerInstrSpec(0, 1, ['constants']), 1),
  'return':
  (CompilerInstrSpec(1, 0, []), 2),
  'py_call':
  (CompilerInstrSpec(0, 1, ['py_constants', 'n_inputs']), 3),
  'add':
  (CompilerInstrSpec(2, 1, []), 4),
  'sub':
  (CompilerInstrSpec(2, 1, []), 5),
  'mul':
  (CompilerInstrSpec(2, 1, []), 6),
  'div':
  (CompilerInstrSpec(2, 1, []), 7),
  'pow':
  (CompilerInstrSpec(2, 1, []), 8),
  'ipow':
  (CompilerInstrSpec(1, 1, ['code']), 9),
  'neg':
  (CompilerInstrSpec(1, 1, []), 10),
  'abs':
  (CompilerInstrSpec(1, 1, []), 11),
  'log':
  (CompilerInstrSpec(1, 1, []), 12),
  'log2':
  (CompilerInstrSpec(1, 1, []), 13),
  'log10':
  (CompilerInstrSpec(1, 1, []), 14),
  'exp':
  (CompilerInstrSpec(1, 1, []), 15),
  'exp2':
  (CompilerInstrSpec(1, 1, []), 16),
  'exp10':
  (CompilerInstrSpec(1, 1, []), 17),
  'cos':
  (CompilerInstrSpec(1, 1, []), 18),
  'sin':
  (CompilerInstrSpec(1, 1, []), 19),
  'tan':
  (CompilerInstrSpec(1, 1, []), 20),
  'sec':
  (CompilerInstrSpec(1, 1, []), 21),
  'csc':
  (CompilerInstrSpec(1, 1, []), 22),
  'cot':
  (CompilerInstrSpec(1, 1, []), 23),
  'acos':
  (CompilerInstrSpec(1, 1, []), 24),
  'asin':
  (CompilerInstrSpec(1, 1, []), 25),
  'atan':
  (CompilerInstrSpec(1, 1, []), 26),
  'cosh':
  (CompilerInstrSpec(1, 1, []), 27),
  'sinh':
  (CompilerInstrSpec(1, 1, []), 28),
  'tanh':
  (CompilerInstrSpec(1, 1, []), 29),
  'sech':
  (CompilerInstrSpec(1, 1, []), 30),
  'csch':
  (CompilerInstrSpec(1, 1, []), 31),
  'coth':
  (CompilerInstrSpec(1, 1, []), 32),
  'acosh':
  (CompilerInstrSpec(1, 1, []), 33),
  'asinh':
  (CompilerInstrSpec(1, 1, []), 34),
  'atanh':
  (CompilerInstrSpec(1, 1, []), 35),
  'log1p':
  (CompilerInstrSpec(1, 1, []), 36),
  'expm1':
  (CompilerInstrSpec(1, 1, []), 37),
  'eint':
  (CompilerInstrSpec(1, 1, []), 38),
  'gamma':
  (CompilerInstrSpec(1, 1, []), 39),
  'lngamma':
  (CompilerInstrSpec(1, 1, []), 40),
  'zeta':
  (CompilerInstrSpec(1, 1, []), 41),
  'erf':
  (CompilerInstrSpec(1, 1, []), 42),
  'erfc':
  (CompilerInstrSpec(1, 1, []), 43),
  'j0':
  (CompilerInstrSpec(1, 1, []), 44),
  'j1':
  (CompilerInstrSpec(1, 1, []), 45),
  'y0':
  (CompilerInstrSpec(1, 1, []), 46),
  'y1':
  (CompilerInstrSpec(1, 1, []), 47),
  'invert':
  (CompilerInstrSpec(1, 1, []), 48),
 },
 by_opcode=[
  ('load_arg',
   CompilerInstrSpec(0, 1, ['args'])),
  ('load_const',
   CompilerInstrSpec(0, 1, ['constants'])),
  ('return',
   CompilerInstrSpec(1, 0, [])),
  ('py_call',
   CompilerInstrSpec(0, 1, ['py_constants', 'n_inputs'])),
  ('add',
   CompilerInstrSpec(2, 1, [])),
  ('sub',
   CompilerInstrSpec(2, 1, [])),
  ('mul',
   CompilerInstrSpec(2, 1, [])),
  ('div',
   CompilerInstrSpec(2, 1, [])),
  ('pow',
   CompilerInstrSpec(2, 1, [])),
  ('ipow',
   CompilerInstrSpec(1, 1, ['code'])),
  ('neg',
   CompilerInstrSpec(1, 1, [])),
  ('abs',
   CompilerInstrSpec(1, 1, [])),
  ('log',
   CompilerInstrSpec(1, 1, [])),
  ('log2',
   CompilerInstrSpec(1, 1, [])),
  ('log10',
   CompilerInstrSpec(1, 1, [])),
  ('exp',
   CompilerInstrSpec(1, 1, [])),
  ('exp2',
   CompilerInstrSpec(1, 1, [])),
  ('exp10',
   CompilerInstrSpec(1, 1, [])),
  ('cos',
   CompilerInstrSpec(1, 1, [])),
  ('sin',
   CompilerInstrSpec(1, 1, [])),
  ('tan',
   CompilerInstrSpec(1, 1, [])),
  ('sec',
   CompilerInstrSpec(1, 1, [])),
  ('csc',
   CompilerInstrSpec(1, 1, [])),
  ('cot',
   CompilerInstrSpec(1, 1, [])),
  ('acos',
   CompilerInstrSpec(1, 1, [])),
  ('asin',
   CompilerInstrSpec(1, 1, [])),
  ('atan',
   CompilerInstrSpec(1, 1, [])),
  ('cosh',
   CompilerInstrSpec(1, 1, [])),
  ('sinh',
   CompilerInstrSpec(1, 1, [])),
  ('tanh',
   CompilerInstrSpec(1, 1, [])),
  ('sech',
   CompilerInstrSpec(1, 1, [])),
  ('csch',
   CompilerInstrSpec(1, 1, [])),
  ('coth',
   CompilerInstrSpec(1, 1, [])),
  ('acosh',
   CompilerInstrSpec(1, 1, [])),
  ('asinh',
   CompilerInstrSpec(1, 1, [])),
  ('atanh',
   CompilerInstrSpec(1, 1, [])),
  ('log1p',
   CompilerInstrSpec(1, 1, [])),
  ('expm1',
   CompilerInstrSpec(1, 1, [])),
  ('eint',
   CompilerInstrSpec(1, 1, [])),
  ('gamma',
   CompilerInstrSpec(1, 1, [])),
  ('lngamma',
   CompilerInstrSpec(1, 1, [])),
  ('zeta',
   CompilerInstrSpec(1, 1, [])),
  ('erf',
   CompilerInstrSpec(1, 1, [])),
  ('erfc',
   CompilerInstrSpec(1, 1, [])),
  ('j0',
   CompilerInstrSpec(1, 1, [])),
  ('j1',
   CompilerInstrSpec(1, 1, [])),
  ('y0',
   CompilerInstrSpec(1, 1, [])),
  ('y1',
   CompilerInstrSpec(1, 1, [])),
  ('invert',
   CompilerInstrSpec(1, 1, [])),
 ],
 ipow_range=(-2147483648, 2147483647))
