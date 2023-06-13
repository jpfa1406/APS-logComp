class SymbolTable:
    def __init__(self):
        self.symbolDict = {}

    def create(self, iden, value):
        if iden in self.symbolDict:
            raise Exception("variavel ja declarada")
        else:
            self.symbolDict[iden] = value

    def get(self, iden):
        #print(self.symbolDict)
        return self.symbolDict[iden]
    
    def set(self, iden, value):
        self.symbolDict[iden] = value