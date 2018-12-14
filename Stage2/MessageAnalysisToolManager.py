from Packet import Packet
from Field import Field

class MessageAnalysisToolManager:
    
    def __init__(self):
        self.p = 0
    
    def newPacket(self,pName,pSize):
        return Packet(pName,pSize)