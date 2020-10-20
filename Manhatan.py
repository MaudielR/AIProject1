import math
import random
import sys

import numpy as np


class Node():   

    def __init__(self, parentNode: (), position: ()):
        self.parentNode = parentNode
        self.position = position

        # distance to start Node, distance to goal, weight, total cost
        self.G = 0
        self.H = 0
        self.W = 1
        self.cost = 0

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.cost < other.cost

    def __hash__(self):
        return hash(self.cost)

#Can be visualized, but cannot be unvisualized also only do this after ALL TESTS are finished within a map cause it gets in the way of A*
def visalize(matrix, path, start, goal):
    temp = np.copy(matrix)
    for cords in path:
        mX, mY = cords
        temp[mX][mY] = "P"
    sX, sY = start
    gX, gY = goal
    temp[sX][sY] = "S"
    temp[gX][gY] = "G"
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in temp]))


# Calculates Distance between two vertices
def distance(vertices):
    x1 = vertices[0][0]
    x2 = vertices[1][0]
    y1 = vertices[0][1]
    y2 = vertices[1][1]
    return math.sqrt((((x2 - x1) ** 2) + ((y2 - y1) ** 2)))
#Where node is a Node object and goal is vertices
def optimalHeuristic(node, closed):
    D,D2 = 3,3
    nX, nY = node.position
    for n in getNeighborsA(node, closed):
        if n not in closed:
            mX, mY = n
            if matrix[mX][mY] != "0":
                suc = Node(node, n)
                nodeCost = getCostA(matrix, node, suc)
                if mX - nX != 0 and mY - nY != 0:
                    D2 = min(D2,nodeCost)
                else:
                    D = min(D,nodeCost)
    return D * (nX + nY) 


    return

# Move in a specified direciton
def move(matrix, dir):
    global x, y, count, first
    mSize = 21
    try:
        if dir == "N":
            if mSize - 1 + y >= 119:
                mSize = 119 - y
            for i in range(1, mSize):
                if matrix[x][y + i] == "a" or matrix[x][y + i] == "b":
                    return False
                if matrix[x][y + i] == "1":
                    matrix[x][y + i] = "a"
                else:
                    matrix[x][y + i] = "b"
            y = y + mSize + 1
        elif dir == "S":
            if y - mSize - 1 < 0:
                mSize = y + 1
            for i in range(1, mSize):
                if matrix[x][y - i] == "a" or matrix[x][y - i] == "b":
                    return False
                if matrix[x][y - i] == "1":
                    matrix[x][y - i] = "a"
                else:
                    matrix[x][y - i] = "b"
            y = y - mSize + 1
        elif dir == "E":
            if mSize - 1 + x >= 159:
                mSize = 159 - x
            for i in range(1, mSize):
                if matrix[x + i][y] == "a" or matrix[x + i][y] == "b":
                    return False
                if matrix[x + i][y] == "1":
                    matrix[x + i][y] = "a"
                else:
                    matrix[x + i][y] = "b"
            x = x + mSize + 1
        elif dir == "W":
            if x - mSize - 1 < 0:
                mSize = x + 1
            for i in range(1, mSize):
                if matrix[x - i][y] == "a" or matrix[x - i][y] == "b":
                    return False
                if matrix[x - i][y] == "1":
                    matrix[x - i][y] = "a"
                else:
                    matrix[x - i][y] = "b"
            x = x + mSize - 1
    except IndexError as e:
        print(e)
    count += mSize
    return True


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
                    path.append(node.position)
                    mX, mY = node.position
                    node = node.parentNode
                    cost += getCostA(matrix, node, Node(0, (mX,mY)))
                return path, cost
            n = getNeighborsA(node, closed)
            for x in n:
                if x not in closed:
                    mX, mY = x
                    if matrix[mX][mY] != "0":
                        suc = Node(node, x)
                        suc.W = weight
                        if H:
                            suc.H = math.trunc(distance((suc.position,goal)))
                        if suc not in fringe:
                            suc.G = sys.maxsize
                        nodeCost = getCostA(matrix, node, suc)
                        if node.G + nodeCost < suc.G:
                            suc.G = abs(node.G - nodeCost)
                            suc.parentNode = node
                            suc.cost = (suc.G + suc.W) * suc.H
                            if suc in fringe:
                                fringe.remove(suc)
                            fringe.append(suc)
    return None


def getNeighborsA(node, closed):
    neighbors = set()
    mX, mY = node.position
    top = True
    bottom = True
    right = True
    left = True
    if mY == 119:
        top = False;
        neighbors.add((mX, mY - 1))
    elif mY == 0:
        bottom = False
        neighbors.add((mX, mY + 1))
    else:
        neighbors.add((mX, mY - 1))
        neighbors.add((mX, mY + 1))

    if mX == 159:
        right = False
        neighbors.add((mX - 1, mY))
    elif mX == 0:
        left = False
        neighbors.add((mX + 1, mY))
    else:
        neighbors.add((mX + 1, mY))
        neighbors.add((mX - 1, mY))

    if top:
        if right:
            neighbors.add((mX + 1, mY + 1))

        if left:
            neighbors.add((mX - 1, mY + 1))

    if bottom:
        if right:
            neighbors.add((mX + 1, mY - 1))

        if left:
            neighbors.add((mX - 1, mY - 1))

    neighbors = neighbors - closed
    return neighbors


def getCostA(matrix, prev, curr):
    mX, mY = prev.position
    nX, nY = curr.position
    if mX - nX != 0 and mY - nY != 0:
        if matrix[mX][mY] == "1" and matrix[nX][nY] == "1":
            return math.sqrt(2)
        elif matrix[mX][mY] == "1" and matrix[nX][nY] == "2":
            return (math.sqrt(2) + math.sqrt(8)) / 2
        elif matrix[mX][mY] == "1" and matrix[nX][nY] == "a":
            return math.sqrt(.5) + math.sqrt(.03125)
        elif matrix[mX][mY] == "1" and matrix[nX][nY] == "b":
            return math.sqrt(.5) + math.sqrt(.125)
        elif matrix[mX][mY] == "2" and matrix[nX][nY] == "2":
            return math.sqrt(8)
        elif matrix[mX][mY] == "2" and matrix[nX][nY] == "a":
            return math.sqrt(2) + math.sqrt(.03125)
        elif matrix[mX][mY] == "2" and matrix[nX][nY] == "b":
            return math.sqrt(2) + math.sqrt(.125)
        elif matrix[mX][mY] == "a" and matrix[nX][nY] == "a":
            return math.sqrt(.125)
        elif matrix[mX][mY] == "a" and matrix[nX][nY] == "b":
            return math.sqrt(.03125) + math.sqrt(.125)
        else:
            return math.sqrt(.5)
    else:
        if matrix[mX][mY] == "1" and matrix[nX][nY] == "1":
            return 1
        elif matrix[mX][mY] == "1" and matrix[nX][nY] == "2":
            return 1.5
        elif matrix[mX][mY] == "1" and matrix[nX][nY] == "a":
            return .625
        elif matrix[mX][mY] == "1" and matrix[nX][nY] == "b":
            return .75
        elif matrix[mX][mY] == "2" and matrix[nX][nY] == "2":
            return 2
        elif matrix[mX][mY] == "2" and matrix[nX][nY] == "a":
            return 1.125
        elif matrix[mX][mY] == "2" and matrix[nX][nY] == "b":
            return 1.25
        elif matrix[mX][mY] == "a" and matrix[nX][nY] == "a":
            return .25
        elif matrix[mX][mY] == "a" and matrix[nX][nY] == "b":
            return .375
        else:
            return .5


def buildHard(matrix):
    centers = []
    regions = 0
    while regions < 8:
        hX, hY = random.randint(0, 159), random.randint(0, 119)
        if hX - 16 >= 0 and hX + 15 <= 119 and hY - 16 >= 0 and hY + 15 <= 159:
            for i in range(hX - 16, hX + 16):
                for j in range(hY - 16, hX + 15):
                    r = random.randint(0, 2)
                    if r == 0:
                        matrix[i][j] = "2"
            regions += 1
            centers.append((hX, hY))
    return matrix


def buildBlocks(matrix):
    global x, y
    blocked = 0
    while blocked < 3840:
        x = random.randint(0, 159)
        y = random.randint(0, 119)
        if matrix[x][y] == "1" or matrix[x][y] == "2":
            matrix[x][y] = "0"
            blocked += 1
    return matrix


def buildPathHelper(prevMatrix, dir):
    global x, y
    if (x >= 159 or y >= 119 or y <= 0 or x <= 0) and not first:
        return "F"
    curMatrix = prevMatrix
    rC = random.randint(0, 100)
    if rC < 60:
        built = move(prevMatrix, dir)
        if built:
            return dir
        else:
            prevMatrix[:] = curMatrix
            return "R"
    elif rC > 60 or first:
        if dir == "N":
            if move(prevMatrix, "E"):
                return "E"
            else:
                prevMatrix[:] = curMatrix
                return "R"
        elif dir == "S":
            if move(prevMatrix, "W"):
                return "W"
            else:
                prevMatrix[:] = curMatrix
                return "R"
        elif dir == "E":
            if move(prevMatrix, "S"):
                return "S"
            else:
                prevMatrix[:] = curMatrix
                return "R"
        elif dir == "W":
            if move(prevMatrix, "N"):
                return "N"
            else:
                prevMatrix[:] = curMatrix
                return "R"


def buildPath(matrix):
    global x, y, count, first
    paths = 0
    while paths < 4:
        x, y = random.randint(0, 159), random.randint(0, 119)
        count, first = 0, True
        if x > y:
            x = 0
            direction = "E"
        else:
            y = 0
            direction = "N"
        attempts = 0
        while direction != "F":
            oldDir = direction
            direction = buildPathHelper(matrix, direction)
            if direction == "R":
                attempts += 1
                direction = oldDir
            else:
                first = False
                attempts = 0

            if attempts > 5 or direction is None:
                break
        if count > 100:
            paths += 1
    return matrix


def buildGrid():
    matrix = [["1" for i in range(120)] for j in range(160)]
    matrix = buildHard(matrix)
    matrix = buildPath(matrix)
    matrix = buildBlocks(matrix)
    return matrix


def generateVertex(matrix):
    attempts = 0
    vertices = []
    while True:
        if len(vertices) == 2:
            if distance(vertices) > 100:
                break
            else:
                vertices.pop(0)

        if attempts % 2 == 0:
            x = random.randint(0, 20)
            y = random.randint(100, 119)
        else:
            x = random.randint(140, 159)
            y = random.randint(0, 20)

        if matrix[x][y] == "1" or matrix[x][y] == "2" and len(vertices) <= 1:
            vertices.append((x, y))
            attempts = 0
        else:
            attempts += 1
    return vertices

def getInfo(Algo):
    average, length = 0, 0
    for items in Algo:
        for item in items:
            path, cost = item
            average += cost
            length += len(path)
    return average/5, length/5

def getSplitInfo(Algo):
    LAverage, LLength = 0, 0
    RAverage, RLength = 0, 0
    count = 0
    for items in Algo:
        for item in items:
            path, cost = item
            if count < 5:
                LAverage += cost
                LLength += len(path)
            else:
                RAverage += cost
                RLength += len(path)
            count += 1
        return LAverage/5, LLength/5, RAverage/5, RLength/5
"""
x, y, first, count = 0, 0, True, 0
matrix = buildGrid()
vertices = generateVertex(matrix)
startPoint = vertices[0]
endPoint = vertices[1]
path, cost = A(matrix,startPoint,endPoint,1, False)
visalize(matrix, path ,startPoint,endPoint)
print(path)
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

"""
UCS, aStar, aWeighted = [], [], []
for i in range(0,5):
    matrix = buildGrid()
    for j in range(0,10):
        pUCS, pStar, pWeighted = [], [], []
        vertices = generateVertex(matrix)
        startPoint = vertices[0]
        endPoint = vertices[1]
        pUCS.append(A(matrix,startPoint,endPoint,1, False))
        pStar.append(A(matrix,startPoint,endPoint,1, True))
        if j < 5:
            pWeighted.append(A(matrix,startPoint,endPoint,1.25, True))
        else:
            pWeighted.append(A(matrix, startPoint, endPoint, 2, True))


    UCS.append(pUCS)
    aStar.append(pStar)
    aWeighted.append(pWeighted)

#Average Cost and length
AverageUCS, UCSLen = getInfo(UCS)
AverageA, ALen = getInfo(aStar)
AverageWL, WLenL, AverageWR, WLenR = getSplitInfo(aWeighted)
WAverage = (AverageWL + AverageWR)/2
LenW = (WLenL+WLenR)/2
print("UCS " + str(AverageUCS) + " Len: " + str(UCSLen))
print("A* " + str(AverageA) + " Len: " + str(ALen))
print("Weighted A* " + str(AverageWL) + " Len: " + str(WLenL))
print("Weighted A* " + str(AverageWR) + " Len: " + str(WLenR))
print("Total Weighted A* " + str(WAverage) + " Len: " + str(LenW))
print(UCS)
print(aStar)
print(aWeighted)




"""np.set_printoptions(threshold=np.inf, linewidth=np.inf)
    with open("Map"+str(i)+".txt", 'w') as f:
        f.write(np.array2string(matrix, separator=', '))"""