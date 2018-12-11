class Edge:
    def __init__(self, edgeID, sourceNodeID, destNodeID, dependency):
        self.edgeID = edgeID
        self.sourceNodeID = sourceNodeID
        self.destNodeID = destNodeID
        self.dependency = dependency
