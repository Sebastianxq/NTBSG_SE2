from test.test_largefile import size

class Packet:
    
    def __init__(self,pName,pSize):
        self.packetName = pName
        self.packetSize = pSize
        
    def setPacketName(self,name):
        self.packetName = name
        
    def setPacketSize(self,size):
        self.packetSize = size
        
    def getPacketSize(self):
        return self.packetSize
    
    def getPacketName(self):
        return self.packetName
