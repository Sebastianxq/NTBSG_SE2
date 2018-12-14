#! /usr/bin/env python

# Field Length Dependency class

import sys

class FieldLengthDependency():
    # Initializing the class 
    def __init__(self, sfn, tfn):
        self.SourceFN = sfn
        self.SourceLen = 0
        self.TargetFN = tfn
        self.TargetLen = 0
    # Adding a source
    def addDependencySource(self, fn):
        self.SourceFN = fn

    # Adding a target 
    def addDependencyTarget(self, fn):
        self.TargetFN = fn

    # Adding source length
    def addSourceLen(self, slen):
        self.SourceLen = slen

    # Adding target length
    def addTargetLen(self, slen):
        self.TargetLen = slen

    # Removing source
    def removeSource(self):
        self.SourceFN = ""
        self.SourceLen = 0

    #Removing target
    def removeTarget(self):
        self.TargetFN = ""
        self.TargetLen = 0

    #Determine relationship
    def detDependency(self):
        return self.TargetLen - self.SourceLen

    #Testing print
    def testPrint(self):
        print("Source fn is %s, and length %d" % (self.SourceFN, self.SourceLen))
        print("Target fn is %s, and length %d" % (self.TargetFN, self.TargetLen))
        print(self.detDependency())

#fl = FieldLengthDependency("source", "target")
#fl.testPrint() 
#fl.removeSource()
#fl.removeTarget()
#fl.addDependencySource("Source")
#fl.addDependencyTarget("Target")
#fl.testPrint()
#fl.addSourceLen(2)
#fl.addTargetLen(4)
#fl.testPrint()
#fl.removeTarget()
#fl.testPrint()
#fl.removeSource()
#fl.testPrint()
