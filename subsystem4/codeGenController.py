#! /usr/bin/env python

# Class for the controller for the code genration controller

import sys

class CodeGenController():
    # Initializing the class it takes the path, and output format
    def __init__(self, path, fileN, output):
        self.DestPath = path
        self.OutputFormat = output
        self.DestFileName = fileN
        self.sourcePN = ""
        self.targetPN = ""
        self.nodeDic = {}
    # Method for obtaining the source and destination Message types
    def getPacketNames(self, seqInfo):
        self.sourcePN = seqInfo[0]
        self.targetPN = seqInfo[1]

    # Method for obtaining the dictionary
    def getDictionary(self, dic):
        self.nodeDic = dic

    # Method for setting checksum
    def setChecksum(self):
        # Create checksum object get values

    # Method for getting packet length dependency
    def setPLD(self):
        #  Set the packet length dependencies

    # Method for setting the field length dependencies
    def setFLD(self):
        # Set the field length dependencies
    
    # Method for setting the field Equivelancies
    def setFE(self):
        # Set the field lequivelancies
        
    # Method for generating and holding the code
    def generateCode(self):
        # Pass info to generate code

    # Method for creating code file
    def exportCode(self):
        # Export and get copy of code

    
