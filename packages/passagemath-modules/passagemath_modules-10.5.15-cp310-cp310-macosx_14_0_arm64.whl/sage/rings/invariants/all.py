# sage_setup: distribution = sagemath-modules
from sage.misc.lazy_import import lazy_import
lazy_import('sage.rings.invariants.invariant_theory', 'invariant_theory')
del lazy_import
