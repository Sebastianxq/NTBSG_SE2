from .edge import Edge
from .node import Node
import pydot

import sys
sys.path.append('../Helpers/')
from Helpers import wiresharkValidation

class StateMachine:
    def __init__(self, nodeList):
        self.nodeList = []
        self.edgeList = []
        nodeCounter = 0
        edgeCounter = 0
        prevNode = None
        for node in nodeList:
            nodeTemp = Node(nodeCounter, node["name"], node)
            #nodeTemp = {
                #"name": node["name"],
                #"index": nodeCounter,
            #}
            self.nodeList.append(nodeTemp)
            if prevNode is not None:
                edgeTemp = Edge(edgeCounter, prevNode.nodeID, nodeTemp.nodeID, "")
                #edgeTemp = {
                    #"edgeID": edgeCounter,
                    #"sourceID": nodeTemp["index"],
                    #"destID": prevNode["index"],
                    #"dependency": ""
                #}
                self.edgeList.append(edgeTemp)
                edgeCounter+= 1
            nodeCounter += 1
            prevNode = nodeTemp
        self.renderStateMachine()

    def renderStateMachine(self):
        graph = pydot.Dot(graph_type='digraph')
        for node in self.nodeList:
            graph.add_node(pydot.Node(node.nodeName))
        for edge in self.edgeList:
            graph.add_edge(pydot.Edge(self.nodeList[edge.sourceNodeID].nodeName, self.nodeList[edge.destNodeID].nodeName))
        graph.write_png('currentGraph.png')

    def addNode(self, nodeName):
        nodeTemp = Node(len(self.nodeList), nodeName)
        #nodeTemp = {
            #"name": node["name"],
            #"index": len(self.nodeList),
        #}
        self.nodeList.append(nodeTemp)
        self.renderStateMachine()

    def deleteNode(self, nodeID):
        del self.nodeList[nodeID]
        self.deleteAllRelatedEdges()
        self.renderStateMachine()

    def addEdge(self, sourceID, destID, dependency):
        edgeTemp = Edge(edgeCounter, sourceID, destID, dependency)
        #edgeTemp = {
            #"edgeID": len(self.edgeList),
            #"sourceID": sourceID,
            #"destID": destID,
            #"dependency": dependency
        #}
        self.edgeList.append(edgeTemp)
        self.renderStateMachine()

    def deleteEdge(self, edgeID):
        del self.edgeList[edgeID]
        self.renderStateMachine()

    def modifyEdge(self, edgeID, sourceID, destID, dependency):
        currentEdge = self.edgeList[edgeID]
        currentEdge.sourceNodeID = sourceID
        currentEdge.destNodeID = destID
        validDependency = wiresharkValidation.validateCrossNodeDependency(self.nodeList, dependency)
        if validDependency:
            currentEdge.dependency = dependency
        else:
            currentEdge.dependency = ""


    def deleteAllRelatedEdges(self, nodeID):
        for edge in self.edgeList:
            if edge.sourceNodeID == nodeID or edge.destNodeID == nodeID:
                self.deleteEdge(edge.edgeID)
        self.renderStateMachine()
