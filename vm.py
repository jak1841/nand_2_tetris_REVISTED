"""

    The purpose of this file is to translate VM code to assembly code

"""





def convert_VM_code_to_assembly(VM_code_array):
    label_instruction_number = 0    # This will be reset and used for when we use jumps and such
    # Initial code the sets sp to correct value
    hack_assembly_code = """
        @256
        D=A
        @SP
        M=D

    """
    
    for x in VM_code_array:
        if (is_push_constant(x)):
            hack_assembly_code+= push_constant_vm_to_assembly(x)
        elif (is_add(x)):
            hack_assembly_code += add_instruction_vm_to_assembly(x)
        elif (is_subtract(x)):
            hack_assembly_code+= subtract_instruction_vm_to_assembly(x)
        elif (is_neg(x)):
            hack_assembly_code+= negative_instruction_vm_to_assembly(x)
        else:
            raise Exception("Unknown VM instruction", x)
    

    # after code finishes goes into while loop
    hack_assembly_code += """
        (END)
        @END
        0;JMP
        
        """
    return hack_assembly_code
        


# Returns true if vm code is a push constant instruction
def is_push_constant(VM_code):
    return (VM_code[:13] == "push constant")

# Assume we have a push constant instruction returns the assembly code that implements that instruction
def push_constant_vm_to_assembly(VM_code):
    constant = VM_code[14:]
    assembly_constant = "    @" + constant
    return assembly_constant + """ 
        D=A
        @SP
        M=M+1
        A=M-1
        M=D

    """

def is_add(VM_code):
    return (VM_code == "add")

def add_instruction_vm_to_assembly(VM_code):
    return """
        @SP
        M=M-1
        A=M
        D=M
        A=A-1
        M=D+M

    """
    
    
def is_subtract(VM_code):
    return (VM_code == "sub")

def subtract_instruction_vm_to_assembly(VM_code):
    return """
        @SP
        M=M-1
        A=M
        D=M
        A=A-1
        M=M-D

    """
    

def is_neg(VM_code):
    return VM_code == "neg"

def negative_instruction_vm_to_assembly(VM_code):
    return """
        @SP
        A=M-1
        M=-M

    """
 
def is_equal(VM_code):
    return VM_code == "eq"

def equal_instruction_vm_to_assembly(VM_code):
    global label_instruction_number
    label_instruction_number+= 1
    return """
        @SP
        M=M-1
        A=M
        D=M
        A=A-1

        D=M-D

    """
     

