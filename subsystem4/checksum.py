#! /usr/bin/env python

# Chesksum class

import sys

class Checksum():
    # Initializing the class 
    def __init__(self):
        self.PacketName = ""
        self.FieldName = []
    # Getting Packet name
    def getPacketName(self, pn):
        self.PacketName = pn
    # Getting add field name
    def getFieldName(self, fn):
        self.FieldName.append(fn)
    # Adding a relationship
    def addRelationship(self):
        # do something

    # Removing a relationship
    def removeRelationship(self):
        # remove something

    #Determine relationship
    def detRelationship(self):
        # calculate calculation

                      
