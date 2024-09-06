#=========================================================================
# regincr-adhoc-test <input-values>
#=========================================================================
# Note that you can turn on line tracing, text waveforms, and VCD
# waveforms by adding these options to the DefaultPassGroup.
#
#  model.apply( DefaultPassGroup(linetrace=True,textwave=True,vcdwave="regincr-adhoc-test.vcd") )
#
# You will also need to add this to the very end of the script:
#
#  model.print_textwave()
#

from pymtl3  import *
from pymtl3.passes.backends.verilog import *
import random

from sys     import argv
from RegIncr import RegIncr

# Get list of input values from command line
sequence = list(range(1, 21, 2))  # Generates [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Shuffle the sequence randomly
# random.shuffle(sequence)
input_values = [ sequence.pop(0) for _ in range(10) ]

# Add three zero values to end of list of input values

input_values.extend( [0]*3 )

# ''' TUTORIAL TASK ''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This simulator script is incomplete. As part of the tutorial you will
# insert code here for constructing and elaborating a RegIncr model.
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
model = RegIncr()
model.elaborate()
# Apply the Verilog import passes and the default pass group

model.apply( VerilogPlaceholderPass() )
model = VerilogTranslationImportPass()( model )
model.apply( DefaultPassGroup(linetrace=True) )

# Reset simulator

model.sim_reset()

# Apply input values and display output values

for input_value in input_values:

  # Write input value to input port

  model.in_ @= input_value
  model.sim_eval_combinational()

  # Print input and output ports


  # Tick simulator one cycle

  model.sim_tick()

