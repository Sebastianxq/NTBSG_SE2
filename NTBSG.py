import sys
from Helpers.pcapToPdml import *
from SequencingStageFiles.stateMachine import StateMachine
#sys.argv[1] = dissectorPath
#sys.argv[2] = pcapPath
#sys.argv[3] = workspacePath
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])

nodeList = nodeSequenceFromPDML(sys.argv[1], sys.argv[2], sys.argv[3])
fullInfo = fullInformationFromPDML(sys.argv[1], sys.argv[2], sys.argv[3])

currStateMachine = StateMachine(nodeList)
