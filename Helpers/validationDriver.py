import sys
sys.path.append('../SequencingStageFiles/')
from edge import Edge
from node import Node
from wiresharkValidation import validateCrossNodeDependency

def testNodeList():
    nodeList = []
    node1Dictionary = {
        "name": "node1",
        "value": 2
    }
    node1 = Node(0, "node1", node1Dictionary)

    node2Dictionary = {
        "name": "node2",
        "value": 3
    }
    node2 = Node(1, "node2", node2Dictionary)

    node3Dictionary = {
        "name": "node3",
        "value": 4
    }
    node3 = Node(2, "node3", node3Dictionary)

    nodeList.append(node1)
    nodeList.append(node2)
    nodeList.append(node3)

    return nodeList

def testCrossNodeDependency():
    nodeList = testNodeList()
    for node in nodeList:
        print(node.nodeName)
        print(node.dataDictionary)
    testDependency = "node1.value = node3.value"
    print(validateCrossNodeDependency(nodeList, testDependency))

testCrossNodeDependency()
