#=========================================================================
# Regincr3stage_test
#=========================================================================
from pymtl3 import *
from pymtl3.stdlib.test_utils import run_test_vector_sim
from ..RegIncr3stage import RegIncr3stage

#-------------------------------------------------------------------------
# test_small
#-------------------------------------------------------------------------

def test_small( cmdline_opts ):
  run_test_vector_sim( RegIncr3stage(), [
    ('in_   out*'),
    [ 0x00, '?'  ],
    [ 0x03, '?'  ],
    [ 0x06, '?'  ],
    [ 0x00, 0x03 ],
    [ 0x00, 0x06 ],
    [ 0x00, 0x09 ],
  ], cmdline_opts )

#-------------------------------------------------------------------------
# test_large
#-------------------------------------------------------------------------

def test_large( cmdline_opts ):
  run_test_vector_sim( RegIncr3stage(), [
    ('in_   out*'),
    [ 0xa0, '?'  ],
    [ 0xb3, '?'  ],
    [ 0xc6, '?'  ],
    [ 0x00, 0xa3 ],
    [ 0x00, 0xb6 ],
    [ 0x00, 0xc9 ],
  ], cmdline_opts )

#-------------------------------------------------------------------------
# test_overflow
#-------------------------------------------------------------------------

def test_overflow( cmdline_opts ):
  run_test_vector_sim( RegIncr3stage(), [
    ('in_   out*'),
    [ 0x00, '?'  ],
    [ 0xfe, '?'  ],
    [ 0xff, '?'  ],
    [ 0x00, 0x03 ],
    [ 0x00, 0x01 ],
    [ 0x00, 0x02 ],
  ], cmdline_opts )

#-------------------------------------------------------------------------
# test_random
#-------------------------------------------------------------------------

import random

def test_random( cmdline_opts ):

  test_vector_table = [( 'in_', 'out*' )]
  last_result_0 = '?'
  last_result_1 = '?'
  last_result_2 = '?'
  for i in range(20):
    rand_value = Bits8( random.randint(0,0xff) )
    test_vector_table.append( [ rand_value, last_result_0 ] )
    last_result_0 = Bits8( rand_value + 3, trunc_int=True )

    rand_value = Bits8( random.randint(0,0xff) )
    test_vector_table.append( [ rand_value, last_result_1 ] )
    last_result_1 = Bits8( rand_value + 3, trunc_int=True )

    rand_value = Bits8( random.randint(0,0xff) )
    test_vector_table.append( [ rand_value, last_result_2 ] )
    last_result_2 = Bits8( rand_value + 3, trunc_int=True )

  run_test_vector_sim( RegIncr3stage(), test_vector_table, cmdline_opts )
