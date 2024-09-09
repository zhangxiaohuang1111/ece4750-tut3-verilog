#=========================================================================
# RegIncr_param
#=========================================================================
# Registered incrementer that is parameterized by the number of stages.

from pymtl3 import *
from pymtl3.passes.backends.verilog import *

class RegIncr_param( VerilogPlaceholder, Component ):
  def construct( s, p_nstages=2, p_nbits=8 ):
    s.in_ = InPort ( p_nbits )
    s.out = OutPort( p_nbits )


