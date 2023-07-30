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




