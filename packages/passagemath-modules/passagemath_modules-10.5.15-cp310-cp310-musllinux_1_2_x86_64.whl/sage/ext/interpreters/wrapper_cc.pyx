# sage_setup: distribution = sagemath-modules
# Automatically generated by /tmp/build-env-2d6tbj2v/lib/python3.10/site-packages/sage_setup/autogen/interpreters/internal/generator.py.  Do not edit!
# distutils: libraries = mpfr mpc gmp

cdef public bint cc_py_call_helper(object domain, object fn,
                                   int n_args,
                                   mpc_t* args, mpc_t retval) except 0:
    py_args = []
    cdef int i
    cdef ComplexNumber ZERO=domain.zero()
    cdef ComplexNumber cn
    for i from 0 <= i < n_args:
        cn = ZERO._new()
        mpfr_set(cn.__re, mpc_realref(args[i]), MPFR_RNDN)
        mpfr_set(cn.__im, mpc_imagref(args[i]), MPFR_RNDN)
        py_args.append(cn)
    cdef ComplexNumber result = domain(fn(*py_args))
    mpc_set_fr_fr(retval, result.__re,result.__im, MPC_RNDNN)
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

cdef extern from "interp_cc.c":
    bint interp_cc(mpc_t* args,
        mpc_t retval,
        mpc_t* constants,
        PyObject** py_constants,
        mpc_t* stack,
        int* code,
        PyObject* domain) except? 0

cdef class Wrapper_cc(Wrapper):
    # attributes are declared in corresponding .pxd file

    def __init__(self, args):
        Wrapper.__init__(self, args, metadata)
        cdef int i
        cdef int count
        cdef ComplexNumber cn
        self.domain = args['domain']
        self.domain_element = self.domain.zero()
        count = args['args']
        self._n_args = count
        self._args = <mpc_t*>check_allocarray(self._n_args, sizeof(mpc_t))
        for i in range(count):
            mpc_init2(self._args[i], self.domain_element._prec)
        val = args['constants']
        self._n_constants = len(val)
        self._constants = <mpc_t*>check_allocarray(self._n_constants, sizeof(mpc_t))
        for i in range(len(val)):
            mpc_init2(self._constants[i], self.domain_element._prec)
        for i in range(len(val)):
            cn = self.domain(val[i])
            mpc_set_fr_fr(self._constants[i], cn.__re, cn.__im, MPC_RNDNN)
        val = args['py_constants']
        self._n_py_constants = len(val)
        self._list_py_constants = PyList_New(self._n_py_constants)
        self._py_constants = (<PyListObject *>self._list_py_constants).ob_item
        for i in range(len(val)):
            self._py_constants[i] = <PyObject *>val[i]; Py_INCREF(self._py_constants[i])
        count = args['stack']
        self._n_stack = count
        self._stack = <mpc_t*>check_allocarray(self._n_stack, sizeof(mpc_t))
        for i in range(count):
            mpc_init2(self._stack[i], self.domain_element._prec)
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
                mpc_clear(self._args[i])
            sig_free(self._args)
        if self._constants:
            for i in range(self._n_constants):
                mpc_clear(self._constants[i])
            sig_free(self._constants)
        if self._stack:
            for i in range(self._n_stack):
                mpc_clear(self._stack[i])
            sig_free(self._stack)
        if self._code:
            sig_free(self._code)

    def __call__(self, *args):
        if self._n_args != len(args): raise ValueError
        cdef ComplexNumber cn
        cdef mpc_t* c_args = self._args
        cdef int i
        for i from 0 <= i < len(args):
            cn = self.domain(args[i])
            mpc_set_fr_fr(self._args[i], cn.__re, cn.__im, MPC_RNDNN)
        cdef ComplexNumber retval = (self.domain_element._new())
        interp_cc(c_args
            , (<mpc_t>(retval.__re))
            , self._constants
            , self._py_constants
            , self._stack
            , self._code
            , <PyObject*>self._domain
            )
        return retval

    cdef bint call_c(self,
                     mpc_t* args,
                     mpc_t result) except 0:
        interp_cc(args
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
  'log':
  (CompilerInstrSpec(1, 1, []), 11),
  'log10':
  (CompilerInstrSpec(1, 1, []), 12),
  'exp':
  (CompilerInstrSpec(1, 1, []), 13),
  'cos':
  (CompilerInstrSpec(1, 1, []), 14),
  'sin':
  (CompilerInstrSpec(1, 1, []), 15),
  'tan':
  (CompilerInstrSpec(1, 1, []), 16),
  'acos':
  (CompilerInstrSpec(1, 1, []), 17),
  'asin':
  (CompilerInstrSpec(1, 1, []), 18),
  'atan':
  (CompilerInstrSpec(1, 1, []), 19),
  'cosh':
  (CompilerInstrSpec(1, 1, []), 20),
  'sinh':
  (CompilerInstrSpec(1, 1, []), 21),
  'tanh':
  (CompilerInstrSpec(1, 1, []), 22),
  'acosh':
  (CompilerInstrSpec(1, 1, []), 23),
  'asinh':
  (CompilerInstrSpec(1, 1, []), 24),
  'atanh':
  (CompilerInstrSpec(1, 1, []), 25),
  'invert':
  (CompilerInstrSpec(1, 1, []), 26),
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
  ('log',
   CompilerInstrSpec(1, 1, [])),
  ('log10',
   CompilerInstrSpec(1, 1, [])),
  ('exp',
   CompilerInstrSpec(1, 1, [])),
  ('cos',
   CompilerInstrSpec(1, 1, [])),
  ('sin',
   CompilerInstrSpec(1, 1, [])),
  ('tan',
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
  ('acosh',
   CompilerInstrSpec(1, 1, [])),
  ('asinh',
   CompilerInstrSpec(1, 1, [])),
  ('atanh',
   CompilerInstrSpec(1, 1, [])),
  ('invert',
   CompilerInstrSpec(1, 1, [])),
 ],
 ipow_range=(-2147483648, 2147483647))
