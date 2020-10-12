import random

"""
◦ Use ’0’ to indicate a blocked cell
◦ Use ’1’ to indicate a regular unblocked cell
◦ Use ’2’ to indicate a hard to traverse cell
◦ Use ’a’ to indicate a regular unblocked cell with a highway
◦ Use ’b’ to indicate a hard to traverse cell with a highway  
"""

rows, cols = (120, 160)
arr = [[1] * cols] * rows

matrix = [["0" for i in range(cols)] for j in range(rows)]

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
for i in range(0, 4):
    # Random starting cords
    x = random.randint(0, 119)
    y = random.randint(0, 159)
    # Random amount of space to move right
    hX = random.randint(0, 21)
    # Random amount of space to move up
    hY = 20 - hX
    print("This is hY: " + str(hY))
    print("This is hX: " + str(hX))
    print("This is y: " + str(y))
    print("This is X: " + str(x))
    if x > y:
        for j in range(0, hX):
            x += 1
            if x >= 119:
                x = 119
                hY += hX - j
                break
            matrix[x][0] = "a"
        for j in range(1, hY):
            matrix[x][j] = "a"
    else:
        for j in range(0, hY):
            y += 1
            if y >= 159:
                y = 159
                hX += hY - j
                break
            matrix[0][y] = "a"
        for j in range(1, hX):
            matrix[j][y] = "a"

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



