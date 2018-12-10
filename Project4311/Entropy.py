# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:18:16 2018

@author: peter
"""

class calculateEntropy:
    def __init__(self, uniqueValues, numberOfPackets):
        self.uniqueValues = uniqueValues
        self.numberOfPackets = numberOfPackets
        
    def funcDiv(self):
        temp = self.uniqueValues/self.numberOfPackets
        return temp

p1 = calculateEntropy(5,5)
print(p1.funcDiv())