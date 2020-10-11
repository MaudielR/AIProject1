import random

rows, cols = (120,160)
arr = [[1]*cols]*rows

matrix = [[0 for i in range(cols)] for j in range(rows)]



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

print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
  

  
 