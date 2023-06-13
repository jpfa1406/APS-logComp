class funcTable:
    funcDict = {}

    @staticmethod
    def create(iden, value):
        if iden in funcTable.funcDict:
            raise Exception("")
        else:
            funcTable.funcDict[iden] = value

    @staticmethod
    def get(iden):
        return funcTable.funcDict[iden]
    
    @staticmethod
    def set(iden, value):
        funcTable.funcDict[iden] = value