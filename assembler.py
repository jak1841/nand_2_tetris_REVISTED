"""

    The purpose of this file is to generate the binary code from an string that is assumed to be an hack assembly file

"""
import numpy as np
import logic as lg


# Given a binary string will generate the np array corresponding to that
def get_bit_np_array(binary_string):
    array = []
    for x in binary_string:
        assert x == "0" or x == "1"
        array.append(int(x))
    
    return np.array(array, dtype=bool)


def convert_int_to_np_array(integer):
    binary_string = bin(integer)[2:]
    binary_array = ["0" for x in range(16)]
    for x in range(len(binary_string)):
        reverse_index = 15-x
        reverse_binary = len(binary_string) - x - 1
        binary_array[reverse_index] = binary_string[reverse_binary]
    binary_string_16_bit = ''.join(binary_array)
    return get_bit_np_array(binary_string_16_bit)

# This function given a string will tokenize the string into an array and it ignores whitespace characters
def tokenize_string(input_string):
    return input_string.split()


def is_A_instruction(assembly_code):
    return assembly_code[0] == "@"

# returns a np array for A instruction
def translate_A_instructions(assembly_code):
    return convert_int_to_np_array(int(assembly_code[1:]))


# Given a assembly code pressumed to be of the c insturction type. Returns an array which will contain [dest, comp, jump]
def get_components_c_instruction(assembly_code):
    dest = "null"
    comp = "null"
    jmp = "null"

    equal_index = assembly_code.find("=")
    semi_colon_index = assembly_code.find(";")

    # dest=comp;jmp
    if (equal_index != -1 and semi_colon_index != -1):
        dest = assembly_code[:equal_index]
        comp = assembly_code[equal_index+1:semi_colon_index]
        jmp = assembly_code[semi_colon_index+1:]
    # dest=comp
    elif (equal_index != -1 and semi_colon_index == -1):
        dest = assembly_code[:equal_index] 
        comp = assembly_code[equal_index+1:]
    # comp;jmp
    elif (equal_index == -1 and semi_colon_index != -1):
        comp = assembly_code[:semi_colon_index]
        jmp = assembly_code[semi_colon_index+1:]
    else:
        raise Exception("unknown c instruction", assembly_code)
        
    return [dest, comp, jmp]


# returns a np array for 
def translate_C_instruction(assembly_code):
    dest, comp, jmp = get_components_c_instruction(assembly_code)

    dest_binary = lg.dest_hashmap_to_binary[dest]
    comp_binary = lg.comp_hashmap_to_binary[comp]
    jump_binary = lg.jmp_hashmap_to_binary[jmp]

    binary_instruction = "111" + comp_binary + dest_binary + jump_binary
    return get_bit_np_array(binary_instruction)


# Given a hack assembly string will return the binary of the 
def get_binary_from_hack_assembly(assembly_code):
    binary_array = []
    for x in tokenize_string(assembly_code):
        if (is_A_instruction(x)):
            binary_array.append(translate_A_instructions(x))
        else:
            binary_array.append(translate_C_instruction(x))
    return binary_array
    








