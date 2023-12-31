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
    while (curr_index < len(string) and string[curr_index] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"):
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
    return string[curr_index] in "()[]}{.,;+-*/&|<>=-^!"

def handle_symbol_token(string, curr_index):
    if (string[curr_index] in "()[]}{.,;+-*/&|<>=-^!"):
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
    elif (op == "*"):
        vm_code.append("mult")
    elif (op == "/"):
        vm_code.append("div")
    elif (op == "^"):
        vm_code.append("power")
    elif (op == "!"):
        vm_code.append("not")

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
current_class_name = ""

# Given a list of tokens an a value, assert that value matches the token
def match_token_value(tokens, value):
    type_token, value_token = tokens.pop(0)


    if (value != value_token):
        raise Exception("Expected", value, "but got", value_token, "Tokenlist outputed:", tokens)
    
    return value_token

def match_token_type(tokens, typer):
    type_token, value_token = tokens.pop(0)


    if (typer != type_token):
        raise Exception("Expected", typer, "but got", type_token, value_token,  "Tokenlist outputed:", tokens)
    
    return value_token


def match_class(tokens):
    global current_class_name
    match_token_value(tokens, "class")
    current_class_name = match_class_names(tokens)
    match_token_value(tokens, "{")

    while (tokens[0][1] in ["static", "field"]):
        match_classVarDec(tokens)
    
    while (tokens[0][1] in ["constructor", "function", "method"]):
        match_subroutine_dec(tokens)

    match_token_value(tokens, "}")




def match_varName(tokens):
    return match_token_type(tokens, "identifier")

def match_subroutine_name(tokens):
    return match_token_type(tokens, "identifier")

def match_class_names(tokens):
    return match_token_type(tokens, "identifier")

def match_type(tokens):
    type_token, value_token = tokens[0]
    if (value_token not in ["int", "char", "boolean"] and type_token != "identifier"):
        raise Exception("Expected type but got", type_token, value_token, tokens)
    
    return match_token_value(tokens, value_token)

    
    
    



def match_varDec(tokens):
    match_token_value(tokens, "var")
    type_ = match_type(tokens)
    name = match_varName(tokens)

    symboltable.define(name, type_, "local")

    while (tokens[0][1] == ","):
        match_token_value(tokens, ",")
        name = match_varName(tokens)
        symboltable.define(name, type_, "local")
    
    match_token_value(tokens, ";")

def is_classVarDec(tokens):
    return (tokens[0][1] in ["static", "field"])

def match_classVarDec(tokens):
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


def match_subroutine_dec(tokens):
    type_token, value_token = tokens[0]
    symboltable.startSubroutine()

    if (value_token not in ["constructor", "function", "method"]):
        raise Exception("Expected constructor, function, or method but got", value_token, tokens)
    
    match_token_value(tokens, value_token)
    
    if (tokens[0][1] == "void"):
        match_token_value(tokens, tokens[0][1])
    else:
        match_type(tokens)
    
    subroutine_name = match_subroutine_name(tokens)
    match_token_value(tokens, "(")
    match_parameter_list(tokens)
    match_token_value(tokens, ")")
    match_subroutine_body(tokens, subroutine_name)

    



def match_parameter_list(tokens):
    if (tokens[0][1] == ")"):
        return

    type_ = match_type(tokens)
    var_name = match_varName(tokens)

    symboltable.define(var_name, type_, "argument")

    while (tokens[0][1] == ","):
        match_token_value(tokens, ",")
        type_ = match_type(tokens)
        var_name = match_varName(tokens)
        symboltable.define(var_name, type_, "argument")
    
    



# furthermore it returns the number of local variables in subroutine body
def match_subroutine_body(tokens, subroutine_name):
    match_token_value(tokens, "{")

    while (tokens[0][1] == "var"):
        match_varDec(tokens)

    vm_code.append("function " + current_class_name+ "." + subroutine_name + " " + str(symboltable.var_index))


    match_statements(tokens)
    match_token_value(tokens, "}")


"""

    Statements

"""


def match_statements(tokens):
    while (is_statement(tokens)):
        match_statement(tokens)



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
    match_token_value(tokens, "let")
    varname = match_varName(tokens)

    if (tokens[0][1] == "["):
        vm_code.append("push " + symboltable.kind_of(varname) + " " + str(symboltable.index_of(varname)))

        match_token_value(tokens, "[")
        match_expression(tokens)
        vm_code.append("add")
        match_token_value(tokens, "]")

        while (tokens[0][1] == "["):
            match_token_value(tokens, "[")
            match_expression(tokens)
            vm_code.append("add")
            match_token_value(tokens, "]")
        
        vm_code.append("pop pointer 1")
    
        match_token_value(tokens, "=")
        match_expression(tokens)

        vm_code.append("pop that 0")
    else:
        match_token_value(tokens, "=")
        match_expression(tokens)
        vm_code.append("pop " + str(symboltable.kind_of(varname)) + " " + str(symboltable.index_of(varname)))


    match_token_value(tokens, ";")

label_counter = 0

def match_if_statement(tokens):
    global label_counter
    label_counter+= 2
    L1 = "if_label" + str(label_counter -2)
    L2 = "if_label" + str(label_counter - 1)

    match_token_value(tokens, "if")
    match_token_value(tokens, "(")
    match_expression(tokens)
    match_token_value(tokens, ")")

    vm_code.append("not")   # Calculating -(cond)
    vm_code.append("if-goto " + L1)



    match_token_value(tokens, "{")
    match_statements(tokens)
    match_token_value(tokens, "}")

    vm_code.append("goto " + L2)
    vm_code.append("label " + L1)

    if (tokens[0][1] == "else"):
        match_token_value(tokens, "else")
        match_token_value(tokens, "{")
        match_statements(tokens)
        match_token_value(tokens, "}")
    
    vm_code.append("label " + L2)
    
    
    



def match_while_statement(tokens):
    global label_counter

    L1 = "while_label" + str(label_counter)
    L2 = "while_label" + str(label_counter + 1)


    vm_code.append("label " + L1)
    match_token_value(tokens, "while")
    match_token_value(tokens, "(")  
    match_expression(tokens)

    vm_code.append("not")
    vm_code.append("if-goto " + L2)

    match_token_value(tokens, ")") 
    match_token_value(tokens, "{")
    match_statements(tokens)
    match_token_value(tokens, "}") 
    vm_code.append("goto " + L1)

    vm_code.append("label " + L2)

    label_counter+=2

def match_do_statement(tokens):
    match_token_value(tokens, "do")
    match_subroutine_call(tokens)
    match_token_value(tokens, ";")

def match_return_statement(tokens):

    match_token_value(tokens, "return")
    if (tokens[0][1] != ";"):
        match_expression(tokens)
    vm_code.append("return")
    match_token_value(tokens, ";")

"""

    Expressions

"""

def match_keywordConstant(tokens):
    if (tokens[0][1] not in ["true", "false", "null", "this"]):
        raise Exception("Expected keyword constant but got", tokens[0][1], tokens)
    return match_token_value(tokens, tokens[0][1])

def match_unaryOp(tokens):
    if (tokens[0][1] == "-"):
        match_token_value(tokens, "-")
    else:
        match_token_value(tokens, "!")

def match_op(tokens):
    if (tokens[0][1] not in "+-*/&|<>=^!"):
        raise Exception("Expected op but got", tokens[0][1], tokens)
    return match_token_value(tokens, tokens[0][1])

def match_term(tokens):
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
    elif (type_token == "identifier" and tokens[1][1] == "."):
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
    elif (value_token in "-!"):
        if (value_token == "-"):
            match_token_value(tokens, "-")
            match_term(tokens)
            vm_code.append("neg")
        else:
            match_token_value(tokens, "!")
            match_term(tokens)
            vm_code.append("not")
    else:
        raise Exception("unknown term", tokens)
    

def match_expression(tokens):
    match_term(tokens)

    while (tokens[0][1] in "+-*/&|<>=^!"):
        op = match_op(tokens)
        match_term(tokens)
        vm_writer_op(op)


def match_subroutine_call(tokens):
    
    class_name = match_varName(tokens)
    match_token_value(tokens, ".")
    subroutine_name = match_subroutine_name(tokens)
    match_token_value(tokens, "(")
    num_args = match_expressionList(tokens)
    vm_code.append("call " + class_name + "." + subroutine_name + " " + str(num_args))
    match_token_value(tokens, ")")

    




def match_expressionList(tokens):
    if (tokens[0][1] == ")"):
        return 0
    num_arg = 1
    match_expression(tokens)


    while (tokens[0][1] == ","):
        num_arg+=1
        match_token_value(tokens, ",")
        match_expression(tokens)
    
    return num_arg
    



def generate_vm_code(jack_code):
    global vm_code, symboltable, label_counter
    vm_code = []
    symboltable = st()
    label_counter = 0

    # Boot strap code which calls function name
    # vm_code.append("call main 0")

    tokens = tokenize_jack_code(jack_code)
    match_class(tokens)
    return vm_code

def generate_vm_code_with_bootstrap(jack_code):
    global vm_code, symboltable, label_counter, current_class_name
    vm_code = ["call Main.main 0", 
               "label main.end",
               "goto main.end"]
    symboltable = st()
    label_counter = 0
    current_class_name = ""

    jack_code = add_libraries_to_jack_code(jack_code)

    tokens = tokenize_jack_code(jack_code)
    while (tokens and tokens[0][1] == "class"):
        match_class(tokens)
    return vm_code

# adds the math library to jack code 
def add_math_libary(jack_code):
    math_library = """
        class Math {
            function void abs(int x) {
                if (x > 0) {
                    return x;
                } else {
                    return -x;
                }
            }
        }

    """
    return math_library + jack_code

def add_screen_library(jack_code):
    """

        Credit for this class goes to https://github.com/havivha/Nand2Tetris/blob/master/12/Screen.jack
        Reason is because this type of stuff is so complicated for me to code and I was stuck on this for legit so long 

    """
    screen_library = """
        class Screen {
            function void drawPixel(int x, int y) {
                var int RAM, address, mask; 
                let address = (32*y) + (x/16) + 16384;
                let mask = 2^(x & 15);
                let RAM[address] = RAM[address] | mask;
                return 0;
            }


            function void drawLine(int x1, int y1, int x2, int y2) {
                var int dx, dy;
                var int temp;
                
                
                if( x1 > x2 ) {
                    let temp = x1;
                    let x1 = x2;
                    let x2 = temp;
                    let temp = y1;
                    let y1 = y2;
                    let y2 = temp;
                }

                let dx = x2 - x1;
                let dy = y2 - y1;
                
                if( dx = 0 ) {
                    do Screen.drawVerticalLine( x1, y1, y2 );
                }
                else { 
                    if( dy = 0 ) {
                        do Screen.drawHorizontalLine( x1, x2, y1 );
                    }
                    else {
                        do Screen.drawDiagonalLine( x1, y1, x2, y2, dx, dy );
                    }
                }
                
                return 0;
            }


            function void drawDiagonalLine( int x1, int y1, int x2, int y2, int dx, int dy ) {
                var int a, b;
                var int adyMinusbdx;
                var int y_incr;

                let a = 0;
                let b = 0;
                let adyMinusbdx = 0;
                
                if( dy < 0 ) {
                    let y_incr = -1;
                }
                else {
                    let y_incr = 1;
                }

                while( !(a > dx) & (((y_incr = 1) & !(b > dy)) | ((y_incr = -1) & !(b < dy))) ) {
                    do Screen.drawPixel( x1+a, y1+b );
                    if( adyMinusbdx < 0 ) {
                        let a = a + 1;
                        let adyMinusbdx = adyMinusbdx + (dy*y_incr);
                    }
                    else {
                        let b = b + y_incr;
                        let adyMinusbdx = adyMinusbdx - dx;
                    }
                }
                return 0;
            }

            function void drawVerticalLine( int x, int y1, int y2 ) {
                var int temp;
                
                if( y1 > y2 ) {
                    let temp = y1;
                    let y1 = y2;
                    let y2 = temp;
                }
                
                while( !(y1 > y2) ) {
                    do Screen.drawPixel( x, y1 );
                    let y1 = y1 + 1;
                }
                return 0;
            }

            function void drawHorizontalLine( int x1, int x2, int y ) {
                var int start_addr, end_addr, screen;
                var int x1mod16, x2mod16;

                let screen = 16384;
                
                let x1mod16 = x1 & 15;
                let x2mod16 = x2 & 15;
                let start_addr = (y*32) + (x1/16);
                let end_addr = (y*32) + (x2/16) + (x2mod16=0);

                if( start_addr = end_addr ) {   
                    do Screen.draw_short_horizontal_line( x1, x2, y );
                }
                else { 
                    if( !(x1mod16 = 0) ) {      
                        let start_addr = start_addr + 1;
                        do Screen.draw_short_horizontal_line( x1, x1+16-x1mod16, y );
                    }
                    if( !(x2mod16 = 0) ) {     
                        let end_addr = end_addr - 1;
                        do Screen.draw_short_horizontal_line( x2-x2mod16, x2, y );
                    }
                    while( !(start_addr > end_addr) ) {     
                        let screen[start_addr] = true;
                        let start_addr = start_addr + 1;
                    }
                }
                
                return 0;
            }
            
            function void draw_short_horizontal_line( int x1, int x2, int y ) {
                while( !(x1 > x2) ) {
                    do Screen.drawPixel( x1, y );
                    let x1 = x1 + 1;
                }
            
                return 0;
            }

            function void drawRectangle(int x1, int y1, int x2, int y2) {
                var int y;
                
                let y = y1;
                while( !(y > y2) ) {
                    do Screen.drawHorizontalLine(x1, x2, y);
                    let y = y + 1;
                }
                return 0;
            }


            
        }
    """

    return jack_code + screen_library

def add_libraries_to_jack_code(jack_code):
    jack_code = add_math_libary(jack_code)
    jack_code = add_screen_library(jack_code)
    return jack_code