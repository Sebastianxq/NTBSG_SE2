class packet:
    def __init__(self, packetName, packetSize):
        self.packetName = packetName
        self.packetSize = packetSize
        
    def getPacketName(self):
        return self.packetName
    
    def getPacketSize(self):
        temp = (int)(self.packetSize)
        return temp
    
tempName = raw_input("Please enter packet name: ")
tempSize = int(raw_input("Please enter packet size: "))

p1 = packet(tempName,tempSize)

p1.getPacketName()

p1.getPacketSize()
        