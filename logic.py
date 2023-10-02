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

# This array will be used to help convert np array to int
def convert_boolean_np_array_to_a_int(bool_array):
    integer_value = np.dot(bool_array, 1 << np.arange(bool_array.size - 1, -1, -1))
    return integer_value

def convert_decimal_to_binary(decimal):
    binary_string = bin(decimal)[2:]
    binary_string_16_bits = binary_string.zfill(16)
    return binary_string_16_bits


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
    a_sum_b = np.zeros(16, dtype=bool)

    cin = False
    for x in range(16):
        reverse_index = 15 - x            
        a_xor_b = a[reverse_index] ^ b[reverse_index]
        a_sum_b[reverse_index] = a_xor_b ^ cin
        cin = (a[reverse_index] & b[reverse_index]) | (cin & (a_xor_b))



    return a_sum_b


# instead of creating a copy of np array will simply just do the results onto a and return it there.
def adder_16_bit_no_creatio(a, b):
    cin = False
    for x in range(16):
        reverse_index = 15 - x
        a_xor_b = a[reverse_index] ^ b[reverse_index]
        temp = a[reverse_index]
        a[reverse_index] = a_xor_b ^ cin
        cin = (temp & b[reverse_index]) | (cin & (a_xor_b))
    
    return a

zero = np.array([False for x in range(16)])

# Given 16 bit and its corresponding flags will return a list containing outputs, zero flag and negative flag
def alu_16_bit(x, y, zx, nx, zy, ny, f, no):
    
    # zx (!nx)

    out = None
    # For multiplication 
    if (zx and not (nx or zy or ny or f or no)):
        out = convert_boolean_np_array_to_a_int(x) * convert_boolean_np_array_to_a_int(y) % 65536
        out = get_bit_np_array(convert_decimal_to_binary(out))
        pass
    else:
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

comp_hashmap_to_binary = dict()
def init_comp_hashmap():
    global comp_hashmap_to_binary
    comp_hashmap_to_binary["0"] = "0101010"
    comp_hashmap_to_binary["1"] = "0111111"
    comp_hashmap_to_binary["-1"] = "0111010"
    comp_hashmap_to_binary["D"] = "0001100"
    comp_hashmap_to_binary["A"] = "0110000"
    comp_hashmap_to_binary["!D"] = "0001101"
    comp_hashmap_to_binary["!A"] = "0110001"
    comp_hashmap_to_binary["-D"] = "0001111"
    comp_hashmap_to_binary["-A"] = "0110011"
    comp_hashmap_to_binary["D+1"] = "0011111"
    comp_hashmap_to_binary["A+1"] = "0110111"
    comp_hashmap_to_binary["D-1"] = "0001110"
    comp_hashmap_to_binary["A-1"] = "0110010"
    comp_hashmap_to_binary["D+A"] = "0000010"
    comp_hashmap_to_binary["D-A"] = "0010011"
    comp_hashmap_to_binary["A-D"] = "0000111"
    comp_hashmap_to_binary["D&A"] = "0000000"
    comp_hashmap_to_binary["D|A"] = "0010101" 

    # Multiplication instruction
    comp_hashmap_to_binary["D*A"] = "0100000"
    comp_hashmap_to_binary["D*M"] = "1100000" 


    comp_hashmap_to_binary["M"] = "1110000"
    comp_hashmap_to_binary["!M"] = "1110001"
    comp_hashmap_to_binary["-M"] = "1110011"
    comp_hashmap_to_binary["M+1"] = "1110111"
    comp_hashmap_to_binary["M-1"] = "1110010"
    comp_hashmap_to_binary["D+M"] = "1000010"
    comp_hashmap_to_binary["D-M"] = "1010011"
    comp_hashmap_to_binary["M-D"] = "1000111"
    comp_hashmap_to_binary["D&M"] = "1000000"
    comp_hashmap_to_binary["D|M"] = "1010101"

    

init_comp_hashmap()
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

"""
        INPUT:              inM [16 bit]
                            instruction [16 bit]
                            reset [1 bit]
        
        OUTPUT:             
                            # To Data Memory
                            outM [16 bit]
                            writeM [1 bit]
                            addressM [16 bit]

                            # To instruction memory
                            PC [16 bit]
                            
""" 

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
            self.program_counter = adder_16_bit(self.program_counter, self.one)
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
            self.program_counter = adder_16_bit(self.program_counter, self.one)
        # 001 --> JGT 
        elif (instruction[13] == False and instruction[14] == False and instruction[15] == True):
            if (ng == False and zr == False):
                self.program_counter = self.a_register
            else:
                self.program_counter = adder_16_bit(self.program_counter, self.one)
        # 010 --> JEQ
        elif (instruction[13] == False and instruction[14] == True and instruction[15] == False):
            if (zr):
                self.program_counter = self.a_register
            else:
                self.program_counter = adder_16_bit(self.program_counter, self.one)
        # 011 --> JGE
        elif (instruction[13] == False and instruction[14] == True and instruction[15] == True):
            if (ng == False):
                self.program_counter = self.a_register
            else:
                self.program_counter = adder_16_bit(self.program_counter, self.one)
        # 100 --> JLT
        elif (instruction[13] == True and instruction[14] == False and instruction[15] == False):
            if (ng):
                self.program_counter = self.a_register
            else:
                self.program_counter = adder_16_bit(self.program_counter, self.one)
        # 101 --> JNE
        elif (instruction[13] == True and instruction[14] == False and instruction[15] == True):
            if (zr == False):
                self.program_counter = self.a_register
            else:
                self.program_counter = adder_16_bit(self.program_counter, self.one)
        # 110 --> JLE
        elif (instruction[13] == True and instruction[14] == True and instruction[15] == False):
            if (ng or zr):
                self.program_counter = self.a_register
            else:
                self.program_counter = adder_16_bit(self.program_counter, self.one)
        else:
            # JUMP 
            self.program_counter = self.a_register
        
        

        
        return [outM, writeM, self.a_register, self.program_counter]

class hack_computer:    
    def __init__(self):
        self.instruction_memory = np.zeros((65536, 16), dtype=bool)
        self.data_memory = np.zeros((65536, 16), dtype=bool)
        self.cpu = cpu_16_bit()  

        # This will be the inM value for when starting the data memory
        self.inM = get_bit_np_array("0000000000000000") 

    # Given the reset will do the hack computer operations
    def operation(self, reset):
        pc = convert_boolean_np_array_to_a_int(self.cpu.program_counter)
        instruction = self.instruction_memory[pc]

        outM, writeM, addressM, pc = self.cpu.operation(self.inM, instruction, reset)

        addressM = convert_boolean_np_array_to_a_int(addressM)
        if (writeM):
            self.data_memory[addressM] = outM
            self.inM = outM
        else:
            self.inM = self.data_memory[addressM]
        
        

    def do_n_operations(self, reset, n):
        for x in range(n):
            self.operation(reset)
    

    # Loads a given program which will be in the form of list of boolean np arrays
    def load_program(self, program):
        self.cpu.program_counter = get_bit_np_array("0000000000000000")
        self.instruction_memory = np.zeros((65536, 16), dtype=bool)
        for x in range(len(program)):
            self.instruction_memory[x] = program[x]


    # Show instruction memort from start and end exclusive
    def show_instruction_memory(self, start, end):
        instruction_memory_section = self.instruction_memory[start:end]
        return_array = [] 
        for x in instruction_memory_section:
            return_array.append(get_binary_number(x))
        
        print(return_array)
    # Shows data memory from start and end exclusive
    def show_data_memory(self, start, end):
        data_memory_section = self.data_memory[start:end]
        return_array = [] 
        for x in data_memory_section:
            return_array.append(get_binary_number(x))
        
        print(return_array)
    
    # Retrieves the data memory from start and end exclusive
    def get_data_memory(self, start, end):
        data_memory_section = self.data_memory[start:end]
        return_array = [] 
        for x in data_memory_section:
            return_array.append(get_binary_number(x))
        
        return return_array
        
    
    def show_registers(self):
        print("Register A:", get_binary_number(self.cpu.a_register))
        print("Register D:", get_binary_number(self.cpu.d_register))
        print("PC:", get_binary_number(self.cpu.program_counter))

    """
    
        SPEED TEST FUNCTIONSS BELOW
    
    """

    def speed_test(self):
        self.instruction_memory = np.random.rand(65536, 16) < 1

        import time
        start_time = time.time()
        self.do_n_operations(False, 100000)
        print("--- %s seconds ---" % (time.time() - start_time))

    




# hack = hack_computer()
# hack.speed_test()

    

    
