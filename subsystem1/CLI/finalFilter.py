
#filter object, used to filter out protocol fields
class filter:

    #New filter object as defined within the srs
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def getName(self):
        return self.name

    def getExpression(self):
        return self.expression

    def editName(self,newName):
        self.name = newName

    def editExpression(self, newExpression):
        self.expression = newExpression


