`ifndef ${seq_name.upper()}__SV
`define ${seq_name.upper()}__SV

typedef class ${seq_lib_name};
class ${seq_name} extends ${seq_lib_name}_base_seq;
  `uvm_object_utils(${seq_name})
  `uvm_add_to_seq_lib(${seq_name}, ${seq_lib_name})

  function new(string name = "${seq_name}");
    super.new(name);
  endfunction: new

  virtual task body();
    ${item_type} m_item = ${item_type}::type_id::create("m_item");
    repeat(10) begin
      `uvm_info(get_full_name, "Starting sequence", UVM_LOW)
      `uvm_do(m_item); // FOR_TEST
      #10; // FOR_TEST
    end
  endtask: body

endclass
`endif // ${seq_name.upper()}__SV
