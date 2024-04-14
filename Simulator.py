f1=open("output_2.txt","w")
f1.close()


def binary_to_int(binary_string):
    """
    Convert a binary string to an integer.

    Args:
    - binary_string: A string representing a binary number.

    Returns:
    - Integer value of the binary number.
    """
    return int(binary_string, 2)

def Immediate(n,b):
    
   
    if n >=0:
        binary = bin(n)[2:]
    else:
        binary = bin(n & int("1" * (n.bit_length() + 1), 2))[2:]

   
    if len(binary) < b:
        if n >= 0:
            binary = '0' * (b - len(binary)) + binary
        else:                                                                       
            binary = '1' * (b - len(binary)) + binary
    elif len(binary) > b:
        binary = binary[-b:]
        
    return binary

def sext(bits, num_bits):
    """
    Perform sign extension on a string of bits to match a specified number of bits.

    Args:
    - bits: A string representing the original bit sequence.
    - num_bits: The number of bits to which the sequence should be extended.

    Returns:
    - Extended bit sequence as a string.
    """
    if len(bits) >= num_bits:
        return bits

    # If the most significant bit is 0, extend with zeros
    if bits[0] == '0':
        return '0' * (num_bits - len(bits)) + bits

    # If the most significant bit is 1, extend with ones
    return '1' * (num_bits - len(bits)) + bits

register_encoding = {
    "x0": "00000",
    "zero": "00000",
    "r0": "00000",
    "x1": "00001",
    "ra": "00001",
    "r1": "00001",
    "x2": "00010",
    "sp": "00010",
    "r2": "00010",
    "x3": "00011",
    "gp": "00011",
    "r3": "00011",
    "x4": "00100",
    "tp": "00100",
    "r4": "00100",
    "x5": "00101",
    "t0": "00101",
    "r5": "00101",
    "x6": "00110",
    "t1": "00110",
    "r6": "00110",
    "x7": "00111",
    "t2": "00111",
    "r6": "00111",
    "x8":"01000",
    "r8":"01000",
    "s0":"01000",
    "fp":"01000",
    "x9":"01001",
    "r9":"01001",
    "s1":"01001",
    "r10": "01010",
    "x10":"01010",
    "a0":"01010",
    "x11": "01011",
    "a1": "01011",
    "r11": "01011",
    "x12": "01100",
    "a2": "01100",
    "r12": "01100",
    "x13": "01101",
    "a3": "01101",
    "r13": "01101",
    "x14": "01110",
    "a4": "01110",
    "r14": "01110",
    "x15": "01111",
    "a5": "01111",
    "r15": "01111",
    "x16": "10000",
    "a6": "10000",
    "r16": "10000",
    "x17": "10001",
    "a7": "10001",
    "x17": "10001",
    "x18": "10010",
    "s2": "10010",
    "r18": "10010",
    "x19": "10011",
    "s3": "10011",
    "r19": "10011",
    "x20": "10100",
    "s4": "10100",
    "r20": "10100",
    "x21": "10101",
    "s5": "10101",
    "r21": "10101",
    "x22": "10110",
    "s6": "10110",
    "r22": "10110",
    "x23": "10111",
    "s7": "10111",
    "r23": "10111",
    "x24": "11000",
    "s8": "11000",
    "r24": "11000",
    "x25": "11001",
    "s9": "11001",
    "r25": "11001",
    "x26": "11010",
    "s10": "11010",
    "r26": "11010",
    "x27": "11011",
    "s11": "11011",
    "r27": "11011",
    "x28": "11100",
    "t3": "11100",
    "r28": "11100",
    "x29": "11101",
    "t4": "11101",
    "r29": "11101",
    "x30": "11110",
    "t5": "11110",
    "r30": "11110",
    "x31": "11111",
    "t6": "11111",
    "r31": "11111"
}


#reg values 
reg_vals={
    "00000":0,
    "00001":0,
    "00010":256,
    "00011":0,
    "00100":0,
    "00101":0,
    "00110":0,
    "00111":0,
    "01000":0,
    "01001":0,
    "01010":0,
    "01011":0,
    "01100":0,
    "01101":0,
    "01110":0,
    "01111":0,
    "10000":0,
    "10001":0,
    "10010":0,
    "10011":0,
    "10100":0,
    "10101":0,
    "10110":0,
    "10111":0,
    "11000":0,
    "11001":0,
    "11010":0,
    "11011":0,
    "11100":0,
    "11101":0,
    "11110":0,
    "11111":0
}

def sll(rs1,rs2):

    amount = binary_to_int(Immediate(rs2,32))
    r = rs1 << amount
    return r

def srl(rs1,rs2):

    amount = binary_to_int(Immediate(rs2,32))
    r = rs1 >> amount
    return r





def Rtype(line,op,pc,cl):
    if line[17:20]=="000":
        if line[25:32]=="0000000":                    #add
            sreg1=line[12:17]
            sreg2=line[7:12]
            dreg=line[20:25]
            reg_vals[dreg]=reg_vals[sreg1]+reg_vals[sreg2]

        elif line[25:32]=="0100000":                
            sreg1=line[15:20]
            sreg2=line[20:25]
            dreg=line[7:12]   
            reg_vals[dreg]=reg_vals[sreg1]-reg_vals[sreg2]

    elif line[17:20]=="001":
            sreg1=line[15:20]
            sreg2=line[20:25]
            dreg=line[7:12]
            reg_vals[dreg]=sll(reg_vals[sreg1],reg_vals[sreg2])
    elif line[17:20]=="010":
            sreg1=line[15:20]
            sreg2=line[20:25]
            dreg=line[7:12]
            if(Immediate(reg_vals[sreg1],32)<Immediate(reg_vals[sreg2],32)):
                reg_vals[dreg]=1

    elif line[17:20]=="011":
            sreg1=line[15:20]
            sreg2=line[20:25]
            dreg=line[7:12]
            if(reg_vals[sreg1]<reg_vals[sreg2]):
                reg_vals[dreg]=1
    elif line[17:20]=="100":
            sreg1=line[15:20]
            sreg2=line[20:25]
            dreg=line[7:12]
            reg_vals[dreg]=reg_vals[sreg1]^reg_vals[sreg2]

    elif line[17:20]=="101":
            sreg1=line[15:20]
            sreg2=line[20:25]
            dreg=line[7:12]
            reg_vals[dreg]=srl(reg_vals[sreg1],reg_vals[sreg2])
    elif line[17:20]=="110":
            sreg1=line[15:20]
            sreg2=line[20:25]
            dreg=line[7:12]
            reg_vals[dreg]=reg_vals[sreg1]|reg_vals[sreg2]
    elif line[17:20]=="111":
            sreg1=line[15:20]
            sreg2=line[20:25]
            dreg=line[7:12]
            reg_vals[dreg]=reg_vals[sreg1]&reg_vals[sreg2]
    



def Btype(line,op,pc):
    imm =""
    imm += "0" + line[-9:-13:-1] + line[-26:-32:-1] + line[-8] + line[-32]
    func = line[-13:-16:-1]
    rs1 = sext(line[-16:-21:-1])
    rs2 = sext(line[-21:-26:-1])
    if func == "000" :
        if rs1==rs2:
            pc += sext(imm)
            cl = sext(imm)
    if func == "001" :
        if rs1!= rs2:
            pc += sext(imm)
            cl = sext(imm)

    if func == "100" :
        if rs2>rs1:
            pc += sext(imm)
            cl = sext(imm)
    if func == "101" :
        if rs1>=rs2:
            pc += sext(imm)
            cl = sext(imm)
    if func == "110" :
        if unsigined(rs1)<unsigined(rs2):
            pc += sext(imm)
            cl = sext(imm)
    if func == "111" :
        if unsigined(rs1)>=unsigined(rs2):
            pc += sext(imm)
            cl = sext(imm)


global pc
global cl

def instructions(line,output,pc,cl):

    opc = line[-7:]
    if line == "0110011":
        Rtype(line,output,pc,cl)
    elif line == "0000011" or line == "1100111" or line == "0010011":
        Itype(line,output,pc,cl)
    elif line == "0100011":
        Stype(line,output,pc,cl)
    elif line == "1100011":
        Btype(line,output,pc,cl)
    elif line == "0110111" or line == "0010111":
        Utype(line,output,pc,cl)
    elif line == "1101111":
        Jtype(line,output,pc),cl











ip=[]
with open("input_2.txt", 'r') as file:
    ip = [line.strip() for line in file]
final = dict()
for i in range(len(ip)):
    final[(i+1)*4] = ip[i]
pc = 4 
cl = 4
op=[]
while True :
    if final[cl]=="00000000000000000000000001100011" :
        break
    x=final[cl]
    instructions(x,op,pc,cl)
    optemp=[programcounter,Immediate(reg_vals["00000"]),Immediate(reg_vals["00001"]),Immediate(reg_vals["00010"]),Immediate(reg_vals["00011"]),Immediate(reg_vals["00100"]),Immediate(reg_vals["00101"]),Immediate(reg_vals["00110"]),Immediate(reg_vals["00111"]),Immediate(reg_vals["01000"]),Immediate(reg_vals["01001"]),Immediate(reg_vals["01010"]),Immediate(reg_vals["01011"]),Immediate(reg_vals["01100"]),Immediate(reg_vals["01101"]),Immediate(reg_vals["01110"]),Immediate(reg_vals["01111"]),Immediate(reg_vals["10000"]),Immediate(reg_vals["10001"]),Immediate(reg_vals["10010"]),Immediate(reg_vals["10011"]),Immediate(reg_vals["10100"]),Immediate(reg_vals["10101"]),Immediate(reg_vals["10110"]),Immediate(reg_vals["10111"]),Immediate(reg_vals["11000"]),Immediate(reg_vals["11001"]),Immediate(reg_vals["11010"]),Immediate(reg_vals["11011"]),Immediate(reg_vals["11100"]),Immediate(reg_vals["11101"]),Immediate(reg_vals["11110"]),Immediate(reg_vals["11111"])]
    op.append(optemp)
f1 = open("output_2.txt","a")
f1.writelines(op)
f1.close()


