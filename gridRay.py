import random

"""
◦ Use ’0’ to indicate a blocked cell
◦ Use ’1’ to indicate a regular unblocked cell
◦ Use ’2’ to indicate a hard to traverse cell
◦ Use ’a’ to indicate a regular unblocked cell with a highway
◦ Use ’b’ to indicate a hard to traverse cell with a highway  
"""


# Use to build highway
def build_highway(prevMatrix, dir):
    if x == 119 or y == 159:
        return "F"
    curMatrix = prevMatrix
    rC = random.randint(0, 100)
    if rC > 60:
        built = move(prevMatrix, dir)
        if built:
            return dir
        else:
            prevMatrix[:] = curMatrix
            return "R"
    else:
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
    mSize = 21
    if dir =="N":
        if mSize - 1 + y > 159:
            mSize = 159 - y
        for i in range(1, mSize):
            if matrix[x][y + i] == "a" or  matrix[x][y + i] == "b":
                return False
            if matrix[x][y + i] == "1":
                matrix[x][y + i] = "a"
            else:
                matrix[x][y + i] = "b"
        y = y + mSize - 1
    elif dir == "S":
        if y - mSize - 1 < 0:
            mSize = y + 1
        for i in range(1, mSize):
            if matrix[x][y - i] == "a" or matrix[x][y + i] == "b":
                return False
            if matrix[x][y - i] == "1":
                matrix[x][y - i] = "a"
            else:
                matrix[x][y - i] = "b"
        y = y - mSize - 1
    elif dir == "E":
        if mSize - 1 + x > 119:
            mSize = 119 - x
        for i in range(1, mSize):
            if matrix[x + i][y] == "a" or matrix[x][y + i] == "b":
                return False
            if matrix[x + i][y] == "1":
                matrix[x + i][y] = "a"
            else:
                matrix[x + i][y] = "b"
        x = x + mSize - 1
    elif dir == "W":
        if x - mSize - 1 < 0:
            mSize = x + 1
        for i in range(1, mSize):
            if matrix[x - i][y] == "a" or matrix[x][y + i] == "b":
                return False
            if matrix[x - i][y] == "1":
                matrix[x - i][y] = "a"
            else:
                matrix[x - i][y] = "b"
        x = x + mSize - 1
    count += mSize
    return True


"""
Harder to Traverse Cells 
--------------------------
8 Random Cords 
-31x31 region centered around Random Cords
-50% chance for each cell to be hard to traverse 
"""

rows, cols = (120, 160)
arr = [[1] * cols] * rows

matrix = [["1" for i in range(cols)] for j in range(rows)]

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

"""
Select 4 Paths
----------------
-4 Random Cells at the boundary of the grid world 
-Move 20 cells H/V away from the boundary, this sequence of cells is a highway
-Next Move 60% chance to move in same direction, 20% in a perpendcular direction
**If you hit a cell that is already a highway, reject, and restart 
-Continue until you hit the boundary
-If length of highway is less than 100 then reject the path and restart
-if you cannot add a highway given the placement of the previous rivers, FULL RESTART
"""

# A lot of what is done here is purely for randomization
paths = 0
while paths < 4:
    # Random starting cords
    x = random.randint(0, 119)
    y = random.randint(0, 159)
    count = 0
    print("This is y: " + str(y))
    print("This is X: " + str(x))
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
            attempts = 0

        if attempts > 5:
            # Check if the highway is completely blocked, if it's not then just reset attempts
            if move(matrix, "N") or move(matrix, "S") or move(matrix, "E") or move("S"):
                attempts = 0
            else:
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

"""

Select Start and Goal
----------------------
>　Start is among unblocked cells, either normal or hard 
-Must be top 20 or bottom 20, left most 20 columns or right most 20 columns
> Goal can be any unbocked cell that is > 100 cells away 
"""
"""

regions = 100

while regions != 0:
  count = 5
  RandomRows = random.randint(0,119)
  RandomCols = random.randint(0,159) 


  matrix[RandomRows][RandomCols] = 1
  matrix[RandomRows-1][RandomCols] = 1
  matrix[RandomRows-2][RandomCols] = 1
  matrix[RandomRows-3][RandomCols] = 1
  matrix[RandomRows-4][RandomCols] = 1
  matrix[RandomRows-5][RandomCols] = 1
  matrix[RandomRows][RandomCols-1] = 1
  matrix[RandomRows][RandomCols-2] = 1
  matrix[RandomRows][RandomCols-3] = 1
  matrix[RandomRows][RandomCols-4] = 1
  matrix[RandomRows][RandomCols -5] = 1
  matrix[RandomRows -1][RandomCols -1] = 1
  matrix[RandomRows -1][RandomCols -2] = 1
  matrix[RandomRows -1][RandomCols -3] = 1
  matrix[RandomRows -1][RandomCols -4] = 1
  matrix[RandomRows -1][RandomCols -5] = 1

  matrix[RandomRows -2][RandomCols -1] = 1
  matrix[RandomRows -3][RandomCols -1] = 1
  matrix[RandomRows -4][RandomCols -1] = 1
  matrix[RandomRows -5][RandomCols -1] = 1

  matrix[RandomRows -2][RandomCols -2] = 1
  matrix[RandomRows -2][RandomCols -3] = 1
  matrix[RandomRows -2][RandomCols -4] = 1
  matrix[RandomRows -2][RandomCols -5] = 1

  matrix[RandomRows -3][RandomCols -2] = 1
  matrix[RandomRows -4][RandomCols -2] = 1
  matrix[RandomRows -5][RandomCols -2] = 1

  matrix[RandomRows -3][RandomCols -3] = 1
  matrix[RandomRows -3][RandomCols -4] = 1
  matrix[RandomRows -3][RandomCols -5] = 1
  matrix[RandomRows -5][RandomCols -3] = 1
  matrix[RandomRows -4][RandomCols -3] = 1
  matrix[RandomRows -4][RandomCols -4] = 1
  matrix[RandomRows -4][RandomCols -5] = 1

  matrix[RandomRows -5][RandomCols -4] = 1


  matrix[RandomRows -5][RandomCols -5] = 1

  regions = regions-1

"""
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
