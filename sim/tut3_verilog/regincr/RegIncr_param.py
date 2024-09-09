#=========================================================================
# RegIncrNstage
#=========================================================================
# Registered incrementer that is parameterized by the number of stages.

from pymtl3 import *
from pymtl3.passes.backends.verilog import *


class RegIncr_param( VerilogPlaceholder, Component ):
  def construct( s, p_nstages=2 , p_bitwidths=8):
    s.in_ = InPort ( p_bitwidths )
    s.out = OutPort( p_bitwidths )