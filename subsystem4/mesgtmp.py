#! /usr/bin/env python

# Message Template

import sys
from fieldLengthD import FieldLengthDependency 
from packetLengthD import PacketLengthDependency
from fieldEquv import FieldEquivelancy

class MessageTemplate():
    # Initializing the class needs the name, foldername, pathname, and output format
    def __init__(self, mtn, dfn, dfp, of):
        self.msgTemplateName = mtn
        self.destFolderName = dfn
        self.destFolderPath = dfp
        self.outputFormat = of
        self.targetPacketLD = ""
        self.sourcePacketLD = ""
        self.chksum = ""
        self.fieldEQ = ""
        self.sourcePacketName = ""
        self.targetPacketName = ""
        self.sourcePL = 0
        self.targetPL = 0
        self.fieldLD = ""
        self.SourceFieldList = []
        self.SourceFieldLenL = []
        self.TargetFieldList = []
        self.TargetFieldLneL = []
        self.Dic = {}
        self.count = 0

    # Get instance data
    def __eq__(self, other):
        if isinrance(other, str):
            return self._data == other
                            
    # Getting Field Length Dependancy from controller
    def collectFLD(self, fld):
        self.fieldLD = fld
        
    # Getting Packet Length Dependency
    def collectPLD(self, spld, tpld):
        self.sourcePacketLD = spld
        self.targetPacketLD = tpld
        self.sourcePacketName = spld.PacketName
        self.targetPacketName = tpld.PacketName
        self.sourcePL = spld.detDependency()
        self.targetPL = tpld.detDependency()
        self.sourceFieldList = spld.FieldName
        self.sourceFieldLenL = spld.FieldLength
        self.targetFieldList = tpld.FieldName
        self.targetFieldLenL = tpld.FieldLength
    
    # Getting Checksum
    def collectCksm(self, chk):
        self.chksum = chk
        
    # Getting the Field Equivelance
    def collectFE(self, fe):
        self.fieldEQ = fe

    # Increment count by one
    def inc(self):
        self.count+=1

    # Initializing dictionary
    def initDic(self):
        self.Dic[self.count] = "#! /usr/bin/env python"
        self.inc()
        self.Dic[self.count] = ""
        self.inc()
        self.Dic[self.count] ="import Scapy"
        self.inc()
        self.Dic[self.count] = ""
        self.inc()
        
    
    # Creating the code into dictionary
    def generateCode(self):
        self.initDic()
        spn = self.sourcePacketName
        tpn = self.targetPacketName
        # create the packets for source as a class
        lin = ""
        lin = "class SourcePacket(Packet):" 
        self.Dic[self.count] = lin
        self.inc()
        self.Dic[self.count] = ""
        self.inc()
        lin = '\tname = "%s"' % spn
        self.Dic[self.count] = lin
        self.inc()
        lin = '\tlen = "%s"' % self.sourcePL
        self.Dic[self.count] = lin
        self.inc()
        lin = '\tsrc = "127.0.0.1"' 
        self.Dic[self.count] = lin
        self.inc()
        lin = '\tdst = "1.1.1.1"'
        self.Dic[self.count] = lin
        self.inc()
        lin = '\tfields_desc = [ ShortField("%s", %d))' % (self.sourceFieldList[0], self.sourceFieldLenL[0])
        self.Dic[self.count] = lin
        self.inc()
        lin = ""
        self.Dic[self.count] = lin
        self.inc()
        lin = '\t@class method'
        self.Dic[self.count] = lin
        self.inc()
        lin = "\tdef add_ShortField(cls, name, value):"
        self.Dic[self.count] = lin
        self.inc()
        lin = "\t\tcls.fields_desc.append(ShortField(name, value))"
        self.Dic[self.count] = lin
        self.inc()
        lin = ""
        self.Dic[self.count] = lin
        self.inc()

        # Code for the target class
        lin = "class TargerPacket(Packet):" 
        self.Dic[self.count] = lin
        self.inc()
        self.Dic[self.count] = ""
        self.inc()
        lin = '\tname = "%s"' % tpn
        self.Dic[self.count] = lin
        self.inc()
        lin = '\tlen = "%s"' % self.targetPL
        self.Dic[self.count] = lin
        self.inc()
        lin = '\tsrc = "1.1.1.1"' 
        self.Dic[self.count] = lin
        self.inc()
        lin = '\tdst = "127.0.0.1"'
        self.Dic[self.count] = lin
        self.inc()
        lin = '\tfields_desc = [ ShortField("%s", %d))' % (self.sourceFieldList[0], self.sourceFieldLenL[0])
        self.Dic[self.count] = lin
        self.inc()
        lin = ""
        self.Dic[self.count] = lin
        self.inc()
        lin = '\t@class method'
        self.Dic[self.count] = lin
        self.inc()
        lin = "\tdef add_ShortField(cls, name, value):"
        self.Dic[self.count] = lin
        self.inc()
        lin = "\t\tcls.fields_desc.append(ShortField(name, value))"
        self.Dic[self.count] = lin
        self.inc()
        lin = ""
        self.Dic[self.count] = lin
        self.inc()

        # Add all additional fields to source
        for x in range(1, len(self.sourceFieldList)):
            lin = "SourcePaacket.add_ShortFields('%s', %d)" % (self.sourceFieldList[x], self.sourceFieldLenL[x])
            self.Dic[self.count] = lin
            self.inc()

        # Add all additional fields to target
        for x in range(1, len(self.targetFieldList)):
            lin = "SourcePaacket.add_ShortFields('%s', %d)" % (self.targetFieldList[x], self.targetFieldLenL[x])
            self.Dic[self.count] = lin
            self.inc()

        # Create the actual packets
        lin = "source = SourcePacket()"
        self.Dic[self.count] = lin
        self.inc()
        lin = "target = TargetPackets()"
        self.Dic[self.count] = lin
        self.inc()

    # Return the completed code
    def retCode(self):
        return self.Dic
    # Test print
    def testPrint(self):
        print("Msg Template name is %s" % self.msgTemplateName)
        print("Destination folder name is %s" % self.destFolderName)
        print("Dest folder path is %s " % self.destFolderPath)
        print("Output format is %s " % self.outputFormat)
        print self.Dic
    
    # Test print the dictionary
    def dicPrint(self):
        for key, val in self.Dic.items():
            print key, " ", val

mt = MessageTemplate("test.py", "test", "/test", "scapy")
mt.testPrint()
fl = FieldLengthDependency("source", "target")
fl.addSourceLen(2)
fl.addTargetLen(4)
mt.collectFLD(fl)
source = PacketLengthDependency("source")
source.addDependency("123", 3)
target = PacketLengthDependency("target")
target.addDependency("456", 3)
mt.collectPLD(source, target)
mt.generateCode()
mt.testPrint()
mt.dicPrint()
