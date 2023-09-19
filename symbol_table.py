


class symboltable:
    def __init__(self):
        self.symbol_hashmap = {}

        # Varaibles below are needed to keep track and count the number of varaible
        self.static_index = 0 
        self.field_index = 0
        self.arg_index = 0
        self.var_index = 0

    # Incremenrts and returns the variable counter of 
    def increment_variable_counter(self, kind):
        if (kind == "static"):
            self.static_index+=1
            return self.static_index-1
        elif (kind == "field"):
            self.field_index+=1
            return self.field_index-1
        elif (kind == "arg"):
            self.arg_index+=1
            return self.arg_index-1
        elif (kind == "var"):
            self.var_index+=1
            return self.var_index-1
        else:
            raise Exception("unknown kind", kind)
    
    # Defines a new identifier with name, type and kind
    def define(self, name, type_, kind):
        if (name in self.symbol_hashmap):
            raise Exception("Symbol already encountered", name)
        
        if (kind not in ["static", "field", "arg", "var"]):
            raise Exception("unknown kind", kind)

        index = self.increment_variable_counter(kind)

        self.symbol_hashmap[name] = (type_, kind, index)
        
    # Returns the kind of variable if it exists
    def kind_of(self, name):
        if (name not in self.symbol_hashmap):
            raise Exception("identifer not defined in symbolname", name)
        
        type_, kind, index = self.symbol_hashmap[name]

        return kind
    
    def type_of(self, name):
        if (name not in self.symbol_hashmap):
            raise Exception("identifer not defined in symbolname", name)
        
        type_, kind, index = self.symbol_hashmap[name]

        return type_
    
    def index_of(self, name):
        if (name not in self.symbol_hashmap):
            raise Exception("identifer not defined in symbolname", name)
        
        type_, kind, index = self.symbol_hashmap[name]

        return index
