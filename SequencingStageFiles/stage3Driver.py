from stateMachine import *

def testNodes():
    nodeList = []
    node1 = {
        "name": "geninfo"
    }
    node2 = {
        "name": "frame"
    }
    node3 = {
        "name": "eth"
    }
    node4 = {
        "name": "ip"
    }
    node5 = {
        "name": "tcp"
    }
    node6 = {
        "name": "ssl"
    }

    nodeList.append(node1)
    nodeList.append(node2)
    nodeList.append(node3)
    nodeList.append(node4)
    nodeList.append(node5)
    nodeList.append(node6)

    return nodeList
def runStateMachineTests():
    nodeList = testNodes()
    testStateMachine = StateMachine(nodeList)

runStateMachineTests()
