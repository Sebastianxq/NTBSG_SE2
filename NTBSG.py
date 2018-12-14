import sys
from Helpers.pcapToPdml import *
from SequencingStageFiles.stateMachine import StateMachine
from subsystem4.codeGenController import CodeGenController
import re
#sys.argv[1] = dissectorPath
#sys.argv[2] = pcapPath
#sys.argv[3] = workspacePath
#print(sys.argv[1])
#print(sys.argv[2])
#print(sys.argv[3])

nodeList = nodeSequenceFromPDML(sys.argv[1], sys.argv[2], sys.argv[3])
fullInfo = fullInformationFromPDML(sys.argv[1], sys.argv[2], sys.argv[3])

currStateMachine = StateMachine(nodeList)

result = re.split('\\\\', sys.argv[3])
resultLength = len(result)
workspaceFolderName = result[resultLength-2]

codeGenObject = CodeGenController('', 'test.py', 'scapy')

codeGenObject.getPacketNames(nodeList)

codeGenObject.getDictionary(fullInfo)

codeGenObject.generateCode()
codeGenObject.exportCode()

#print(workspaceFolderName)
