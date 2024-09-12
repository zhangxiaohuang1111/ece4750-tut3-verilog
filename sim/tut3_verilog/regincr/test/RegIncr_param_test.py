#=========================================================================
# Regincr_param_test
#=========================================================================

import collections
import pytest
from pymtl3 import mk_bits

from random import sample, seed

from pymtl3 import *
from pymtl3.stdlib.test_utils import run_test_vector_sim, mk_test_case_table
from ..RegIncr_param import RegIncr_param

# To ensure reproducible testing

seed(0xdeadbeef)

#-------------------------------------------------------------------------
# mk_test_vector_table
#-------------------------------------------------------------------------

def mk_test_vector_table( nstages, inputs, bitwidth ):
  inputs = [min(input_, (1 << bitwidth) - 1) for input_ in inputs]
  inputs.extend( [0]*nstages )

  test_vector_table = [ ('in_ out*') ]
  last_results = collections.deque( ['?']*nstages )
  BitsN = mk_bits(bitwidth)
  for input_ in inputs:
    test_vector_table.append( [ input_, last_results.popleft() ] )
    last_results.append(BitsN( input_ + nstages, trunc_int=True ) )
  return test_vector_table

#-------------------------------------------------------------------------
# Parameterized Testing with Test Case Table
#-------------------------------------------------------------------------

test_case_table = mk_test_case_table([
  (                    "nstages inputs bitwidth           "),
  [ "2stage_small",    2,       [ 0x00, 0x03, 0x06 ]   ,  9],
  [ "2stage_large",    2,       [ 0xa0, 0xb3, 0xc6 ]   ,  9],
  [ "2stage_overflow", 2,       [ 0x00, 0xfe, 0xff ]   ,  9],
  [ "2stage_random",   2,       sample(range(0xff),20) ,  9],
  [ "3stage_small",    3,       [ 0x00, 0x03, 0x06 ]   ,  9],
  [ "3stage_large",    3,       [ 0xa0, 0xb3, 0xc6 ]   ,  9],
  [ "3stage_overflow", 3,       [ 0x00, 0xfe, 0xff ]   ,  9],
  [ "3stage_random",   3,       sample(range(0xff),20) ,  9],
])

@pytest.mark.parametrize( **test_case_table )
def test( test_params, cmdline_opts ):
  nstages = test_params.nstages
  inputs  = test_params.inputs
  bitwidth = test_params.bitwidth

  run_test_vector_sim( RegIncr_param( nstages ),
    mk_test_vector_table( nstages, inputs, bitwidth ), cmdline_opts )

# #-------------------------------------------------------------------------
# # Parameterized Testing of With nstages = [ 1, 2, 3, 4, 5, 6 ]
# #-------------------------------------------------------------------------

# @pytest.mark.parametrize( "n", [ 1, 2, 3, 4, 5, 6 ] )
# def test_random_nstages( n, cmdline_opts ):
#   run_test_vector_sim( RegIncr_param( p_nstages=n, p_bitwidths=8),
#     mk_test_vector_table( n, sample(range(0xff),20), 8 ), cmdline_opts )

# #-------------------------------------------------------------------------
# # Parameterized Testing of With bitwidths = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
# #-------------------------------------------------------------------------

# @pytest.mark.parametrize( "m", range(1, 8) )
# def test_random_bitwidths( m, cmdline_opts ):
#   run_test_vector_sim( RegIncr_param( p_nstages=3, p_bitwidths=m ),
#     mk_test_vector_table( 3, sample(range(0xff),20), m ), cmdline_opts )


#-------------------------------------------------------------------------
# Parameterized Testing of With nstages = [ 1, 2, 3, 4, 5, 6 ] and bitwidths = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
#-------------------------------------------------------------------------

@pytest.mark.parametrize( "n", range(1, 5))
@pytest.mark.parametrize( "m", range(1, 3))
def test_random_bitwidths_and_nstages( n, m, cmdline_opts ):
    run_test_vector_sim( RegIncr_param( p_nstages=n, p_bitwidths=m ),
        mk_test_vector_table( n, sample(range(0xff), 20), m ), cmdline_opts )
    
# Have problem starting at 9/3