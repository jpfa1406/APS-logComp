# -*- coding: utf-8 -*-
import sys
import re
import nodes as nd
import symbolTable

#https://regex101.com/r/sCzB1d/1

class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

class PrePro:
    def __init__(self, source):
        self.source = source
    
    def filter(self):
        return re.sub(r'( *)#(.*)', '', self.source)
   
class Tokenizer:
    def __init__(self, source, position, nextToken):
        self.source = source
        self.position = position
        self.nextToken = None

    def selectNext(self):
        word = ''
        if self.position >= len(self.source):
            self.nextToken = Token("EOF", None)
            return
        
        while((self.source[self.position] == ' ') or (self.source[self.position] == '\n')):
                self.position += 1
                if self.position >= len(self.source):
                    self.nextToken = Token("EOF", None)
                    return


        if (self.source[self.position]).isdigit():
            while ((self.position < len(self.source)) and (self.source[self.position]).isdigit()):
                word += self.source[self.position]
                self.position += 1
            self.nextToken = Token("INT", int(word))
            return
        elif (self.source[self.position]).isalpha():
            while ((self.position < len(self.source)) and ((self.source[self.position]).isdigit() or (self.source[self.position]).isalpha() or (self.source[self.position] == '_'))):
                word += self.source[self.position]
                self.position += 1
            if word == "print":
                self.nextToken = Token("PRINT", word)
            elif word == "if":
                self.nextToken = Token("IF", None)
            elif word == "while":
                self.nextToken = Token("WHILE", None)
            elif word == "else":
                self.nextToken = Token("ELSE", None)
            elif word == "end":
                self.nextToken = Token("END", None)
            elif word == "readin":
                self.nextToken = Token("READ", None)
            elif word == "Int":
                self.nextToken = Token("TYPE", "Int")
            elif word == "String":
                self.nextToken = Token("TYPE", "Str")
            elif word == "func":
                self.nextToken = Token("FUNC", None)
            elif word == "return":
                self.nextToken = Token("RET", None)    
            else:
                self.nextToken = Token("IDENT", word)
            return
        else:            
            if self.source[self.position] == '+':
                self.nextToken = Token("PLUS", "+")
                self.position += 1
                return
            elif self.source[self.position] == '-':
                self.nextToken = Token("MINUS", "-")
                self.position += 1
                if self.source[self.position] == '>':
                    self.nextToken = Token("ON", "->")
                    self.position += 1
                    return
                return
            elif self.source[self.position] == '*':
                self.nextToken = Token("MULT", "*")
                self.position += 1
                return
            elif self.source[self.position] == '/':
                self.nextToken = Token("DIVIDE", "/")
                self.position += 1
                return
            elif self.source[self.position] == '(':
                self.nextToken = Token("PARA1", "(")
                self.position += 1
                return
            elif self.source[self.position] == ')':
                self.nextToken = Token("PARA2", ")")
                self.position += 1
                return
            elif self.source[self.position] == '{':
                self.nextToken = Token("CHAVE1", "{")
                self.position += 1
                return
            elif self.source[self.position] == '}':
                self.nextToken = Token("CHAVE2", "}")
                self.position += 1
                return
            elif self.source[self.position] == '<':
                self.nextToken = Token("LESST", "<")
                self.position += 1
                if self.source[self.position] == '-':
                    self.nextToken = Token("IN", "<-")
                    self.position += 1
                    return
                return
            elif self.source[self.position] == '>':
                self.nextToken = Token("MORET", ">")
                self.position += 1
                return
            elif self.source[self.position] == '|':
                self.position += 1
                if self.source[self.position] == '|':
                    self.nextToken = Token("OR", "||")
                    self.position += 1
                    return
            elif self.source[self.position] == '&':
                self.position += 1
                if self.source[self.position] == '&':
                    self.nextToken = Token("AND", "&&")
                    self.position += 1
                    return
            elif self.source[self.position] == '=':
                self.nextToken = Token("EQUAL", "=")
                self.position += 1
                if self.source[self.position] == '=':
                    self.nextToken = Token("ISEQUAL", "==")
                    self.position += 1
                    return
                return
            elif self.source[self.position] == '!':
                self.nextToken = Token("NOT", "!")
                self.position += 1
                return
            elif self.source[self.position] == '"':
                self.nextToken = Token("QMARKS", None)
                self.position += 1
                return
            elif self.source[self.position] == '.':
                self.nextToken = Token("DOT", '.')
                self.position += 1
                return
            elif self.source[self.position] == ',':
                self.nextToken = Token("COMMA", ',')
                self.position += 1
                return
            elif self.source[self.position] == ';':
                self.nextToken = Token("SEMICOLON", ';')
                self.position += 1
                return
    
class Parser:
    def parseStatement():
        token = Parser.tokenizer.nextToken 
        #print(Parser.tokenizer.nextToken.tipo)  
        if token.tipo == "IDENT":
            variable = nd.Indent(token.valor,[])
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.nextToken.tipo == "IN":
                Parser.tokenizer.selectNext()
                #return nd.Assingment(None, [variable, Parser.parseRealExpression()]) 
                if Parser.tokenizer.nextToken.tipo == "PARA1":
                    Parser.tokenizer.selectNext()
                    tipo = Parser.tokenizer.nextToken
                    Parser.tokenizer.selectNext()
                    if tipo.valor == "String":
                        if Parser.tokenizer.nextToken.tipo == "PARA2":
                            Parser.tokenizer.selectNext()
                            return nd.VarDec(tipo.valor, [variable, nd.StrVal("",[])])    
                    elif tipo.valor == "Int":
                        if Parser.tokenizer.nextToken.tipo == "PARA2":
                            Parser.tokenizer.selectNext()
                            return nd.VarDec(tipo.valor, [variable, nd.IntVal(0,[])])
                    else:
                        raise Exception()    
                return nd.Assingment(None, [variable, Parser.parseRealExpression()])        
            elif Parser.tokenizer.nextToken.tipo  == "PARA1":
                args = []
                Parser.tokenizer.selectNext()
                while Parser.tokenizer.nextToken.tipo != "PARA2":
                    args.append(Parser.parseRealExpression())
                    if Parser.tokenizer.nextToken.tipo == "COMMA":
                        Parser.tokenizer.selectNext()
                Parser.tokenizer.selectNext()
                return nd.FuncCall(variable.value, [args])
        elif token.tipo == "PRINT":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.nextToken.tipo  == "PARA1":
                Parser.tokenizer.selectNext()
                realExpress = nd.Print("",[Parser.parseRealExpression()])
                token = Parser.tokenizer.nextToken
                if token.tipo == "PARA2":
                    Parser.tokenizer.selectNext()
                else:
                    raise Exception(("não fechou ()"))  
                return realExpress
            else:
                 raise Exception(("não abriu ()"))
        elif token.tipo == "WHILE":
            Parser.tokenizer.selectNext()
            realExpress = Parser.parseRealExpression()
            if Parser.tokenizer.nextToken.tipo == "NEXT":
                Parser.tokenizer.selectNext()
                blocks = []
                while Parser.tokenizer.nextToken.tipo != "END":
                    blocks.append(Parser.parseStatement())
                Parser.tokenizer.selectNext()
                return nd.While(None, [realExpress, nd.Block(None, blocks)])
        elif token.tipo == "IF":
            Parser.tokenizer.selectNext()
            realExpress = Parser.parseRealExpression()
            if Parser.tokenizer.nextToken.tipo == "CHAVE1":
                Parser.tokenizer.selectNext()
                blocks1 = []
                blocks2 = []
                while True:
                    cmd = Parser.parseStatement()
                    if Parser.tokenizer.nextToken.tipo == 'SEMICOLON':
                        Parser.tokenizer.selectNext()
                        blocks1.append(cmd)
                    if Parser.tokenizer.nextToken.tipo == "CHAVE2":
                        Parser.tokenizer.selectNext()
                        break
                if Parser.tokenizer.nextToken.tipo == "ELSE":
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.nextToken.tipo == "CHAVE1":
                        Parser.tokenizer.selectNext()
                        while Parser.tokenizer.nextToken.tipo != "CHAVE2":
                            cmd = Parser.parseStatement()
                            if Parser.tokenizer.nextToken.tipo == 'SEMICOLON':
                                Parser.tokenizer.selectNext()
                                blocks2.append(cmd)
                Parser.tokenizer.selectNext()
                return nd.If(None, [realExpress, nd.Block(None, blocks1), nd.Block(None, blocks2)])
            else:
                raise Exception()
        elif token.tipo == "FUNC":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.nextToken.tipo == "IDENT":
                name = nd.Indent(Parser.tokenizer.nextToken.valor,[])
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.nextToken.tipo == "PARA1":
                    Parser.tokenizer.selectNext()
                    args = []
                    while Parser.tokenizer.nextToken.tipo != "PARA2":
                        if Parser.tokenizer.nextToken.tipo == "IDENT":
                            variable = nd.Indent(Parser.tokenizer.nextToken.valor,[])
                            Parser.tokenizer.selectNext()
                            if Parser.tokenizer.nextToken.tipo == "PARA1":
                                Parser.tokenizer.selectNext()
                                tipo = Parser.tokenizer.nextToken
                                Parser.tokenizer.selectNext()
                                if tipo.valor == "Str":
                                    if Parser.tokenizer.nextToken.tipo == "PARA2":
                                        Parser.tokenizer.selectNext()
                                        args.append(nd.VarDec(tipo.valor, [variable, nd.StrVal("",[])]))
                                elif tipo.valor == "Int":
                                    if Parser.tokenizer.nextToken.tipo == "PARA2":
                                        Parser.tokenizer.selectNext()
                                        args.append(nd.VarDec(tipo.valor, [variable, nd.IntVal(0 ,[])]))
                                else:
                                    raise Exception()
                                if Parser.tokenizer.nextToken.tipo == "COMMA":
                                    Parser.tokenizer.selectNext()
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.nextToken.tipo == "ON":
                        Parser.tokenizer.selectNext()
                        if Parser.tokenizer.nextToken.tipo == "CHAVE1":
                            Parser.tokenizer.selectNext()
                            blocks = []
                            while Parser.tokenizer.nextToken.tipo != "CHAVE2":
                                cmd = Parser.parseStatement()
                                #print('akiiiiiii',cmd,Parser.tokenizer.nextToken.tipo)
                                if Parser.tokenizer.nextToken.tipo == 'SEMICOLON':
                                    Parser.tokenizer.selectNext()
                                    blocks.append(cmd)
                            Parser.tokenizer.selectNext()
                            if Parser.tokenizer.nextToken.tipo == 'PARA1':
                                Parser.tokenizer.selectNext()
                                if Parser.tokenizer.nextToken.tipo == 'TYPE':
                                    tipo = Parser.tokenizer.nextToken.valor
                                    Parser.tokenizer.selectNext()
                                    if Parser.tokenizer.nextToken.tipo == "PARA2":
                                        Parser.tokenizer.selectNext()
                                        #print(blocks)
                                        return nd.FuncDec(tipo, [name, args, nd.Block(None, blocks)])                                            
        elif token.tipo == "RET":
            Parser.tokenizer.selectNext()
            return nd.ret("RET", [Parser.parseRealExpression()])
        else:
            raise Exception("token ", Parser.tokenizer.nextToken.tipo , " invalido")

    def parseBlock():
        blocks = []
        while Parser.tokenizer.nextToken.tipo != "EOF":
            cmd = Parser.parseStatement()
            if Parser.tokenizer.nextToken.tipo == 'SEMICOLON':
                Parser.tokenizer.selectNext()
                blocks.append(cmd)
            else:
                raise Exception()
        return nd.Block(None, blocks)
        
    def parseRealExpression():
        express = Parser.parseExpression()
        token = Parser.tokenizer.nextToken
        while Parser.tokenizer.nextToken.tipo == "ISEQUAL" or Parser.tokenizer.nextToken.tipo == "LESST" or Parser.tokenizer.nextToken.tipo == "MORET":
            token = Parser.tokenizer.nextToken
            Parser.tokenizer.selectNext()
            express = nd.BinOp(token.valor, [express, Parser.parseExpression()])
            token = Parser.tokenizer.nextToken
        return express
    
    def parseExpression():
        termo = Parser.parseTerm()
        token = Parser.tokenizer.nextToken
        while Parser.tokenizer.nextToken.tipo == "PLUS" or Parser.tokenizer.nextToken.tipo == "MINUS" or Parser.tokenizer.nextToken.tipo == "OR":
            token = Parser.tokenizer.nextToken
            Parser.tokenizer.selectNext()
            termo = nd.BinOp(token.valor, [termo, Parser.parseTerm()])
            token = Parser.tokenizer.nextToken
        return termo

    def parseTerm():
        termo = Parser.parseFactor()                 
        token = Parser.tokenizer.nextToken 
        while token.tipo == "MULT" or token.tipo == "DIVIDE" or token.tipo == "AND" or token.tipo == "DOT":
            token = Parser.tokenizer.nextToken
            Parser.tokenizer.selectNext()
            termo = nd.BinOp(token.valor, [termo, Parser.parseFactor()])
            token = Parser.tokenizer.nextToken
        return termo

    
    def parseFactor():
        token = Parser.tokenizer.nextToken 
        if token.tipo == "INT":
            factor = nd.IntVal(token.valor, [])
            Parser.tokenizer.selectNext()
            return factor
        elif token.tipo == "QMARKS":
            Parser.tokenizer.selectNext()
            #print('aki', Parser.tokenizer.nextToken.valor)
            factor = nd.StrVal(Parser.tokenizer.nextToken.valor, [])
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.nextToken.tipo == "QMARKS":
                Parser.tokenizer.selectNext()
                return factor
            else:
                raise Exception(("não fechou aspas"))
        elif token.tipo == "PLUS" or token.tipo == "MINUS" or token.tipo == "NOT":
            Parser.tokenizer.selectNext()
            factor = nd.UnOp(token.valor, [Parser.parseFactor()])
            return factor
        elif token.tipo == "PARA1":
            Parser.tokenizer.selectNext()
            factor = Parser.parseRealExpression()
            token = Parser.tokenizer.nextToken
            if token.tipo == "PARA2":
                Parser.tokenizer.selectNext()
                return factor
            else:
                raise Exception(("não fechou ()"))
        elif token.tipo == "IDENT":
            Parser.tokenizer.selectNext()
            variable = nd.Indent(token.valor,[])
            factor = nd.UnOp(None, [variable])
            if Parser.tokenizer.nextToken.tipo  == "PARA1":
                args = []
                Parser.tokenizer.selectNext()
                while True:
                    if Parser.tokenizer.nextToken.tipo == "COMMA":
                        Parser.tokenizer.selectNext()
                    elif Parser.tokenizer.nextToken.tipo == "PARA2":
                        break
                    elif Parser.tokenizer.nextToken.tipo in ["IDENT", "INT", "STR"]:
                        args.append(Parser.parseRealExpression())
                    else:
                        raise Exception()
                    
                Parser.tokenizer.selectNext()
                factor = nd.FuncCall(variable.value, [args])
            return factor
        elif token.tipo == "READ":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.nextToken.tipo  == "PARA1":
                Parser.tokenizer.selectNext()
                read = nd.Read(None,[])
                token = Parser.tokenizer.nextToken
                if token.tipo == "PARA2":
                    Parser.tokenizer.selectNext()
                else:
                    raise Exception(("não fechou ()"))
                return read
            else:
                 raise Exception(("não abriu ()"))
        return

    def run(code):
        source = PrePro(code)
        limpo = source.filter()
        #print(limpo)
        Parser.tokenizer = Tokenizer(limpo, 0, None)
        Parser.tokenizer.selectNext()
        resutado = Parser.parseBlock()
        if Parser.tokenizer.nextToken.tipo != "EOF":
            raise Exception(("terminou sem EOF"))
        return resutado
    
#import funcTable
with open(sys.argv[1], "r") as f:
    st = symbolTable.SymbolTable()
    val = Parser.run(f.read())
    #print(val.children[0])
    val.evaluate(st)
    #print(funcTable.funcTable.funcDict)

    