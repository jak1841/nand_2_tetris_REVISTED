import numpy as np

# Given a binary string will generate the np array corresponding to that
def get_bit_np_array(binary_string):
    array = []
    for x in binary_string:
        assert x == "0" or x == "1"
        array.append(int(x))
    
    return np.array(array, dtype=bool)

# Given a bit binary string will return the corresponding binary number
def get_binary_number(bit_np_array):
    bit_string = ""
    for x in bit_np_array:
        if (x == True):
            bit_string+= "1"
        else:
            bit_string+= "0"
    
    return bit_string

def convert_boolean_np_array_to_a_int(bool_array):
        binary_array = bool_array.astype(np.uint8)

        # Convert binary array to integer
        integer_value = np.packbits(binary_array).view(np.uint16)[0]
        return integer_value


# LOGIC GATES WE CAN USE 
"""
AND, OR, NOT, XOR
"""

# Given two np arrayies and a selector bit will return a if !sel else b
def multiplexor(a, b, sel):
    if (sel[0] == False):
        return a
    return b

# Given a input bit np array and a selector bit will return an array where 1st index will be a and 2nd index will be b
def demultiplexor(input, sel):
    n = len(input)
    zero = np.array([False for x in range(n)])

    if (sel[0]):
        return np.array([zero, input])
    
    return np.array([input, zero])

# Assumed to be two bits
def full_adder(a, b, cin):
    a_xor_b = a ^ b
    sum_bit = a_xor_b ^ cin
    carry_out = (a & b) | (cin & (a_xor_b))

    return np.array([sum_bit, carry_out])

# Given two binary numbers which will be assumed to be sixteen bit will reurn another binary number a + b.
def adder_16_bit(a, b):
    a_sum_b = np.copy(zero)

    cin = False
    for x in range(16):
        reverse_index = 15 - x
        digit_sum = full_adder(a[reverse_index], b[reverse_index], cin)
        a_sum_b[reverse_index] = digit_sum[0]
        cin = digit_sum[1]
    



    return a_sum_b
zero = np.array([False for x in range(16)])

# Given 16 bit and its corresponding flags will return a list containing outputs, zero flag and negative flag
def alu_16_bit(x, y, zx, nx, zy, ny, f, no):
    speed_fast = True
    if (speed_fast):
        out = None
        if (zx):
            x = zero
        if (nx):
            x = ~x
        if (zy):
            y = zero
        if (ny):
            y = ~y
        if (f):
            out = adder_16_bit(x, y)
        else:
            out = x & y
        if (no):
            out = ~out
        ng = out[0]
        zr = np.array_equal(out, zero)
        return [out, zr, ng]
    
    else:
        is_x_zero = multiplexor(x, zero, zx)
        is_x_negate = multiplexor(is_x_zero, ~is_x_zero, nx)
        is_y_zero = multiplexor(y, zero, zy)
        is_y_negate = multiplexor(is_y_zero, ~is_y_zero, ny)
        add_x_y = adder_16_bit(is_x_negate, is_y_negate)
        and_x_y = is_x_negate & is_y_negate
        is_add_or_and = multiplexor(and_x_y, add_x_y, f)
        out = multiplexor(is_add_or_and, ~is_add_or_and, no)
        ng = out[0]
        zr = np.array_equal(out, zero)
        return [out, zr, ng]

# Given an ALU and binary flags bit representation will return a list containing output, zero flag, negative flag
def alu_binary_flags_16_bit(x, y, bf):
    return alu_16_bit(x, y, bf[0], bf[1], bf[2], bf[3], bf[4], bf[5])

alu_hashmap_to_binary = dict()

def init_alu_hashmap():
    global alu_hashmap_to_binary
    alu_hashmap_to_binary["ZERO"] = "101010"
    alu_hashmap_to_binary["ONE"] = "111111"
    alu_hashmap_to_binary["NEGATIVE_1"] = "111010"
    alu_hashmap_to_binary["X"] = "001100"
    alu_hashmap_to_binary["Y"] = "110000"
    alu_hashmap_to_binary["!X"] = "001101"
    alu_hashmap_to_binary["!Y"] = "110001"
    alu_hashmap_to_binary["NEGATIVE_X"] = "001111"
    alu_hashmap_to_binary["NEGATIVE_Y"] = "110011"
    alu_hashmap_to_binary["X+1"] = "011111"
    alu_hashmap_to_binary["Y+1"] = "110111"
    alu_hashmap_to_binary["X-1"] = "001110"
    alu_hashmap_to_binary["Y-1"] = "110010"
    alu_hashmap_to_binary["X+Y"] = "000010"
    alu_hashmap_to_binary["X-Y"] = "010011"
    alu_hashmap_to_binary["Y-X"] = "000111"
    alu_hashmap_to_binary["X&Y"] = "000000"
    alu_hashmap_to_binary["X|Y"] = "010101" 
init_alu_hashmap()

dest_hashmap_to_binary = dict()
def init_dest_hashmap():
    global dest_hashmap_to_binary
    dest_hashmap_to_binary["null"] = "000"
    dest_hashmap_to_binary["M"] = "001"
    dest_hashmap_to_binary["D"] = "010"
    dest_hashmap_to_binary["MD"] = "011"
    dest_hashmap_to_binary["A"] = "100"
    dest_hashmap_to_binary["AM"] = "101"
    dest_hashmap_to_binary["AD"] = "110"
    dest_hashmap_to_binary["AMD"] = "111"  
init_dest_hashmap()

jmp_hashmap_to_binary = dict()
def init_jmp_hashmap():
    global jmp_hashmap_to_binary
    jmp_hashmap_to_binary["null"] = "000"
    jmp_hashmap_to_binary["JGT"] = "001"
    jmp_hashmap_to_binary["JEQ"] = "010"
    jmp_hashmap_to_binary["JGE"] = "011"
    jmp_hashmap_to_binary["JLT"] = "100"
    jmp_hashmap_to_binary["JNE"] = "101"
    jmp_hashmap_to_binary["JLE"] = "110"
    jmp_hashmap_to_binary["JMP"] = "111"
init_jmp_hashmap()

# Reason we need the cpu class is for keeping track of the registers
class cpu_16_bit:
    def __init__(self):
        self.a_register = get_bit_np_array("0000000000000000")
        self.d_register = get_bit_np_array("0000000000000000")
        self.program_counter = get_bit_np_array("0000000000000000")
        self.one = get_bit_np_array("0000000000000001") # Optimization purposes

    def operation(self, inM, instruction, reset):
        # a instruction
        if (instruction[0] == False):
            self.a_register = instruction
            self.program_counter = adder_16_bit(self.one, self.program_counter)
            return [instruction, False, self.a_register, self.program_counter]
        
        # c instruction 111a cccc ccdd djjj
        # Reset program counter
        if (reset):
            self.program_counter = get_bit_np_array("0000000000000000")

        A_or_M = self.a_register
        if (instruction[3]):
            A_or_M = inM

        outM, zr, ng = alu_16_bit(self.d_register, A_or_M, instruction[4], instruction[5], instruction[6], instruction[7], instruction[8], instruction[9])

        # Destination Handling
        # Write to M
        writeM = instruction[12]
        # Write to A register
        if (instruction[10]):
            self.a_register = outM
        # Write to d register
        if (instruction[11]):
            self.d_register = outM
        
        # Jump Handling 
        # 000 --> NULL : NO JUMP
        if (instruction[13] == False and instruction[14] == False and instruction[15] == False):
            self.program_counter = adder_16_bit(self.one, self.program_counter)
        # 001 --> JGT 
        elif (instruction[13] == False and instruction[14] == False and instruction[15] == True):
            if (ng == False and zr == False):
                self.program_counter = self.a_register
        # 010 --> JEQ
        elif (instruction[13] == False and instruction[14] == True and instruction[15] == False):
            if (zr):
                self.program_counter = self.a_register
        # 011 --> JGE
        elif (instruction[13] == False and instruction[14] == True and instruction[15] == True):
            if (ng == False):
                self.program_counter = self.a_register
        # 100 --> JLT
        elif (instruction[13] == True and instruction[14] == False and instruction[15] == False):
            if (ng):
                self.program_counter = self.a_register
        # 101 --> JNE
        elif (instruction[13] == True and instruction[14] == False and instruction[15] == True):
            if (zr == False):
                self.program_counter = self.a_register
        # 110 --> JLE
        elif (instruction[13] == True and instruction[14] == True and instruction[15] == False):
            if (ng or zr):
                self.program_counter = self.a_register
        else:
            # JUMP 
            self.program_counter = self.a_register
        
        return [outM, writeM, self.a_register, self.program_counter]



class hack_computer:
    


        pass
    def __init__(self):
        pass   

    

    
