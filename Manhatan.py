import math
import random
import sys
from gridRay import Node, buildGrid,buildPath,buildBlocks,buildHard,buildPathHelper,getNeighborsA,getInfo,getCostA,getSplitInfo,generateVertex,getListTotal,move,distance
import numpy as np


#Where node is a Node object and goal is vertices
def optimalHeuristic(node, closed, goal):
    D= 3
    nX, nY = node.position
    gX, gY = goal
    dX = abs(nX-gX)
    dY = abs(nY-gY)
    for n in getNeighborsA(node, closed):
        if n not in closed:
            mX, mY = n
            if matrix[mX][mY] != "0":
                suc = Node(node, n)
                nodeCost = getCostA(matrix, node, suc)
                D = min(D,nodeCost)
    return D * (dX+dY)


def A(matrix, start, goal, weight, H):
    fringe = []
    closed = set()
    cost = 0
    nodeStart = Node(start, start)
    nodeStart.W = weight
    fringe.append(nodeStart)
    while fringe:
        fringe.sort()
        node = fringe.pop(0)
        if node not in closed:
            closed.add(node.position)
            if node.position == goal:
                path = []
                while node != nodeStart:
                    mem = sys.getsizeof(fringe) + sys.getsizeof(closed)
                    path.append(node.position)
                    mX, mY = node.position
                    node = node.parentNode
                    cost += getCostA(matrix, node, Node(0, (mX, mY)))
                return path, cost, mem, len(closed)
            n = getNeighborsA(node, closed)
            for x in n:
                if x not in closed:
                    mX, mY = x
                    if matrix[mX][mY] != "0":
                        suc = Node(node, x)
                        suc.W = weight
                        nodeCost = getCostA(matrix, node, suc)
                        if H == "D":
                            suc.H = optimalHeuristic(suc, closed, goal)
                        elif H == "N":
                            suc.H = math.trunc(distance((suc.position, goal)))
                        if suc not in fringe:
                            suc.G = sys.maxsize
                        if node.G + nodeCost < suc.G:
                            suc.G = node.G + nodeCost
                            suc.parentNode = node
                            suc.cost = suc.G + suc.W * suc.H
                            if suc in fringe:
                                fringe.remove(suc)
                            fringe.append(suc)
    return None

UCS, aStar, aWeighted = [], [], []
for i in range(0,5):
    pUCS, pStar, pWeighted = [], [], []
    matrix = buildGrid()
    matrix = np.array(matrix)
    np.set_printoptions(threshold=np.inf, linewidth=np.inf)
    with open("Map" + str(i+1) + ".txt", 'w') as f:
        f.write(np.array2string(matrix, separator=', '))
    for j in range(0, 10):
        vertices = generateVertex(matrix)
        startPoint = vertices[0]
        endPoint = vertices[1]
        pUCS.append(A(matrix, startPoint, endPoint, 1, "F"))
        pStar.append(A(matrix, startPoint, endPoint, 1, "D"))
        if j < 5:
            pWeighted.append(A(matrix, startPoint, endPoint, 1.25, "D"))
        else:
            pWeighted.append(A(matrix, startPoint, endPoint, 2, "D"))
    UCS.append(pUCS)
    aStar.append(pStar)
    aWeighted.append(pWeighted)

# Average Cost and length
AverageUCS, UCSLen, MemoryUCS, ExpandedUCS = getInfo(UCS)
AverageA, ALen, MemoryA, ExpandedA = getInfo(aStar)
AverageWL, WLenL, MemoryWL,ExpandedWL, AverageWR, WLenR, MemoryWR, ExpandedWR = getSplitInfo(aWeighted)
print("UCS " + str(AverageUCS) + " Len: " + str(UCSLen) + " Mem: " + str(MemoryUCS) + " Nodes: " + str(ExpandedUCS))
print("A* " + str(AverageA) + " Len: " + str(ALen)+ " Mem: " + str(MemoryA) + " Nodes: " + str(ExpandedA))
print("Weighted A* with 1.25:  " + str(AverageWL) + " Len: " + str(WLenL) + " Mem: " + str(MemoryWL) + " Nodes: " + str(ExpandedWL))
print("Weighted A* with 2:  " + str(AverageWR) + " Len: " + str(WLenR) + " Mem: " + str(MemoryWR) + " Nodes: " + str(ExpandedWR))
AverageUCS, UCSLen, MemoryUCS, ExpandedUCS = getListTotal(AverageUCS)/5, getListTotal(UCSLen)/5, getListTotal(MemoryUCS)/5, getListTotal(ExpandedUCS)/5
AverageA, ALen, MemoryA, ExpandedA = getListTotal(AverageA)/5, getListTotal(ALen)/5, getListTotal(MemoryA)/5, getListTotal(ExpandedA)/5
AverageWL, WLenL, MemoryWL, ExpandedWL = getListTotal(AverageWL)/5, getListTotal(WLenL)/5, getListTotal(MemoryWL)/5, getListTotal(ExpandedWL)/5
AverageWR, WLenR, MemoryWR, ExpandedWR = getListTotal(AverageWR)/5, getListTotal(WLenR)/5, getListTotal(MemoryWR)/5, getListTotal(ExpandedWR)/5
WAverage = (AverageWL + AverageWR) / 2
LenW = (WLenL + WLenR) / 2
MemoryW = (MemoryWL+MemoryWR)/2
ExpandedW = (ExpandedWL+ExpandedWR)/2
print("UCS " + str(AverageUCS) + " Len: " + str(UCSLen) + " Mem: " + str(MemoryUCS) + " Nodes: " + str(ExpandedUCS))
print("A* " + str(AverageA) + " Len: " + str(ALen)+ " Mem: " + str(MemoryA) + " Nodes: " + str(ExpandedA))
print("Weighted A* with 1.25 " + str(AverageWL) + " Len: " + str(WLenL) + " Mem: " + str(MemoryWL) + " Nodes: " + str(ExpandedWL))
print("Weighted A* with 2: " + str(AverageWR) + " Len: " + str(WLenR) + " Mem: " + str(MemoryWR) + " Nodes: " + str(ExpandedWR))
print("Total Weighted A* " + str(WAverage) + " Len: " + str(LenW)+ " Mem: " + str(MemoryW) + " Nodes: " + str(ExpandedW))
