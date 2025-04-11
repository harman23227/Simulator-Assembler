RISC-V Simulator and Assembler
A Python-based RISC-V ISA simulator and assembler that provides functionality for converting RISC-V assembly code to binary machine code and simulating its execution.
Overview
This project implements a RISC-V processor simulator that can:

Assemble RISC-V assembly code into binary instructions
Execute these instructions in a simulated environment
Track register values and memory states
Output the processor state after execution

Features

Instruction Support: Handles all major RISC-V instruction types:

R-type (add, sub, sll, slt, sltu, xor, srl, or, and)
I-type (lw, addi, sltiu, jalr)
S-type (sw)
B-type (beq, bne, blt, bge, bltu, bgeu)
U-type (lui, auipc)
J-type (jal)


Register Support: Includes all 32 RISC-V registers with their standard naming conventions (x0-x31) and ABI names (zero, ra, sp, etc.)
Memory Management: Simulates memory operations with a simple dictionary-based implementation
Execution Flow: Handles control flow instructions (branches, jumps) correctly

Usage
Input Format
The simulator expects two input files:

input.txt: Contains RISC-V assembly code to be assembled
input_2.txt: Contains binary machine code to be executed

Output Format
The simulator produces:

output.txt: Assembly errors (if any) or binary machine code
output_2.txt: Execution trace with register values and memory contents

Running the Simulator
bash# First, assemble the code
python risc_v_assembler.py

# Then, simulate the execution
python risc_v_simulator.py
Implementation Details

Binary Handling: Includes utility functions for binary conversion and manipulation
Two's Complement: Properly handles signed values with two's complement representation
Immediate Values: Supports sign-extension and bit field manipulations needed for RISC-V instructions
Error Handling: Provides detailed error messages for invalid syntax or register names

Limitations

Currently supports a subset of the RISC-V ISA (RV32I)
Memory is implemented as a simple dictionary rather than a true memory model
Limited error checking and debugging capabilities
Does not support floating-point instructions or extensions

Future Improvements

Add support for the full RV32I instruction set
Implement RV32F and RV32D extensions for floating-point operations
Create a more sophisticated memory model
Add a debugging interface with breakpoints and step execution
Improve error reporting and handling
