#! /usr/bin/env python

# Chesksum class

import sys

class Checksum():
    # Initializing the class, it needs the packet Name 
    def __init__(self, packNam):
        self.PacketName = packNam
        self.FieldName = []
    # Adding a field name
    def addFieldName(self, fn):
        self.FieldName.append(fn)
    # Adding a relationship as long as it is not in the list
    def addRelationship(self, fn):
        if not fn in self.FieldName:
            self.addFieldName(fn)
        
    # Removing a relationship if it is in the list
    def removeRelationship(self, fn):
        if fn in self.FieldName:
            x = self.FieldName.index(fn)
            
            del self.FieldName[x]

    # For testing print a
    def testPrint(self):
        print(self.PacketName)
        print(self.FieldName)

chk = Checksum("test")
print chk.testPrint()
chk.addRelationship("123")
chk.addRelationship("234")
chk.addRelationship("456")
chk.testPrint()
chk.removeRelationship("no")
chk.testPrint()
print("Done")
