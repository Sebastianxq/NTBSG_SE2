from Entropy import calculateEntropy

class field:
    def __init__(self, fieldName, fieldShowName, fieldPosition, fieldSize, fieldValue, fieldShow):
        self.fieldName = fieldName
        self.fieldShowName = fieldShowName
        self.fieldPosition = fieldPosition
        self.fieldSize = fieldSize
        self.fieldValue = fieldValue
        self.fieldShow = fieldShow
        
    def editFieldName(self):
        self.fieldName = raw_input("Edit field Name: ")
        
    def editFieldShowName(self):
        self.fieldShowName = raw_input("Edit field show name: ")
        
    def editFieldPosition(self):
        self.fieldPosition = raw_input("Edit field position: ")
        
    def editFieldSize(self):
        self.fieldSize = raw_input("Edit field size: ")
        
    def editFieldValue(self):
        self.fieldValue = raw_input("Edit field value: ")
        
    def editFieldShow(self):
        self.fieldShow = raw_input("Edit field show: ")
        
    def printVal(self):
        temp = self.fieldName
        print(temp)
        

tempName = raw_input("Enter field name: ")
tempSName = raw_input("Enter field show name: ")
tempPosition = int(raw_input("Enter field position: "))
tempSize = int(raw_input("Enter field size: "))
tempValue = int(raw_input("Enter field value: "))
tempShow = int(raw_input("Enter field show: "))

fieldCom = field(tempName,tempSName,tempPosition,tempSize,tempValue,tempShow)

fieldCom.editFieldName()

fieldCom.editFieldShowName()

fieldCom.editFieldPosition()

fieldCom.editFieldSize()

fieldCom.editFieldValue()

fieldCom.editFieldShow()

fieldCom.printVal()

ent = calculateEntropy(tempValue,tempShow)

print(ent)

        
    