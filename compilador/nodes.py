from abc import ABC, abstractmethod
from typing import List
import funcTable
import symbolTable

class Node(ABC):
    def __init__(self, value, children):
        self.value = value
        self.children: List[Node] = children
    @abstractmethod    
    def evaluate(self, st):
        pass
    
class UnOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def evaluate(self, st):
    #     print("causa", self.children[0])
    #     print("problema" , self.children[0].evaluate(st)[0])
        valor = self.children[0].evaluate(st)[1]
        if self.children[0].evaluate(st)[0] == "Int":
            if self.value == '-':
                return ("Int", -valor)
            elif self.value == '!':
                return ("Int", not(valor))
            return ("Int", valor)
        elif self.children[0].evaluate(st)[0] == "Str":
            return ("Str", valor)
    
class BinOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def evaluate(self, st):
        valor1 = self.children[0].evaluate(st)[1]
        valor2 = self.children[1].evaluate(st)[1]
        result = ()
        if (self.children[0].evaluate(st)[0] == "Str") or (self.children[1].evaluate(st)[0] == "Str"): #operacao string 
            if self.value == '.':
                result = ("Str", str(valor1) + str(valor2))
            elif self.value == '>':
                result = ("Str", int(valor1 > valor2))
            elif self.value == '<':
                result = ("Str", int(valor1 < valor2))
            elif self.value == "==":
                result = ("Str", int(str(valor1) == str(valor2)))
            return result
        if (self.children[0].evaluate(st)[0] == "Int") and (self.children[1].evaluate(st)[0] == "Int"): #operacao int
            if self.value == '+':
                result = ("Int", valor1 + valor2)
            elif self.value == '-':
                result = ("Int", valor1 - valor2)
            elif self.value == '*':
                result = ("Int", valor1 * valor2)
            elif self.value == '/':
                result = ("Int", valor1 // valor2)
            elif self.value == "==":
                result = ("Int", int(valor1 == valor2))
            elif self.value == "<":
                result = ("Int", int(valor1 < valor2))
            elif self.value == ">":
                result = ("Int", int(valor1 > valor2))
            elif self.value == "||":
                result = ("Int", int(valor1 | valor2))
            elif self.value == "&&":
                result = ("Int", int(valor1 & valor2))
            elif self.value == '.':
                result = ("Str", str(valor1) + str(valor2))
            return result
        
class IntVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def evaluate(self, st):
        return ("Int", self.value)
    
class StrVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def evaluate(self, st):
        return ("Str", self.value)
    
class Block(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def evaluate(self, st):
        for i in self.children:
            if i.value != "RET":
                i.evaluate(st)
            else:
                return i.evaluate(st)

class Indent(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def evaluate(self, st):
        return st.get(self.value)

class Assingment(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def evaluate(self, st):
        child = self.children[1].evaluate(st)
        if st.get(self.children[0].value)[0] == child[0]:
            st.set(self.children[0].value, child)
        else:
            raise Exception()

class Print(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def evaluate(self, st):
        #print(self.children[0])
        print(self.children[0].evaluate(st)[1])

class If(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def evaluate(self, st):
        if self.children[0].evaluate(st):
            self.children[1].evaluate(st)
        else:
            self.children[2].evaluate(st)

class While(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def evaluate(self, st):
        while self.children[0].evaluate(st)[1]:
            self.children[1].evaluate(st)

class Read(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def evaluate(self, st):
        return ("Int", int(input()))
    
class VarDec(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def evaluate(self, st):
        st.create(self.children[0].value, (self.value, self.children[1].evaluate(st)[1]))

class FuncDec(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def evaluate(self, st):
        funcTable.funcTable.create(self.children[0].value, self)

class FuncCall(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def evaluate(self, st):
        func = funcTable.funcTable.get(self.value)
        symbol_table = symbolTable.SymbolTable()
        for i in func.children[1]:
            i.evaluate(symbol_table)

        for i, j in enumerate(self.children[0]):
            symbol_table.set(func.children[1][i].children[0].value, j.evaluate(st))

        ret = func.children[-1].evaluate(symbol_table)
        return ret

class ret(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def evaluate(self, st):
        #print("ret", self.children[0].evaluate(st))
        return self.children[0].evaluate(st)
    
class NoOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def evaluate(self, st):
        pass