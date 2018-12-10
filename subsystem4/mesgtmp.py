#! /usr/bin/env python

# Message Template

import sys

class MessageTemplate():
    # Initializing the class 
    def __init__(self, mtn, dfn, dfp, of):
        self.msgTemplateName = mtn
        self.destFolderName = dfn
        self.destFolderPath = dfp
        self.outputFormat = of
                            
    # Getting Field Length Dependancy
    def collectFLD(self):
        # Collect value from FLD
    # Getting Packet Length Dependency
    def collectPLD(self):
        # Collect value from PLD
    # Getting Checksum
    def collectCksm(self):
        # Collecting value from checksum
    # Getting the Field Equivelance
    def collectFE(self):
        # Collecting FE
    # Adding a relationship
    def generateCode(self):
        # generate the code somehow

    
