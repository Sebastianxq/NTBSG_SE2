#! /usr/bin/env python

# Packet Length Dependency class 

import sys

class PacketLengthDependency():
    # Initializing the class 
    def __init__(self, pn):
        self.PacketName = pn
        self.FieldName = []
        self.FieldLength = []
    
    

    # Adding a field name to the list
    def addFieldName(self, fn, flen):
        self.FieldName.append(fn)
        self.FieldLength.append(flen)

    # Adding a relationship as long as its not on the list
    def addDependency(self, fn, flen):
        if not fn in self.FieldName:
            self.addFieldName(fn, flen)
            
    # Return packet ld
    def givePN(self):
        return self.PacketName 

    # Removing a relationship if it is in the list
    def removeDependency(self, fn):
        if fn in self.FieldName:
            x = self.FieldName.index(fn)
            del self.FieldName[x]
            del self.FieldLength[x]

    # Calculate packet length by adding all of the dependent field lengths
    def detDependency(self):
        sum = 0
        for x in range(0, len(self.FieldLength)):
            sum += self.FieldLength[x]
        return sum

    # For testing print
    def testPrint(self):
        print(self.PacketName)
        print(self.FieldName)
        print(self.FieldLength)
        print(self.detDependency())

#pl = PacketLengthDependency("test")
#pl.testPrint()
#pl.addDependency("123", 3)
#pl.addDependency("234", 1)
#pl.addDependency("455", 3)
#pl.testPrint()
#pl.removeDependency("no")
#pl.testPrint()
#pl.removeDependency("123")
#pl.testPrint()
