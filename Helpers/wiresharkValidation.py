def validateCrossNodeDependency(nodeList, dependency):
    cleanDependency = dependency.replace(" ", "")
    leftAndRightSide = cleanDependency.split("=")
    leftSideValid = False
    rightSideValid = False
    if len(leftAndRightSide) is 2:
        leftSide = leftAndRightSide[0]
        rightSide = leftAndRightSide[1]

        splitLeft = leftSide.split(".")
        splitRight = rightSide.split(".")

        if len(splitLeft) is 2 and len(splitRight) is 2:
            nodeLeft, attributeLeft = splitLeft
            nodeRight, attributeRight = splitRight
            for node in nodeList:
                if leftSideValid is False and node.nodeName == nodeLeft and attributeLeft in node.dataDictionary:
                    leftSideValid = True
                    nodeList.remove(node)
                if rightSideValid is False and node.nodeName == nodeRight and attributeRight in node.dataDictionary:
                    rightSideValid = True
                    nodeList.remove(node)
    if leftSideValid and rightSideValid:
        return True
    return False

def validatePacketDependency(nodeList, dependency):
    cleanDependency = dependency.replace(" ", "")
    leftAndRightSide = cleanDependency.split("=")
    leftSideValid = False

    if len(leftAndRightSide) is 2:
        leftSide = leftAndRightSide[0]

        splitLeft = leftSide.split(".")
        if len(splitLeft) is 2 and len(splitRight) is 2:
            nodeLeft, attributeLeft = splitLeft
            for node in nodeList:
                if leftSideValid is False and node.nodeName == nodeLeft and attributeLeft in node.dataDictionary:
                    return True
    return False
