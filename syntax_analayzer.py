
# Given a string and the current index position inside that string 
# will advance the current position until we have reached a Non whitespace character
# returns that value
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
    return string[curr_index] in "123456789"

def handle_integer_tokenizer(string, curr_index):
    curr_token = ""
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







jack_code = """

    if(x < 153)
        {let city="Paris";}



"""



print(tokenize_jack_code(jack_code))






def is_integer_constant(cur_token):
    return cur_token.isdigit()

def xml_integer_constant(cur_token):
    print("<integerConstant>", cur_token ,"</integerConstant>")


def is_string_constant(cur_token):
    return cur_token[0] == "\"" and cur_token[-1] == "\""

def xml_string_constant(cur_token):
    print("<stringConstant>", cur_token, "</stringConstant>")

def is_identifier(cur_token):
    return cur_token[0] not in "1234567890"

def xml_identifier(cur_token):
    print("<identifier>", cur_token ,"</identifier>")

def is_keyword_constant(cur_token):
    return cur_token in ["true", "false", "null", "this"]

def xml_keyword_constant(cur_token):
    print("<KeywordConstant>", cur_token ,"</KeywordConstant>")

def is_op(cur_token):
    return cur_token in "+-*/&|<>="

def xml_op(cur_token):
    print("<op>", cur_token ,"<op>")

def is_symbol(cur_token):
    return (cur_token in "()[]}{.,;+-*/&|<>=-")

def xml_symbol(cur_token):
    print("<symbol>", cur_token, "</symbol>")

def is_keyword(cur_token):
    return cur_token in ["class", "constructor", "function", ]

