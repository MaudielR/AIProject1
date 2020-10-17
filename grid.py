
import math
import random

import numpy as np
"""
 moving horizontally or vertically between two hard to traverse cells has a cost of 2;
• moving diagonally between two hard to traverse cells has a cost of sqrt(8);
• moving horizontally or vertically between a regular unblocked cell and a hard to traverse cell
(in either direction) has a cost of 1.5;
• moving diagonally between a regular unblocked cell and a hard to traverse cell (in either
direction) has a cost of (sqrt(2)+sqrt(8))/2;

"""
class Node():

    #none 
    def __init__(self, parentNode:(), position:()):
        self.parentNode=parentNode
        self.position = position

        #distance to start Node, distance to goal, total cost
        self.Distance = 0
        self.goal = 0
        self.cost=0
        
    
#A start search 
    def Asearch(matrix, startPoint,EndPoint):
        #append node
        startParent = Node(None,startPoint)
        startParent.Distance = 0
        startParent.goal = 0
        startParent.cost=0 
        endnode = Node(None,endPoint)
        endnode.Distance=0
        endnode.goal=0
        endnode.cost = 0

        openlist = []
        closedlist = []
        
        #append starter node 
        openlist.append(startParent)
        print(len(openlist))
        
            
        #loop list until EndPoint found 
        while len(openlist) > 0:
            print("ARRAY LENGTH")
            print(len(openlist)) 
            newcurrent = openlist[0]
            
            nodeindex = 0
            print(newcurrent.position)
            print(newcurrent.cost)
            #find current node, if total cost of i is less than newcurrent cost make newcurrent = i:
            for newindex, i in enumerate(openlist):
                if i.cost < newcurrent.cost:
                    newcurrent=i
                    nodeindex= newindex
                    print("i.cost newcurren.cost")
                    print(i.cost)
                    print(newcurrent.cost)
                    print("nodeindex")
                    print(nodeindex)
            openlist.pop(nodeindex)
            closedlist.append(newcurrent)
            # if current node = endnode, path found 
            if newcurrent ==endnode: 
                Pathfound = []
                currentnode = newcurrent
                while currentnode != None: 
                    Pathfound.append(currentnode.position)
                    currentnode = currentnode.parentNode 
                #reversed path
                return Pathfound[::-1] 

            newChildren= []
            #check all positons, in range, not = 0
            for allPossiblePositons in [(1,1),(-1,-1),(0,-1),(-1,0),(1,-1),(-1,1),(0,1),(1,0)]:
                nextposition =(newcurrent.position[0]+allPossiblePositons[0], newcurrent.position[1]+ allPossiblePositons[1])
                
                
                print(nextposition)
                print(newcurrent.position[0])
                #check if node is not out of bounds
               
                if nextposition[0]> (len(matrix) -1) or nextposition[0] < 0 or nextposition[1] > (len(matrix[len(matrix)-1])-1) or nextposition[1] < 0:
                    continue
                #check 0 areas 
                if (matrix[nextposition[0]][nextposition[1]] == 0): 
                    continue

                if nextposition in enumerate(openlist):
                    continue
                nextnode = Node(newcurrent,nextposition)
                newChildren.append(nextnode) 
                
            
            print(newcurrent)
            print(len(newChildren))
            print(len(closedlist))
            print(len(openlist))
            newcost = 0
            for xelems in newChildren: #where it breaks
                for yelems in closedlist:
                    if xelems.position == yelems.position:
                        continue
                mX = newcurrent.position[0] 
                mY = newcurrent.position[1]
                nX = xelems.position[0]
                nY = xelems.position[1]
                xelems.cost = getCost(matrix, newcurrent.position, xelems.position)
                #nodes of f, g and h
                xelems.Distance = abs(xelems.position[0] - closedlist[0].position[0]) + abs(xelems.position[1] - closedlist[0].position[1])
                xelems.goal = abs(xelems.position[0] - endnode.position[0]) + abs(xelems.position[1] - endnode.position[1])
                xelems.cost = xelems.Distance + xelems.goal + xelems.cost
                # any movements from 1 to 1 = +1 cost
                
                

                print(xelems.cost)
                print(xelems.Distance)
                print(xelems.goal)
                for zelems in openlist:
                    if xelems == zelems and xelems.goal >= zelems.goal:
                        continue
                    
                openlist.append(xelems)
                print("I stop here")

"""
◦ Use ’0’ to indicate a blocked cell
◦ Use ’1’ to indicate a regular unblocked cell
◦ Use ’2’ to indicate a hard to traverse cell
◦ Use ’a’ to indicate a regular unblocked cell with a highway
◦ Use ’b’ to indicate a hard to traverse cell with a highway  
"""

def distance(vertices):
    x1 = vertices[0][0]
    x2 = vertices[1][0]
    y1 = vertices[0][0]
    y2 = vertices[1][1]
    return math.sqrt((x2-x1)**2+(y2-y1)**2)


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


def move(matrix, dir):
    global x
    global y
    global count
    global first
    # print("Move and X is " +str(x)+ " while y is " + str(y))
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
        print("X is: " + str(x))
        print("y is: " + str(y))
        print("mSize is: " + str(mSize))
    count += mSize
    return True


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



"""
Harder to Traverse Cells 
--------------------------
8 Random Cords 
-31x31 region centered around Random Cords
-50% chance for each cell to be hard to traverse 
"""

matrix = [["1" for i in range(120)] for j in range(160)]
centers = []
regions = 0
while regions < 8:
    hX = random.randint(0, 119)
    hY = random.randint(0, 159)
    if hX - 16 >= 0 and hX + 15 <= 119 and hY - 16 >= 0 and hY + 15 <= 159:
        for i in range(hX - 16, hX + 16):
            for j in range(hY - 16, hX + 15):
                r = random.randint(0, 2)
                if r == 0:
                    matrix[i][j] = "2"
        regions += 1
        centers.append((hX, hY))

"""
Select 4 Patths
----------------
-4 Random Cells at the boundary of the grid world 
-Move 20 cells H/V away from the boundary, this sequence of cells is a highway
-Next Move 60% chance to move in same direction, 20% in a perpendcular direction
**If you hit a cell that is already a highway, reject, and restart 
-Continue until you hit the boundary
-If length of highway is less than 100 then reject the path and restart
-if you cannot add a highway given the placement of the previous rivers, FULL RESTART

"""

paths = 0
while paths < 4:
    # Random starting cords
    x = random.randint(0, 119)
    y = random.randint(0, 159)
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

"""
(After Select Paths)
Select Blocked Cells > Agents cannot pass through these cells
-------------------
-Randomly select 20% of total cells, exclude all highways
**Agents can pass through where blocked cells touch diagonally
"""

blocked = 0
while blocked < 3840:
    x = random.randint(0, 159)
    y = random.randint(0, 119)
    if matrix[x][y] == "1" or matrix[x][y] == "2":
        matrix[x][y] = "0"
        blocked += 1

"""
Select Start and Goal
----------------------
>　Start is among unblocked cells, either normal or hard 
-Must be top 20 or bottom 20, left most 20 columns or right most 20 columns
> Goal can be any unbocked cell that is > 100 cells away 
"""
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



print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

matrix = np.array(matrix)

print(startPoint)
print(endPoint)

path = Node.Asearch(matrix, startPoint, endPoint)
print("this is my path")
print(path)

np.set_printoptions(threshold=np.inf, linewidth=np.inf)
with open("test.txt", 'w') as f:
    f.write(np.array2string(matrix, separator=', '))







"""
-Sstart denotes start vertex
-Sgoal denotes goal vertex
-C(s,s') cost of transiton between tow neighboring certices s,s'ES
-succ(s) the set of seccessors of vertex s in ES 

Step1- Generate a list - 
Step2- Store Children in Priority Queue based on distance to goal
Step3 Select Closest child and repeat from sptep 1

"""
