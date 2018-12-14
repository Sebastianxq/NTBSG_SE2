
class Field:
    
    def __init__(self,fName,fSName,fPosition,fSize,fValue,fShow):
        self.fieldName = fName
        self.fieldShowName = fSName
        self.fieldPosition = fPosition
        self.fieldSize = fSize
        self.fieldValue = fValue
        self.fieldShow = fShow
    
    def getFieldName(self):
        return self.fieldName
    def getFieldShowName(self):
        return self.fieldShowName
    def getFieldPosition(self):
        return self.fieldPosition
    def getFieldSize(self):
        return self.fieldSize
    def getFieldValue(self):
        return self.fieldValue
    def getFieldShow(self):
        return self.fieldShow 
    
    def setFieldName(self,nFieldName):
        self.fieldName = nFieldName
    def setFieldShowName(self,nFieldShowName):
        self.fieldShowName = nFieldShowName
    def setFieldPosition(self,nFieldPosition):
        self.fieldPosition = nFieldPosition
    def setFieldSize(self, nFieldSize):
        self.fieldSize = nFieldSize
    def setFieldValue(self,nFieldValue):
        self.fieldValue = nFieldValue
    def setFieldShow(self,nFieldShow):
        self.fieldShow = nFieldShow 