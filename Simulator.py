f1=open("output_2.txt","w")
f1.close()






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
    "00000":00000000000000000000000000000000,
    "00001":00000000000000000000000000000000,
    "00010":00000000000000000000000000000000,
    "00011":00000000000000000000000000000000,
    "00100":00000000000000000000000000000000,
    "00101":00000000000000000000000000000000,
    "00110":00000000000000000000000000000000,
    "00111":00000000000000000000000000000000,
    "01000":00000000000000000000000000000000,
    "01001":00000000000000000000000000000000,
    "01010":00000000000000000000000000000000,
    "01011":00000000000000000000000000000000,
    "01100":00000000000000000000000000000000,
    "01101":00000000000000000000000000000000,
    "01110":00000000000000000000000000000000,
    "01111":00000000000000000000000000000000,
    "10000":00000000000000000000000000000000,
    "10001":00000000000000000000000000000000,
    "10010":00000000000000000000000000000000,
    "10011":00000000000000000000000000000000,
    "10100":00000000000000000000000000000000,
    "10101":00000000000000000000000000000000,
    "10110":00000000000000000000000000000000,
    "10111":00000000000000000000000000000000,
    "11000":00000000000000000000000000000000,
    "11001":00000000000000000000000000000000,
    "11010":00000000000000000000000000000000,
    "11011":00000000000000000000000000000000,
    "11100":00000000000000000000000000000000,
    "11101":00000000000000000000000000000000,
    "11110":00000000000000000000000000000000,
    "11111":00000000000000000000000000000000,
}

def add_binary(a, b):
    # Convert binary strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    # Add the integers
    result = int_a + int_b
    
    # Convert the result back to binary and return
    return bin(result)[2:]

# Example usage:

print("Binary sum:", binary_sum)
def Rtype(line,output,pc):
    line1=line[::-1]
    if line1[12:15]=="000":
        if line1[25:32]=="0000000":                    #add
            sreg1=line1[15:20]
            sreg2=line1[20:25]
            dreg=line[7:12]
            reg_vals[dreg]=reg_vals[sreg1]+reg_vals[sreg2]
        elif line1[25:32]=="0100000":
            sreg1=line1[15:20]
            sreg2=line1[20:25]
            dreg=line[7:12]   
            reg_vals[dreg]=reg_vals[sreg1]+reg_vals[sreg2]

def Btype(line,output,pc):
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

    op = line[-7:]
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
f1 = open("output_2.txt","a")
f1.writelines(op)


