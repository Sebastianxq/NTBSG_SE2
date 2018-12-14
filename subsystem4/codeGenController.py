#! /usr/bin/env python

# Class for the controller for the code genration controller

import sys
from checksum import Checksum
from fieldLengthD import FieldLengthDependency
from fieldEquv import FieldEquivelancy
from packetLengthD import PacketLengthDependency
from mesgtmp import MessageTemplate

class CodeGenController():
    # Initializing the class it takes the path, and output format
    def __init__(self, path, fileN, output):
        self.DestPath = path
        self.OutputFormat = output
        self.DestFileName = fileN
        self.sourcePN = ""
        self.targetPN = ""
        self.nodeDic = {}
        self.sourceChksm = ""
        self.targetChksm = ""
        self.sourcePLD = ""
        self.targetPLD = ""
        self.MessagTmpl = ""
        self.DestFN = "test"
        self.code = {}
    # Method for obtaining the source and destination Message types
    def getPacketNames(self, seqInfo):
        self.sourcePN = seqInfo[0]
        self.targetPN = seqInfo[1]
        self.setChecksum()
        self.sourcePLD = self.setPLD(self.sourcePN)
        self.targetPLD = self.setPLD(self.targetPN)
        

    # Method for obtaining the dictionary
    def getDictionary(self, dic):
        self.nodeDic = dic
        sourceDic = self.nodeDic[self.sourcePN]
        targetDic = self.nodeDic[self.targetPN]
        flen = 0
        fn = ""
        for key, val in sourceDic.items():
            flen = val
            fn = key
            self.sourcePLD.addFieldName(fn, flen)
        for key, val in targetDic.items():
            flen = val
            fn = key
            self.targetPLD.addFieldName(fn, flen)
    # Method for setting checksum
    def setChecksum(self):
        self.sourceChksm = Checksum(self.sourcePN)
        self.targetChksm = Checksum(self.targetPN)

    # Method for getting packet length dependency
    def setPLD(self, pn):
        tmp = PacketLengthDependency(pn)
        return tmp

    # Method for setting the field length dependencies
    def setFLD(self, sfn, tfn):
        fieldLd = FieldLengthDependency(sfn, tfn)
    
    # Method for setting the field Equivelancies
    def setFE(self, sfn, smt, tfn, tmt):
        fieldLE = FieldEquivelancy(sfn, smt, tfn, tmt)
        
        
    # Method for generating and holding the code
    def generateCode(self):
        self.MessagTmpl = MessageTemplate(self.DestFileName, self.DestFN, self.DestPath, self.OutputFormat)
        self.MessagTmpl.collectPLD(self.sourcePLD, self.targetPLD)
        self.MessagTmpl.generateCode()
        self.code = self.MessagTmpl.retCode()
        
        
    # Method for creating code file
    def exportCode(self):
        self.MessagTmpl.codeFile()
        
    # Method to print test code
    def testPrint(self):
        self.MessagTmpl.testPrint()

t = CodeGenController("", "test.py", "scapy")
names = ["source", "target"]
t.getPacketNames(names)    
fdic = {
    "source1": 2,
    "source2": 2
}
tdic = {
    "target1": 2,
    "target2": 3
}
dic = {
    "source":fdic,
    "target":tdic
}
t.getDictionary(dic)
t.generateCode()
t.exportCode()
