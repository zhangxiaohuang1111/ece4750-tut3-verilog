//========================================================================
// Registered Incrementer
//========================================================================
// This is a simple example of a module for a registered incrementer
// which combines a positive edge triggered register with a combinational
// +2 incrementer. We use flat register-transfer-level modeling.

`ifndef TUT3_VERILOG_REGINCR_REG_INCR_V
`define TUT3_VERILOG_REGINCR_REG_INCR_V

// You will need to uncomment this when you explore line tracing.
//
`include "/home/zh476/ece4750/tut3/sim/vc/trace.v"

module tut3_verilog_regincr_RegIncr
#(
  parameter p_bitwidths = 2
)
(
  input  logic       clk,
  input  logic       reset,
  input  logic [p_bitwidths-1:0] in_,
  output logic [p_bitwidths-1:0] out
);

  // Sequential logic

  logic [p_bitwidths-1:0] reg_out;
  always @( posedge clk ) begin
    if ( reset )
      reg_out <= 0;
    else
      reg_out <= in_;
  end
  logic [p_bitwidths-1:0] temp_wire;
  always_comb begin
    temp_wire = reg_out + 1;
  end
  assign out = temp_wire;
  // ''' TUTORIAL TASK '''''''''''''''''''''''''''''''''''''''''''''''''''
  // This model is incomplete. As part of the tutorial you will insert
  // combinational logic here to model the incrementer logic.
  // '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

  // You will need to uncomment this when you explore line tracing.
  //
  `ifndef SYNTHESIS
  
  logic [`VC_TRACE_NBITS-1:0] str;
  `VC_TRACE_BEGIN
  begin
    $sformat( str, "in %x reg_out (%x) out %x", in_, reg_out, out );
    vc_trace.append_str( trace_str, str );
  end
  `VC_TRACE_END
  
  `endif /* SYNTHESIS */

endmodule

`endif /* TUT3_VERILOG_REGINCR_REG_INCR_V */
