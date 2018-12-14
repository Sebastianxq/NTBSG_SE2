#! /usr/bin/env python

# Field Equivelancy class

import sys

class FieldEquivelancy():
    # Initializing the class with source and target field names and the message types
    def __init__(self, sfn,  smt, tfn, tmt):
        self.SourceFN = sfn
        self.TargetFN = tfn
        self.SourceMT = smt
        self.TargetMT = tmt
        
    # Adding a new source
    def addSource(self, smt, sfn):
        self.SourceMT = smt
        self.SourceFN = sfn

    # Adding a new target
    def addTarget(self, tmt, tfn):
        self.TargetMT = tmt
        self.TargetFN = tfn

    # Removing target
    def removeSource(self):
        self.SourceMT = self.SourceFN = ""

    # Remove source
    def removeTarget(self):
        self.TargetMT = self.TargetFN = ""

    
    #Determine relationship return appropiate mt
    def detEquivelance(self):
        if (not self.SourceMT == self.TargetMT):
            self.SourceMT = self.TargetMT
        return self.SourceMT

    # Testing print method
    def testPrint(self):
        print("Source field name is %s" % (self.SourceFN))
        print("Source Message type is %s" % (self.SourceMT))
        print("Target field name is %s" % (self.TargetFN))
        print("Target Message Type is %s" % (self.TargetMT))
        print("Equivelance is %s" % (self.detEquivelance()))


fe = FieldEquivelancy("source", "type1", "target", "type2")
fe.testPrint()
fe.testPrint()
fe.removeTarget()
fe.testPrint()
fe.testPrint()
fe.removeSource()
fe.testPrint()
fe.testPrint()
fe.addTarget("target", "type1")
fe.testPrint()
fe.testPrint()
fe.addSource("source", "type2")
fe.testPrint()
fe.testPrint()
