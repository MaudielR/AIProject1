# Node is a tuple of (X,Y)
import math
from queue import PriorityQueue

"""Unoptimized A* search
def A(matrix, start, goal):
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
    return None
"""

def UpdateVertex(matrix, node, suc, fringe):
    cost = getCost(matrix, node, suc)
    if node.G + cost < suc.G:
        suc.G = node.G + cost
        suc.parentNode = node
        suc.cost = suc.G + suc.cost
        if suc in fringe.queue:
            fringe.remove(suc)
        fringe.put(suc)

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