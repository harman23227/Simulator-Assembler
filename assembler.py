def binary_string(number):
    return bin(number)[2:]

r_type_instructions = {
    "add": {"opcode": "0110011", "funct3": "000", "funct7": "0000000"},
    "sub": {"opcode": "0110011", "funct3": "000", "funct7": "0100000"},
    "sll": {"opcode": "0110011", "funct3": "001", "funct7": "0000000"},
    "slt": {"opcode": "0110011", "funct3": "010", "funct7": "0000000"},
    "sltu": {"opcode": "0110011", "funct3": "011", "funct7": "0000000"},
    "xor": {"opcode": "0110011", "funct3": "100", "funct7": "0000000"},
    "srl": {"opcode": "0110011", "funct3": "101", "funct7": "0000000"},
    "or": {"opcode": "0110011", "funct3": "110", "funct7": "0000000"},
    "and": {"opcode": "0110011", "funct3": "111", "funct7": "0000000"}
}
i_type_instructions = {
    "lw": {"opcode": "0000011", "funct3": "010"},
    "addi": {"opcode": "0010011", "funct3": "000"},
    "sltiu": {"opcode": "0010011", "funct3": "011"},
    "jalr": {"opcode": "1100111", "funct3": "000"}
}
s_type_instructions = {
    "sw": {"opcode": "0100011", "funct3": "010"},
}
b_type_instructions = {
    "beq": {"opcode": "1100011", "funct3": "000"},
    "bne": {"opcode": "1100011", "funct3": "001"},
    "blt": {"opcode": "1100011", "funct3": "100"},
    "bge": {"opcode": "1100011", "funct3": "101"},
    "bltu": {"opcode": "1100011", "funct3": "110"},
    "bgeu": {"opcode": "1100011", "funct3": "111"},
}
u_type_instructions = {
    "lui": {"opcode": "0110111"},
    "auipc": {"opcode": "0010111"},
}
j_type_instructions = {
    "jal": {"opcode": "1101111"},
}
