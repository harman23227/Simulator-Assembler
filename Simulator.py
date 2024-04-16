fn = open("output_2.txt","w")
fn.close()
def bin_with_bits(num, num_bits):
    n="0b"+Immediate(num,num_bits)
    return n
def hex_with_bits(num):
     n="0x000"+hex(num)[2:]
     return n
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
nums = list()
nomber = 65536
for x in range(32):
     nums.append(nomber)
     nomber = nomber + 4
mem =dict.fromkeys(nums,0)

     
     
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





def Rtype(line,op,pc):
    print("Enetring r type ")
    if line[17:20]=="000":
        if line[25:32]=="0000000":                    #add
            sreg1=line[12:17]
            sreg2=line[7:12]
            dreg=line[20:25]
            reg_vals[dreg]=reg_vals[sreg1]+reg_vals[sreg2]
            ans=pc[0]+4

        elif line[25:32]=="0100000":                
            sreg1=line[15:20]
            sreg2=line[20:25]
            dreg=line[7:12]   
            reg_vals[dreg]=reg_vals[sreg1]-reg_vals[sreg2]
            ans=pc[0]+4

    elif line[17:20]=="001":
            sreg1=line[15:20]
            sreg2=line[20:25]
            dreg=line[7:12]
            reg_vals[dreg]=sll(reg_vals[sreg1],reg_vals[sreg2])
            ans=pc[0]+4
    elif line[17:20]=="010":
            sreg1=line[15:20]
            sreg2=line[20:25]
            dreg=line[7:12]
            if(Immediate(reg_vals[sreg1],32)<Immediate(reg_vals[sreg2],32)):
                reg_vals[dreg]=1
            ans=pc[0]+4

    elif line[17:20]=="011":
            sreg1=line[15:20]
            sreg2=line[20:25]
            dreg=line[7:12]
            if(reg_vals[sreg1]<reg_vals[sreg2]):
                reg_vals[dreg]=1
            ans=pc[0]+4
    elif line[17:20]=="100":
            sreg1=line[15:20]
            sreg2=line[20:25]
            dreg=line[7:12]
            reg_vals[dreg]=reg_vals[sreg1]^reg_vals[sreg2]
            ans=pc[0]+4

    elif line[17:20]=="101":
            sreg1=line[15:20]
            sreg2=line[20:25]
            dreg=line[7:12]
            reg_vals[dreg]=srl(reg_vals[sreg1],reg_vals[sreg2])
            ans=pc[0]+4
    elif line[17:20]=="110":
            sreg1=line[15:20]
            sreg2=line[20:25]
            dreg=line[7:12]
            reg_vals[dreg]=reg_vals[sreg1]|reg_vals[sreg2]
            ans=pc[0]+4
    elif line[17:20]=="111":
            sreg1=line[15:20]
            sreg2=line[20:25]
            dreg=line[7:12]
            reg_vals[dreg]=reg_vals[sreg1]&reg_vals[sreg2]
            ans=pc[0]+4
    ans = pc[0]+4
    return ans

def Btype(line,op,pc):   #btype
    print("Enetring b  type ")
    imm =""
    imm += "0" + line[-9:-13:-1] + line[-26:-32:-1] + line[-8] + line[-32] 
    imm = imm[-1::-1]
    func = line[-13:-16:-1]
    func = reversed(func)
    rs1 = reversed(line[-16:-21:-1])
    rs2 = reversed(line[-21:-26:-1])
    if func == "000" :
        if Immediate(reg_vals[rs1],32)==Immediate(reg_vals[rs2],32):
            imm=imm+"0"
            ans = binary_to_int(sext(imm,32))
    if func == "001" :
        if Immediate(reg_vals[rs1],32)!=Immediate(reg_vals[rs2],32):
            imm=imm+"0"
            ans = binary_to_int(sext(imm,32))
    if func == "100" :
        if Immediate(reg_vals[rs1],32)<Immediate(reg_vals[rs2],32):
            imm=imm+"10"
            ans = binary_to_int(sext(imm,32))

    if func == "101" :
        if Immediate(reg_vals[rs1],32)>=Immediate(reg_vals[rs2],32):
            imm=imm+"0"
            ans = binary_to_int(sext(imm,32))

    if func == "110" :
        if reg_vals[rs1]<reg_vals[rs2]:
            imm=imm+"0"
            ans = binary_to_int(sext(imm,32))

    if func == "111" :
        if reg_vals[rs1]>=reg_vals[rs2]:
            imm=imm+"0"
            ans = binary_to_int(sext(imm,32))
    return ans

        
def Jtype(line,output,pc):
    print("Enetring j type ")
    rd = line[-7:-12]
    imm = "0" + line[-32:-22:-1] +line[-21] + line[-21:-13:-1] + line[-32]
    reg_vals[rd] = pc[0] +4
    ans = binary_to_int(sext(imm, 32)) 
    return ans

def Utype(line,output,pc):
    imm=line[0:20]+"000000000000"
    rsd=line[20:25]
    print("entering U type")
    if(line[25:32]=="0110111"):
          reg_vals[rsd]=sext(imm,32)
    elif(line[25:32]=="0010111"):
          reg_vals[25:32]=pc[0]+sext(imm,32)
    return pc[0]+4
          
          
def Stype(line,output,pc):
     imm=line[0:7]+line[20:25]
     immd=binary_to_int(imm)
     rs1=line[12:17]
     rs2=line[7:12]
     val=reg_vals[rs1]+immd
     mem[val]=reg_vals[rs2]
     return pc[0]+4


     

def instructions(line,output,pc):
    print("Enetring intruction ")
    op = line[-7:]
    if op == "0110011":
        ans = Rtype(line,output,pc)
    # elif op == "0000011" or op == "1100111" or op == "0010011":
    #     Itype(line,output,pc)
    # elif op == "0100011":
    #     Stype(line,output,pc)
    elif op == "1100011":
        ans = Btype(line,output,pc)
    elif op == "0110111" or op== "0010111":
              Utype(line,output,pc)
    elif op == "1101111":
        ans = Jtype(line,output,pc)
    return ans











ip=[]
with open("input_2.txt", 'r') as file:
    ip = [line.strip() for line in file]
final = dict()
for i in range(len(ip)):
    final[(i+1)*4] = ip[i]
pc = [4]
op=[]
while True :
    print(pc[0]," ")
    if final[pc[0]]=="00000000000000000000000001100011" :
        break
    x=final[pc[0]]
    pc[0] = instructions(x,op,pc)
    optemp=bin_with_bits(pc[0],32)+" "+bin_with_bits(reg_vals["00000"],32)+" "+bin_with_bits(reg_vals["00001"],32)+" "+bin_with_bits(reg_vals["00010"],32)+" "+bin_with_bits(reg_vals["00011"],32)+" "+bin_with_bits(reg_vals["00100"],32)+" "+bin_with_bits(reg_vals["00101"],32)+" "+bin_with_bits(reg_vals["00110"],32)+" "+bin_with_bits(reg_vals["00111"],32)+" "+bin_with_bits(reg_vals["01000"],32)+" "+bin_with_bits(reg_vals["01001"],32)+" "+bin_with_bits(reg_vals["01010"],32)+" "+bin_with_bits(reg_vals["01011"],32)+" "+bin_with_bits(reg_vals["01100"],32)+" "+bin_with_bits(reg_vals["01101"],32)+" "+bin_with_bits(reg_vals["01110"],32)+" "+bin_with_bits(reg_vals["01111"],32)+" "+bin_with_bits(reg_vals["10000"],32)+" "+bin_with_bits(reg_vals["10001"],32)+" "+bin_with_bits(reg_vals["10010"],32)+" "+bin_with_bits(reg_vals["10011"],32)+" "+bin_with_bits(reg_vals["10100"],32)+" "+bin_with_bits(reg_vals["10101"],32)+" "+bin_with_bits(reg_vals["10110"],32)+" "+bin_with_bits(reg_vals["10111"],32)+" "+bin_with_bits(reg_vals["11000"],32)+" "+bin_with_bits(reg_vals["11001"],32)+" "+bin_with_bits(reg_vals["11010"],32)+" "+bin_with_bits(reg_vals["11011"],32)+" "+bin_with_bits(reg_vals["11100"],32)+" "+bin_with_bits(reg_vals["11101"],32)+" "+bin_with_bits(reg_vals["11110"],32)+" "+bin_with_bits(reg_vals["11111"],32)+"\n"
    op.append(optemp)
f1 = open("output_2.txt","a")
f1.writelines(op)
memory = []
for i in range(65536,65664,4):
     no = hex_with_bits(i)+":"+bin_with_bits(mem[i],32)+"\n"
     print
     memory.append(no)
print(mem)
print(memory)
f1.writelines(memory)
f1.close()
