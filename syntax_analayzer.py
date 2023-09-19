from symbol_table import symboltable as st

# Given a string and the current index position inside that string 
# will advance the current position until we have reached a Non whitespace character
# returns that value

"""

    Tokenizers functions

"""
def ignore_whitespace(string, curr_index):
    while (curr_index < len(string) and string[curr_index].isspace()):
        curr_index+=1
    
    return curr_index

def tokenize_jack_code(jack_code):
    curr_index = 0
    tokens = []

    while (curr_index < len(jack_code)):
        curr_index = ignore_whitespace(jack_code, curr_index)
        token = None
        if (curr_index >= len(jack_code)):
            break
        if (is_identifier_tokenizer(jack_code, curr_index)):
            token, curr_index = handle_identifier_tokenizer(jack_code, curr_index)
        elif (is_integer_tokenizer(jack_code, curr_index)):
            token, curr_index = handle_integer_tokenizer(jack_code, curr_index)
        elif (is_symbol_token(jack_code, curr_index)):
            token, curr_index = handle_symbol_token(jack_code, curr_index)
        elif (is_string_token(jack_code, curr_index)):
            token, curr_index = handle_string_token(jack_code, curr_index)
        else:
            raise Exception("Unknown token detected", jack_code[curr_index:])
    
        tokens.append(token)
    
    return tokens



def is_identifier_tokenizer(string, curr_index):
    return string[curr_index] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"

def handle_identifier_tokenizer(string, curr_index):
    curr_token = ""
    while (curr_index < len(string) and string[curr_index] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
        curr_token+= string[curr_index]
    
        curr_index+=1

    # returns keyword instead if it is a keyword
    keyword = ["class", "constructor", "function", "method", "field", 
               "static", "var", "int", "char", "boolean", "void", "true", 
               "false", "null", "this", "let", "do", "if", "else", "while", "return"]
    if (curr_token in keyword):
        return (("keyword", curr_token), curr_index)
    
    return (("identifier", curr_token), curr_index)

def is_integer_tokenizer(string, curr_index):
    return string[curr_index] in "0123456789"

def handle_integer_tokenizer(string, curr_index):
    curr_token = ""
    if (string[curr_index] == "0"):
        curr_token += string[curr_index]
        curr_index+= 1
        return (("integer", curr_token), curr_index)

    while (curr_index < len(string) and string[curr_index] in "0123456789"):
        curr_token += string[curr_index]
        curr_index+= 1
    
    return (("integer", curr_token), curr_index)

def is_symbol_token(string, curr_index):
    return string[curr_index] in "()[]}{.,;+-*/&|<>=-"

def handle_symbol_token(string, curr_index):
    if (string[curr_index] in "()[]}{.,;+-*/&|<>=-"):
        return (("symbol", string[curr_index]), curr_index + 1)

def is_string_token(string, curr_index):
    return string[curr_index] == "\""

def handle_string_token(string, curr_index):
    curr_index +=1

    curr_token = ""
    while (curr_index < len(string) and string[curr_index] != "\""):
        curr_token+= string[curr_index]
        curr_index += 1
    
    return (("string", curr_token), curr_index+1)



xml_string = ""


"""

    Below is where the vm writer code will be located


"""

def vm_writer_op(op):
    print(op)
    if (op == "+"):
        vm_code.append("add")
    elif (op == "-"):
        vm_code.append("sub")
    elif (op == "&"):
        vm_code.append("and")
    elif (op == "|"):
        vm_code.append("or")
    elif (op == "<"):
        vm_code.append("lt")
    elif (op == ">"):
        vm_code.append("gt")
    elif (op == "="):
        vm_code.append("eq")
    else:
        raise Exception("unknown op", op)
    
def vm_writer_keyword_constant(keyword):
    if (keyword == "true"):
        vm_code.append("push constant 1")
        vm_code.append("neg")
    elif (keyword == "false" or keyword == "null"):
        vm_code.append("push constant 0")
    elif (keyword == "this"):
        vm_code.append("push this 0")
    else:
        raise Exception("unknown keyword", keyword)
    




"""
    Syntax analyzer functions below

"""

vm_code = []
symboltable = st()

# Given a list of tokens an a value, assert that value matches the token
def match_token_value(tokens, value):
    type_token, value_token = tokens.pop(0)

    print("<" + type_token + ">", value_token, "</" + type_token + ">")

    if (value != value_token):
        raise Exception("Expected", value, "but got", value_token, "Tokenlist outputed:", tokens)
    
    return value_token

def match_token_type(tokens, typer):
    type_token, value_token = tokens.pop(0)

    print("<" + type_token + ">", value_token, "</" + type_token + ">")

    if (typer != type_token):
        raise Exception("Expected", typer, "but got", type_token, "Tokenlist outputed:", tokens)
    
    return value_token


def match_class(tokens):
    print("<class>")
    match_token_value(tokens, "class")
    match_class_names(tokens)
    match_token_value(tokens, "{")

    while (tokens[0][1] in ["static", "field"]):
        match_classVarDec(tokens)
    
    while (tokens[0][1] in ["constructor", "function", "method"]):
        match_subroutine_dec(tokens)

    match_token_value(tokens, "}")

    print("</class>")



def match_varName(tokens):
    return match_token_type(tokens, "identifier")

def match_subroutine_name(tokens):
    match_token_type(tokens, "identifier")

def match_class_names(tokens):
    match_token_type(tokens, "identifier")

def match_type(tokens):
    type_token, value_token = tokens[0]
    if (value_token not in ["int", "char", "boolean"] and type_token != "identifier"):
        raise Exception("Expected type but got", type_token, value_token, tokens)
    
    return match_token_value(tokens, value_token)

    
    
    



def match_varDec(tokens):
    print("<varDec>")
    match_token_value(tokens, "var")
    match_type(tokens)
    match_varName(tokens)

    while (tokens[0][1] == ","):
        match_token_value(tokens, ",")
        match_varName(tokens)
    
    match_token_value(tokens, ";")
    print("</varDec>")

def is_classVarDec(tokens):
    return (tokens[0][1] in ["static", "field"])

def match_classVarDec(tokens):
    print("<classVarDec>")
    type_token, value_token = tokens[0]
    if (value_token not in ["static", "field"]):
        raise Exception("Expected static or field but got", value_token)
    

    kind = match_token_value(tokens, value_token)
    type_ = match_type(tokens)
    name = match_varName(tokens)
    symboltable.define(name, type_, kind)

    while (tokens[0][1] == ","):
        match_token_value(tokens, ",")
        name = match_varName(tokens)
        symboltable.define(name, type_, kind)
    
    match_token_value(tokens, ";")
    print("</classVarDec>")


def match_subroutine_dec(tokens):
    print("<subroutineDec>")
    type_token, value_token = tokens[0]

    if (value_token not in ["constructor", "function", "method"]):
        raise Exception("Expected constructor, function, or method but got", value_token, tokens)
    
    match_token_value(tokens, value_token)
    
    if (tokens[0][1] == "void"):
        match_token_value(tokens, tokens[0][1])
    else:
        match_type(tokens)
    
    match_subroutine_name(tokens)
    match_token_value(tokens, "(")
    match_parameter_list(tokens)
    match_token_value(tokens, ")")
    match_subroutine_body(tokens)

    print("</subroutineDec>")



def match_parameter_list(tokens):
    print("<parameterlist>")
    if (tokens[0][1] == ")"):
        print("</parameterlist>")
        return

    match_type(tokens)
    match_varName(tokens)

    while (tokens[0][1] == ","):
        match_token_value(tokens, ",")
        match_type(tokens)
        match_varName(tokens)
    
    


    print("</parameterlist>")

def match_subroutine_body(tokens):
    print("<subroutinebody>")
    match_token_value(tokens, "{")

    while (tokens[0][1] == "var"):
        match_varDec(tokens)


    match_statements(tokens)
    match_token_value(tokens, "}")
    print("</subroutinebody>")


"""

    Statements

"""


def match_statements(tokens):
    print("<statements>")
    while (is_statement(tokens)):
        match_statement(tokens)

    print("</statements>")


def is_statement(tokens):
    return (tokens[0][1] in ["let", "if", "while", "do", "return"])

def match_statement(tokens):
    token_value = tokens[0][1]

    if (token_value == "let"):
        match_let_statement(tokens)
    elif (token_value == "if"):
        match_if_statement(tokens)
    elif (token_value == "while"):
        match_while_statement(tokens)
    elif (token_value == "do"):
        match_do_statement(tokens)
    elif (token_value == "return"):
        match_return_statement(tokens)
    else:
        raise Exception("Unknown statement", tokens)


def match_let_statement(tokens):
    print("<let statement>")
    match_token_value(tokens, "let")
    varname = match_varName(tokens)

    if (tokens[0][1] == "["):
        vm_code.append("push " + symboltable.kind_of(varname) + " " + str(symboltable.index_of(varname)))

        match_token_value(tokens, "[")
        match_expression(tokens)
        vm_code.append("add")
        vm_code.append("pop pointer 1")
        match_token_value(tokens, "]")

        while (tokens[0][1] == "["):
            match_token_value(tokens, "[")
            match_expression(tokens)
            vm_code.append("add")
            vm_code.append("pop pointer 1")
            match_token_value(tokens, "]")
    
    match_token_value(tokens, "=")
    match_expression(tokens)

    vm_code.append("pop " + symboltable.kind_of(varname) + " " + str(symboltable.index_of(varname)))

    match_token_value(tokens, ";")
    print("</let statement>")

def match_if_statement(tokens):
    print("<if statement>")
    match_token_value(tokens, "if")
    match_token_value(tokens, "(")
    match_expression(tokens)
    match_token_value(tokens, ")")

    match_token_value(tokens, "{")
    match_statements(tokens)
    match_token_value(tokens, "}")

    if (tokens[0][1] == "else"):
        match_token_value(tokens, "else")
        match_token_value(tokens, "{")
        match_statements(tokens)
        match_token_value(tokens, "}")

    print("</if statement>")


def match_while_statement(tokens):
    print("<while statement>")
    match_token_value(tokens, "while")
    match_token_value(tokens, "(")  
    match_expression(tokens)
    match_token_value(tokens, ")") 
    match_token_value(tokens, "{")
    match_statements(tokens)
    match_token_value(tokens, "}") 
    print("</while statement>")

def match_do_statement(tokens):
    print("<do statement>")
    match_token_value(tokens, "do")
    match_subroutine_call(tokens)
    match_token_value(tokens, ";")
    print("</do statement>")

def match_return_statement(tokens):
    print("<return statement>")
    match_token_value(tokens, "return")
    if (tokens[0][1] != ";"):
        match_expression(tokens)
    match_token_value(tokens, ";")
    print("</return statement>")

"""

    Expressions

"""

def match_keywordConstant(tokens):
    if (tokens[0][1] not in ["true", "false", "null", "this"]):
        raise Exception("Expected keyword constant but got", tokens[0][1], tokens)
    return match_token_value(tokens, tokens[0][1])

def match_unaryOp(tokens):
    match_token_value(tokens, "-")

def match_op(tokens):
    if (tokens[0][1] not in "+-*/&|<>="):
        raise Exception("Expected op but got", tokens[0][1], tokens)
    return match_token_value(tokens, tokens[0][1])

def match_term(tokens):
    print("<term>")
    type_token, value_token = tokens[0]
    # Integer constant 
    if (type_token == "integer"):
        integer_value = match_token_type(tokens, "integer")
        vm_code.append("push constant " + integer_value)
    # String constant
    elif (type_token == "string"):
        match_token_type(tokens, "string")
    # Keyword constant
    elif (value_token in ["true", "false", "null", "this"]):
        keyword_constant = match_keywordConstant(tokens)
        vm_writer_keyword_constant(keyword_constant)
    # VarName[Expression]
    elif (type_token == "identifier" and tokens[1][1] == "["):

        varname = match_varName(tokens)
        vm_code.append("push " + symboltable.kind_of(varname) + " " + str(symboltable.index_of(varname)))
        match_token_value(tokens, "[")
        match_expression(tokens)
        vm_code.append("add")
        vm_code.append("pop pointer 1")
        vm_code.append("push that 0")
        match_token_value(tokens, "]")
    # Subroutine call
    elif (type_token == "identifier" and tokens[1][1] == "("):

        match_subroutine_call(tokens)
    # VarName
    elif (type_token == "identifier"):
        varname = match_varName(tokens)
        vm_code.append("push " + symboltable.kind_of(varname) + " " + str(symboltable.index_of(varname)))
    # (expression)
    elif (value_token == "("):
        match_token_value(tokens, "(")
        match_expression(tokens)
        match_token_value(tokens, ")")

    # unaryOp term
    elif (value_token == "-"):
        match_token_value(tokens, "-")
        match_term(tokens)
        vm_code.append("neg")
    else:
        raise Exception("unknown term", tokens)
    
    print("</term>")

def match_expression(tokens):
    print("<expression>")
    match_term(tokens)

    while (tokens[0][1] in "+-*/&|<>="):
        op = match_op(tokens)
        match_term(tokens)
        vm_writer_op(op)

    print("</expression>")

def match_subroutine_call(tokens):
    print("<subroutine call>")
    if (tokens[1][1] == "("):
        match_subroutine_name(tokens)
        match_token_value(tokens, "(")
        match_expressionList(tokens)
        match_token_value(tokens, ")")
    else:
        match_varName(tokens)
        match_token_value(tokens, ".")
        match_subroutine_name(tokens)
        match_token_value(tokens, "(")
        match_expressionList(tokens)
        match_token_value(tokens, ")")
    
    print("</subroutine call>")




def match_expressionList(tokens):
    print("<expressionList>")
    if (tokens[0][1] == ")"):
        print("</expressionList>")
        return 
    match_expression(tokens)

    while (tokens[0][1] == ","):
        match_token_value(tokens, ",")
        match_expression(tokens)
    
    print("</expressionList>")



def generate_vm_code(jack_code):
    global vm_code, symboltable
    vm_code = []
    symboltable = st()

    tokens = tokenize_jack_code(jack_code)
    match_class(tokens)


# jack_code = """
#     class Bar {
#         method Fraction foo(int y) {
#             var int temp;
#             let temp = (xxx + 12)*-63;
#         }
#     }
# """

# ExpressionlessSquare = """
# class square {
#     method void incSize() {
#         if (x) {
#             do erase();
#             let size = size;
#             do draw();

#         }
#         return;
#     }
# }
# """

# Square = """
# class square {
#     method void incSize() {
#         if (((y + size) < 254) & ((x + size) < 510 )) {
#             do erase();
#             let size = size + 2;
#             do draw();
#         }

#         return;
#     }
# }
# """



# generate_vm_code(Square)
# print("")
# generate_vm_code(ExpressionlessSquare)
# print("")
# generate_vm_code(jack_code)

# code = """
#     class bruh {
#         static int ram, ll;
#         function void d() {
#             let ram = 0;
#             let ram[16] = 69;
#         }
#     }

# """

# generate_vm_code(code)
# print(symboltable.symbol_hashmap)
# print(vm_code)


