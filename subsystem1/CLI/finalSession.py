from finalPCAP import PCAP #PCAP class obj
from finalMessageType import messageType #messageType class obj
from finalFilter import filter #filter class obj

class Session:

    #New session object as defined within the srs and sdd
    def __init__(self, name, description):
        self.SessionName = name
        self.description = description
        self.filterList = list()
        self.messageTypeList  = list()
        self.fieldList = list()

    def addPDML(self,pdmlObject):
        self.sessionPDML = pdmlObject

    def addMessageType(self,messageType):
        self.messageTypeList.append(messageType)

    def addFilter(self, filter):
        self.filterList.append(filter)

    def addField(selfself, field):
        self.fieldList.append(field)

#creates a temp pcap, pdml, filter, messageType and session Objects
testPcap = PCAP("testPcap", "no file")
pdml = testPcap.convertToPdml()
testFilter = filter("ipx only", "ipx")
testMessageType = messageType("nameIsTest","name=test")
testSession = Session("test","A session used to showcase CLI functionality")

#Binds pdml,filter and messageType to the session
testSession.addPDML(pdml)
testSession.addFilter(testFilter)
testSession.addMessageType(testMessageType)
