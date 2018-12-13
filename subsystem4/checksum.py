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
            self.addFieldName(self, fn)

    # Removing a relationship if it is in the list
    def removeRelationship(self, fn):
        for fn in self.FieldName:
            self.FieldName.remove(fn)

                      
