import random


rows, cols = (120,160)
arr = [[1]*cols]*rows

matrix = [[0 for i in range(cols)] for j in range(rows)]


count = 31
regions = 8
while regions != 0:
  
  RandomRows = random.randint(0,119)
  RandomCols = random.randint(0,159)
  A = matrix[RandomRows][RandomCols]
  B = matrix[RandomRows -31][RandomCols -31]
  matrix[RandomRows][RandomCols] = 1
  for isinstances in range(A,B):
    matrix[RandomRows][RandomCols-1] =1
    RandomCols = RandomCols -1
    for areas in range(A,B): 
      matrix[RandomRows-1][RandomCols] = 1
      RandomRows = RandomRows - 1
  
    

  regions = regions-1

print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
