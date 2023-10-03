"""

    The purpose of this file is to translate VM code to assembly code

"""



label_instruction_number = 0 

def convert_VM_code_to_assembly(VM_code_array):
    global label_instruction_number
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
            hack_assembly_code+= push_constant_vm_to_assembly(x) + '\n'
        elif (is_add(x)):
            hack_assembly_code += add_instruction_vm_to_assembly(x) + '\n'
        elif (is_subtract(x)):
            hack_assembly_code+= subtract_instruction_vm_to_assembly(x) + '\n'
        elif (is_neg(x)):
            hack_assembly_code+= negative_instruction_vm_to_assembly(x)+ '\n'
        elif (is_equal(x)):
            hack_assembly_code+= equal_instruction_vm_to_assembly(x)+ '\n'
        elif (is_greater_than(x)):
            hack_assembly_code+= greater_than_instruction_vm_to_assembly(x)+ '\n'
        elif (is_less_than(x)):
            hack_assembly_code+= less_than_instruction_vm_to_assembly(x)+ '\n'
        elif (is_and(x)):
            hack_assembly_code+= and_instruction_vm_to_assembly(x)+ '\n'
        elif (is_or(x)):
            hack_assembly_code+= or_instruction_vm_to_assembly(x)+ '\n'
        elif (is_not(x)):
            hack_assembly_code+= not_instruction_vm_to_assembly(x)+ '\n'
        elif (is_push_predefined_memory_segment(x)):
            hack_assembly_code+= push_predefined_memory_segment_vm_assembly(x)+ '\n'
        elif (is_pop_predefined_memory_segment(x)):
            hack_assembly_code+= pop_predefined_memory_segment_vm_to_assembly(x)+ '\n'
        elif (is_label(x)):
            hack_assembly_code+= label_vm_to_assembly(x)+ '\n'
        elif (is_goto(x)):
            hack_assembly_code+= goto_vm_to_assembly(x)+ '\n'
        elif (is_if_goto(x)):
            hack_assembly_code+= if_goto_vm_to_assembly(x)+ '\n'
        elif (is_call_function(x)):
            hack_assembly_code += call_function_vm_to_assembly(x)+ '\n'
        elif (is_function(x)):
            hack_assembly_code+= function_vm_to_assembly(x)+ '\n'
        elif (is_return(x)):
            hack_assembly_code+= return_vm_to_assembly(x)+ '\n'
        elif (is_multiplication(x)):
            hack_assembly_code+= multiplication_instruction_vm_to_assembly(x) + '\n'
        elif (is_division(x)):
            hack_assembly_code+= division_instruction_vm_to_assembly(x) + '\n'
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

def is_multiplication(VM_code):
    return VM_code == "mult"

def multiplication_instruction_vm_to_assembly(VM_code):
    return """
        @SP
        M=M-1
        A=M
        D=M
        A=A-1
        M=D*M
    """

def is_division(VM_code):
    return VM_code == "div"

def division_instruction_vm_to_assembly(VM_code):
    return """
        @SP
        M=M-1
        A=M-1
        D=M
        A=A+1
        D=D/M
        A=A-1
        M=D


        
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
        """ + "@LBL_EQUAL" + str(label_instruction_number) + """
        D;JEQ

        @SP
        A=M-1
        M=0
        """+ "@LBL_END" + str(label_instruction_number) + """
        0;JMP
        """ + "(LBL_EQUAL" + str(label_instruction_number) + ")" + """
        
        @SP
        A=M-1
        M=-1
    """ + "(LBL_END" + str(label_instruction_number) + ")"

def is_greater_than(VM_code):
    return VM_code == "gt"

def greater_than_instruction_vm_to_assembly(VM_code):
    global label_instruction_number
    label_instruction_number+= 1
    
    return """
        @SP
        M=M-1
        A=M
        D=M
        A=A-1
        D=M-D
        """ + "@LBL_GREATER_THAN" + str(label_instruction_number) + """
        D;JGT

        @SP
        A=M-1
        M=0
        """+ "@LBL_END" + str(label_instruction_number) + """
        0;JMP
        """ + "(LBL_GREATER_THAN" + str(label_instruction_number) + ")" + """
        
        @SP
        A=M-1
        M=-1
    """ + "(LBL_END" + str(label_instruction_number) + ")"

def is_less_than(VM_code):
    return VM_code == "lt"

def less_than_instruction_vm_to_assembly(VM_code):
    global label_instruction_number
    label_instruction_number+= 1
    
    return """
        @SP
        M=M-1
        A=M
        D=M
        A=A-1
        D=M-D
        """ + "@LBL_LESS_THAN" + str(label_instruction_number) + """
        D;JLT

        @SP
        A=M-1
        M=0
        """+ "@LBL_END" + str(label_instruction_number) + """
        0;JMP
        """ + "(LBL_LESS_THAN" + str(label_instruction_number) + ")" + """
        
        @SP
        A=M-1
        M=-1
    """ + "(LBL_END" + str(label_instruction_number) + ")"

def is_and(VM_code):
    return VM_code == "and"

def and_instruction_vm_to_assembly(VM_code):
    return """
        @SP
        M=M-1
        A=M
        D=M
        A=A-1
        M=D&M
    """

def is_or(VM_code):
    return VM_code == "or"

def or_instruction_vm_to_assembly(VM_code):
    return """
        @SP
        M=M-1
        A=M
        D=M
        A=A-1
        M=D|M
        
    """

def is_not(VM_code):
    return VM_code == "not"

def not_instruction_vm_to_assembly(VM_code):
    return """
        @SP
        A=M-1
        M=!M

    """

def is_push_predefined_memory_segment(VM_code):
    items = VM_code.split()
    if (len(items) != 3):
        return False
    
    if (items[0] != "push"):
        return False
    
    return (items[1] in ["local", "argument", "this", "that", "temp", "pointer", "static"])

def push_predefined_memory_segment_vm_assembly(VM_code):
    """
        push segment index Push the value of segment[index] onto the stack.
    
    """
    items = VM_code.split()
    memory_segment = items[1]
    if (memory_segment == "local"):
        return "    @" + items[2] + """
            D=A
            @LCL
            A=D+M
            D=M 

            @SP
            M=M+1
            A=M-1
            M=D

        """
    elif (memory_segment == "argument"):
        return "    @" + items[2] + """
            D=A
            @ARG
            A=D+M
            D=M 

            @SP
            M=M+1
            A=M-1
            M=D
        """
    elif (memory_segment == "this"):
        return "    @" + items[2] + """
            D=A
            @THIS
            A=D+M
            D=M 

            @SP
            M=M+1
            A=M-1
            M=D
        """
    elif (memory_segment == "that"):
        return "    @" + items[2] + """
            D=A
            @THAT
            A=D+M
            D=M 

            @SP
            M=M+1
            A=M-1
            M=D
        """
    elif (memory_segment == "temp"):
        return "    @" + str(5 + int(items[2])) + """
            
            D=M 

            @SP
            M=M+1
            A=M-1
            M=D
        """
    elif (memory_segment == "pointer"):
        return "    @" + str(3 + int(items[2])) + """
            D=M

            @SP
            M=M+1
            A=M-1
            M=D
        """
    elif (memory_segment == "static"):
        return "    @" + str(16 + int(items[2])) + """
            D=M 
            @SP
            M=M+1
            A=M-1
            M=D
        """
    else:
        raise Exception("unexpected memory segment vm code", VM_code)

def is_pop_predefined_memory_segment(VM_code):
    items = VM_code.split()
    if (len(items) != 3):
        return False
    
    if (items[0] != "pop"):
        return False
    
    return (items[1] in ["local", "argument", "this", "that", "temp", "pointer", "static"])
    
def pop_predefined_memory_segment_vm_to_assembly(VM_code):
    items = VM_code.split()
    memory_segment = items[1]

    if (memory_segment == "local"):
        return  "    @" + items[2] + """
            D=A
            @LCL
            D=D+M

            @R11
            M=D

            @SP
            M=M-1
            A=M
            D=M

            @R11
            A=M

            M=D

        """
    elif (memory_segment == "argument"):
        return  "    @" + items[2] + """
            D=A
            @ARG
            D=D+M
            @R11
            M=D
            @SP
            M=M-1
            A=M
            D=M
            @R11
            A=M
            M=D

        """
    elif (memory_segment == "this"):
        return  "    @" + items[2] + """
            D=A
            @THIS
            D=D+M
            @R11
            M=D
            @SP
            M=M-1
            A=M
            D=M
            @R11
            A=M
            M=D

        """
    elif (memory_segment == "that"):
        return  "    @" + items[2] + """
            D=A
            @THAT
            D=D+M
            @R11
            M=D
            @SP
            M=M-1
            A=M
            D=M
            @R11
            A=M
            M=D

        """
    elif (memory_segment == "temp"):
        return  "    @" + str(5 + int(items[2])) + """
            D=A
            @R11
            M=D
            @SP
            M=M-1
            A=M
            D=M
            @R11
            A=M
            M=D

        """ 
    elif (memory_segment == "pointer"):
        return  "    @" + str(3 + int(items[2])) + """
            D=A

            @R11
            M=D

            @SP
            M=M-1
            A=M
            D=M

            @R11
            A=M
            M=D

        """ 
    elif (memory_segment == "static"):
        return  "    @" + str(16 + int(items[2])) + """
            D=A
            
            @R11
            M=D
            @SP
            M=M-1
            A=M
            D=M
            @R11
            A=M
            M=D

        """
    else:
        raise Exception("Unfamiliar Memory Segment VM_code", VM_code)

def is_label(VM_code):
    return VM_code[:5] == "label"

def label_vm_to_assembly(VM_code):
    return "(" + VM_code[6:] + ")\n" 

def is_goto(VM_code):
    return VM_code[:4] == "goto"

def goto_vm_to_assembly(VM_code):
    return "    @" + VM_code[5:] + """
        0;JMP

    """

def is_if_goto(VM_code):
    return VM_code[:7] == "if-goto"

def if_goto_vm_to_assembly(VM_code):
    return  """
        @SP
        A=M-1
        D=M
    """ + "    @" + VM_code[8:] + "\n    D;JNE "

def is_call_function(VM_code):
    return VM_code[:4] == "call"

def call_function_vm_to_assembly(VM_code):
    global label_instruction_number
    label_instruction_number+= 1

    call, function_name, number_arguments = VM_code.split()

    return "\n".join([
        # push return address
        "@" + function_name + str(label_instruction_number), 
        "D=A",
        "@SP",
        "M=M+1",
        "A=M-1",
        "M=D",

        # push LCL
        "@LCL", 
        "D=M",
        "@SP",
        "M=M+1",
        "A=M-1",
        "M=D", 

        # push arg
        "@ARG", 
        "D=M",
        "@SP",
        "M=M+1",
        "A=M-1",
        "M=D", 

        # Push This
        "@THIS", 
        "D=M",
        "@SP",
        "M=M+1",
        "A=M-1",
        "M=D",

        # Push that 
        "@THAT", 
        "D=M",
        "@SP",
        "M=M+1",
        "A=M-1",
        "M=D",

        # ARG = SP-n-5
        "@" + str(int(number_arguments) + 5), 
        "D=A", 
        "@SP", 
        "D=M-D", 
        "@ARG", 
        "M=D", 

        # LCL = SP
        "@SP", 
        "D=M", 
        "@LCL", 
        "M=D", 

        # goto f
        "@" + function_name,
        "0;JMP",

        # Return address
        "(" + function_name + str(label_instruction_number) + ")"
    ])

    pass

def is_function(VM_code):
    return VM_code[:8] == "function"

def function_vm_to_assembly(VM_code):
    fun, function_name, num_local_variables = VM_code.split()

    return "\n".join([
        "(" + function_name + ")", 
        "@" + num_local_variables, 
        "D=A",

        "(" + function_name + "_loop_label)",
        "@" + function_name + "END_label",
        "D;JLE",

        # Push constant 0
        "@SP",
        "M=M+1",
        "A=M-1",
        "M=0", 
        "D=D-1",

        "@" + function_name + "_loop_label",
        "0;JMP",

        "(" + function_name + "END_label" + ")"



    ])


def is_return(VM_code):
    return VM_code == "return"

def return_vm_to_assembly(VM_code):
    
    # *ARG = pop()
    return pop_predefined_memory_segment_vm_to_assembly("pop argument 0") + "\n".join([
        # SP = ARG + 1
        "@ARG", 
        "D=M+1",
        "@SP", 
        "M=D",

        # THAT = *(FRAME - 1)
        "@LCL", 
        "A=M-1", 
        "D=M",
        "@THAT", 
        "M=D", 

        # THIS = *(FRAME - 2)
        "@2", 
        "D=A", 
        "@LCL", 
        "A=M-D", 
        "D=M",
        "@THIS", 
        "M=D", 

        # ARG = *(FRAME - 3)
        "@3", 
        "D=A", 
        "@LCL", 
        "A=M-D", 
        "D=M",
        "@ARG", 
        "M=D", 


        # RET = *(FRAME - 5)
        "@5", 
        "D=A", 
        "@LCL", 
        "A=M-D", 
        "D=M",
        "@7", 
        "M=D", 

        # LCL = *(FRAME - 4)

        "@4", 
        "D=A", 
        "@LCL", 
        "A=M-D", 
        "D=M",
        "@LCL", 
        "M=D", 

        # GOTO RET
        "@7", 
        "A=M", 
        "0;JMP"
    ])
    


    


