import math
import random
import sys
from queue import PriorityQueue

import numpy as np


class Node():

    # none
    def __init__(self, parentNode: (), position: ()):
        self.parentNode = parentNode
        self.position = position

        # distance to start Node, distance to goal, total cost
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

    # A start search
    def Asearch(matrix, startPoint, EndPoint):
        # append node
        startParent = Node(None, startPoint)
        startParent.Distance = 0
        startParent.goal = 0
        startParent.cost = 0
        endnode = Node(None, endPoint)
        endnode.Distance = 0
        endnode.goal = 0
        endnode.cost = 0

        openlist = []
        closedlist = []

        # append starter node
        openlist.append(startParent)
        print(len(openlist))

        # loop list until EndPoint found
        while len(openlist) > 0:

            print(len(openlist))
            newcurrent = openlist[0]

            nodeindex = 0

            # find current node, if total cost of i is less than newcurrent cost make newcurrent = i:
            for newindex, i in enumerate(openlist):
                if i.cost < newcurrent.cost:
                    newcurrent = i
                    nodeindex = newindex

            openlist.pop(nodeindex)
            closedlist.append(newcurrent)
            # if current node = endnode, path found
            if newcurrent == endnode:
                Pathfound = []
                currentnode = newcurrent
                while currentnode != None:
                    Pathfound.append(currentnode.position)
                    currentnode = currentnode.parentNode
                    # reversed path
                return Pathfound[::-1]

            newChildren = []
            # check all positons, in range, not = 0
            for allPossiblePositons in [(1, 1), (-1, -1), (0, -1), (-1, 0), (1, -1), (-1, 1), (0, 1), (1, 0)]:
                nextposition = (
                    newcurrent.position[0] + allPossiblePositons[0], newcurrent.position[1] + allPossiblePositons[1])

                # check if node is not out of bounds
                if nextposition[0] > (len(matrix) - 1) or nextposition[0] < 0 or nextposition[1] > (
                        len(matrix[len(matrix) - 1]) - 1) or nextposition[1] < 0:
                    print("invalid position")
                    continue

                # check 0 areas
                if matrix[nextposition[0]][nextposition[1]] == 1 or matrix[nextposition[0]][nextposition[1]] == 'a' or \
                        matrix[nextposition[0]][nextposition[1]] == 'b':
                    continue

                nextnode = Node(newcurrent, nextposition)
                newChildren.append(nextnode)
                print(nextposition)
            print(len(newChildren))
            print(len(closedlist))
            for xelems in newChildren:  # where it breaks
                for yelems in closedlist:
                    if xelems == yelems:
                        continue
                # I have the cost wrong, must impliment method of :

                # nodes of f, g and h
                xelems.Distance = abs(xelems.position[0] - startParent.position[0]) + abs(
                    xelems.position[1] - startParent.position[1])
                xelems.goal = abs(xelems.position[0] - endnode.position[0]) + abs(
                    xelems.position[1] - endnode.position[1])
                xelems.count = xelems.Distance + xelems.goal

                for zelems in openlist:
                    if zelems == xelems and xelems.Distance > zelems.Distance:
                        continue

                openlist.append(xelems)
                print("I stop here")


# Calculates Distance between two vertices
def distance(vertices):
    x1 = vertices[0][0]
    x2 = vertices[1][0]
    y1 = vertices[0][1]
    y2 = vertices[1][1]
    return math.sqrt((((x2 - x1) ** 2) + ((y2 - y1) ** 2)))


# Use to build highway
def build_highway(prevMatrix, dir):
    global x
    global y
    # print("Build and X is " +str(x)+ " while y is " + str(y))
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


# Move in a specified direciton
def move(matrix, dir):
    global x
    global y
    global count
    global first
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

def UpdateVertex(matrix, node, suc, fringe):
    cost = getCostA(matrix, node, suc)
    if node.G + cost < suc.G:
        suc.G = node.G + cost
        suc.parentNode = node
        suc.cost = suc.G + suc.cost
        if suc in fringe.queue:
            fringe.remove(suc)
        fringe.put(suc)

"""def A(matrix, start, goal):
    fringe = []
    closed = []
    nodeStart = Node(None, start)
    nodeGoal = Node(None, goal)
    fringe.append(nodeStart)
    while len(fringe) > 0:
        fringe.sort()
        node = fringe.pop(0)
        if node == nodeGoal:
            path = []
            while node != nodeStart:
                path.append(node.position)
                node = node.parentNode
            return path
        closed.append(node)
        mX, mY = node.position
        for x in getNeighborsA(node):
            if matrix[mX][mY] != "0":
                suc = Node(node, x)
            if suc not in closed:
                if suc not in fringe:
                    suc.G = sys.maxsize
                    suc.parentNode = None
                UpdateVertex(matrix, node, suc, fringe)
    return None"""


def A(matrix, start, goal, weight):
    fringe = []
    closed = set()
    nodeStart = Node(start, start)
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
                    matrix[mX][mY] = "P"
                    node = node.parentNode
                return path
            n = getNeighborsA(node, closed)
            for x in n:
                if x not in closed:
                    mX, mY = x
                    if matrix[mX][mY] != "0":
                        suc = Node(node, x)
                        if suc not in fringe:
                            suc.G = sys.maxsize
                            suc.W = weight
                        nodeCost = getCostA(matrix, node, suc)
                        if node.G + cost < suc.G:
                            suc.G = node.G + nodeCost
                            suc.parentNode = node
                            suc.cost = suc.G + suc.W*suc.H
                            if suc in fringe:
                                fringe.remove(suc)
                            fringe.append(suc)
    return None

"""   suc = Node(node, x)
   if suc not in fringe.queue:
       suc.G = sys.maxsize
   UpdateVertex(matrix, node, suc, fringe)
"""

def ucs(matrix, start, goal):
    visited = set()
    track = {}
    queue = PriorityQueue()
    queue.put((0, start, 0))

    while queue:
        cost, node, parent = queue.get()
        if node not in visited:
            visited.add(node)
            track[node] = parent
            if node == goal:
                return visited, track, cost
            for i in getNeighbors(node):
                if i not in visited:
                    mX, mY = i
                    # Check for blocked cells
                    if matrix[mX][mY] != "0":
                        nodeCost = getCost(matrix, node, i)
                        total_cost = cost + nodeCost
                        queue.put((total_cost, i, node))
    return "UCS has failed if it reaches this point"


# Node is a tuple of (X,Y)
def getNeighbors(node):
    neighbors = set()
    mX, mY = node
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
    elif bottom:
        if right:
            neighbors.add((mX + 1, mY - 1))
        if left:
            neighbors.add((mX - 1, mY - 1))

    return neighbors


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

    neighbors = neighbors-closed
    return neighbors


def getCost(matrix, prev, curr):
    mX, mY = prev
    nX, nY = curr
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

# >> Harder to Traverse Cells
matrix = [["1" for i in range(120)] for j in range(160)]
centers = []
regions = 0
while regions < 8:
    hX = random.randint(0, 159)
    hY = random.randint(0, 119)
    if hX - 16 >= 0 and hX + 15 <= 119 and hY - 16 >= 0 and hY + 15 <= 159:
        for i in range(hX - 16, hX + 16):
            for j in range(hY - 16, hX + 15):
                r = random.randint(0, 2)
                if r == 0:
                    matrix[i][j] = "2"
        regions += 1
        centers.append((hX, hY))

# >> Select 4 Paths
paths = 0
while paths < 4:
    # Random starting cords
    x = random.randint(0, 159)
    y = random.randint(0, 119)
    count = 0
    first = True
    if x > y:
        x = 0
        direction = "E"
    else:
        y = 0
        direction = "N"
    attempts = 0
    while direction != "F":
        oldDir = direction
        direction = build_highway(matrix, direction)
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

# >> Select Blocked Cells
blocked = 0
while blocked < 3840:
    x = random.randint(0, 159)
    y = random.randint(0, 119)
    if matrix[x][y] == "1" or matrix[x][y] == "2":
        matrix[x][y] = "0"
        blocked += 1

# >>Select Start and Goal
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

startPoint = vertices[0]
endPoint = vertices[1]

# print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

"""


visited, tracked, cost = ucs(matrix, startPoint, endPoint)
print(startPoint)
print(endPoint)
#print(tracked)
print(cost)

for i in visited:
    mX, mY = i
    matrix[mX][mY] = "X"

path = []
currNode = tracked[endPoint]
path.append((endPoint))
while currNode != 0:
    mX, mY = currNode
    matrix[mX][mY] = "P"
    path.append(currNode)
    currNode = tracked[currNode]


sX, sY = startPoint
eX, eY = endPoint

matrix[sX][sY] = "S"
matrix [eX][eY] = "E"


print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
"""

visited, tracked, cost = ucs(matrix, startPoint, endPoint)
print(startPoint)
print(endPoint)
# print(tracked)
print(cost)

path = A(matrix, startPoint, endPoint, 1)
print(path)
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

matrix = np.array(matrix)
# Save the Grid to a Textfile
np.set_printoptions(threshold=np.inf, linewidth=np.inf)
with open("test.txt", 'w') as f:
    f.write(np.array2string(matrix, separator=', '))
