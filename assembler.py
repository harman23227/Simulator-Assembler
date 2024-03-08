def binary_string(number):                 #converting decimal to binary string
    return bin(number)[2:]              
def decimal_to_binary_twos_complement(decimal_number):
    if decimal_number < 0:
        binary_string = bin(decimal_number & int("1" * (decimal_number.bit_length() + 1), 2))[2:]   #decimal to 2s complement 
    else:
        binary_string = bin(decimal_number)[2:]

    return binary_string

def fill(binary_string, num_bits,s):
    if len(binary_string) < num_bits:
        binary_string = s * (num_bits - len(binary_string)) + binary_string   #filling
    
    elif len(binary_string) > num_bits:
        binary_string = binary_string[-num_bits:]
    
    return binary_string



r_type_instructions = {
    "add": {"opcode": "0110011", "rd": "", "funct3": "000", "rs1": "", "rs2": "", "funct7": "0000000"},
    "sub": {"opcode": "0110011", "rd": "", "funct3": "000", "rs1": "", "rs2": "", "funct7": "0100000"},
    "sll": {"opcode": "0110011", "rd": "", "funct3": "001", "rs1": "", "rs2": "", "funct7": "0000000"},
    "slt": {"opcode": "0110011", "rd": "", "funct3": "010", "rs1": "", "rs2": "", "funct7": "0000000"},
    "sltu": {"opcode": "0110011", "rd": "", "funct3": "011", "rs1": "", "rs2": "", "funct7": "0000000"},
    "xor": {"opcode": "0110011", "rd": "", "funct3": "100", "rs1": "", "rs2": "", "funct7": "0000000"},
    "srl": {"opcode": "0110011", "rd": "", "funct3": "101", "rs1": "", "rs2": "", "funct7": "0000000"},
    "or": {"opcode": "0110011", "rd": "", "funct3": "110", "rs1": "", "rs2": "", "funct7": "0000000"},
    "and": {"opcode": "0110011", "rd": "", "funct3": "111", "rs1": "", "rs2": "", "funct7": "0000000"}
}

i_type_instructions = {
    "lw": {"opcode": "0000011","rd": "", "funct3": "010", "rs1": "",  "imm": ""},
    "addi": {"opcode": "0010011","rd": "", "funct3": "000", "rs1": "",  "imm": ""},
    "sltiu": {"opcode": "0010011","rd": "", "funct3": "011", "rs1": "", "imm": ""},
    "jalr": {"opcode": "1100111","rd": "", "funct3": "000", "rs1": "",  "imm": ""}
}

s_type_instructions = {
    "sw": {"opcode": "0100011","imm":"", "funct3": "010","rs1":"","rs2":""},
}
b_type_instructions = {
    "beq": {"opcode": "1100011", "imm1": "", "funct3": "000", "rs1": "", "rs2": "", "imm2": ""},
    "bne": {"opcode": "1100011", "imm1": "", "funct3": "001", "rs1": "", "rs2": "", "imm2": ""},
    "blt": {"opcode": "1100011", "imm1": "", "funct3": "100", "rs1": "", "rs2": "", "imm2": ""},
    "bge": {"opcode": "1100011", "imm1": "", "funct3": "101", "rs1": "", "rs2": "", "imm2": ""},
    "bltu": {"opcode": "1100011", "imm1": "", "funct3": "110", "rs1": "", "rs2": "", "imm2": ""},
    "bgeu": {"opcode": "1100011", "imm1": "", "funct3": "111", "rs1": "", "rs2": "", "imm2": ""}
}

u_type_instructions = {
    "lui": {"opcode": "0110111","rd":"","imm":""},
    "auipc": {"opcode": "0010111","rd":"","imm":""},
}
j_type_instructions = {
    "jal": {"opcode": "1101111","rd":"","imm":""},
}

instruction_types=[r_type_instructions,i_type_instructions,s_type_instructions,b_type_instructions,u_type_instructions,j_type_instructions]

register_encoding = {
    "x0 (zero)": "00000",
    "x1 (ra)": "00001",
    "x2 (sp)": "00010",
    "x3 (gp)": "00011",
    "x4 (tp)": "00100",
    "x5 (t0)": "00101",
    "x6 (t1)": "00110",
    "x7 (t2)": "00111",
    "x8 (s0)": "01000",
    "x9 (s1)": "01001",
    "x10 (a0)": "01010",
    "x11 (a1)": "01011",
    "x12 (a2)": "01100",
    "x13 (a3)": "01101",
    "x14 (a4)": "01110",
    "x15 (a5)": "01111",
    "x16 (a6)": "10000",
    "x17 (a7)": "10001",
    "x18 (s2)": "10010",
    "x19 (s3)": "10011",
    "x20 (s4)": "10100",
    "x21 (s5)": "10101",
    "x22 (s6)": "10110",
    "x23 (s7)": "10111",
    "x24 (s8)": "11000",
    "x25 (s9)": "11001",
    "x26 (s10)": "11010",
    "x27 (s11)": "11011",
    "x28 (t3)": "11100",
    "x29 (t4)": "11101",
    "x30 (t5)": "11110",
    "x31 (t6)": "11111"
}

ip=[]
with open("input.txt", 'r') as file:
    lines = (line.strip() for line in file if line.strip() and not line.startswith('#'))   #removing uneccesary spaces and empty whitespaces plus comments
    ip = list(lines)   #storing all lines in a list
print (ip)
file.close()

# def rtype(func , list):
#     bintemp=""
#     bintemp+=r_type_instructions[func]["opcode"]                            #func for rtype , incomplete
#     #register
#     bintemp+=r_type_instructions[func]["funct3"]
#     #rs1
#     #rs2
#     bintemp+=r_type_instructions[func]["funct7"]



# def itype(func , list):
#     bintemp=""
#     bintemp+=i_type_instructions[func]["opcode"]                            #func for itype , incomplete
    


# def stype(func , list):
#     bintemp=""
#     bintemp+=s_type_instructions[func]["opcode"]                            #func for stype , incomplete
    


# def btype(func , list):
#     bintemp=""
#     bintemp+=b_type_instructions[func]["opcode"]                            #func for btype , incomplete
   


# def utype(func , list):
#     bintemp=""
#     bintemp+=u_type_instructions[func]["opcode"]                            #func for utype , incomplete
   


# def jtype(func , list):
#     bintemp=""
#     bintemp+=r_type_instructions[func]["opcode"]                            #func for jtype , incomplete
    


 


# for line in ip:
#     temp=""
#     flag=False
#     for word in line.split():
#         for type in instruction_types:                        #to check if line begins with a type function , then its whole line will be written
#             if word in type:
#                 if word in r_type_instructions.keys(): 
#                     temp+=rtype(word , line.split())   
#                     flag=True                          
#                     break
#                 if word in i_type_instructions.keys():
#                     temp+=itype(word , line.split())
#                     flag=True
#                     break
#                 if word in s_type_instructions.keys():
#                     temp+=stype(word , line.split())
#                     flag=True
#                     break
#                 if word in b_type_instructions.keys():
#                     temp+=btype(word , line.split())
#                     flag=True
#                     break
#                 if word in u_type_instructions.keys():
#                     temp+=utype(word , line.split())
#                     flag=True
#                     break
#                 if word in j_type_instructions.keys():
#                     temp+=jtype(word , line.split())
#                     flag=True
#                     break
#         if flag==True:
#             break            
        
    


                    



            
        







    

 