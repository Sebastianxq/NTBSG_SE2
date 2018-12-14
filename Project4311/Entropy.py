class calculateEntropy:
    def __init__(self, uniqueValues, numberOfPackets):
        self.uniqueValues = uniqueValues
        self.numberOfPackets = numberOfPackets
        
    def funcDiv(self):
        temp = (int)(self.uniqueValues/self.numberOfPackets)
        return temp

#p1 = calculateEntropy(5,5)
#print(p1.funcDiv())