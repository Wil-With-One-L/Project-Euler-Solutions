def getV2D(filename):

  file = open(filename)
  numGrid = []
  for row in file.readlines():
    row = row.strip('\n')
    row = row.split(' ')
    numGrid.append(row)

  return numGrid

def intV2D(grid):
  to_return = []
  for row in grid:
    new_row = []
    for n in row:
      new_row.append(int(n))
    to_return.append(new_row)
  return to_return

def largestHoriz(grid):
  largest = 0
  for row in range(0, len(grid)):
    for col in range(0, len(grid[row]) - 3):
      test = 1
      for i in range(0, 4):
        test *= grid[row][col + i]
      largest = max(largest, test)
  return largest

def largestVert(grid):
  largest = 0
  for row in range(0, len(grid) - 3):
    for col in range(0, len(grid[row])):
      test = 1
      for i in range(0, 4):
        test *= grid[row + i][col]
      largest = max(largest, test)
  return largest
    
def largestDiag(grid):
  largest = 0
  for row in range(0, len(grid) - 3):
    for col in range(0, len(grid[row]) - 3):
      test = 1
      for i in range(0, 4):
        # if grid[row + i][col] == 0:
        #   break
        test *= grid[row + i][col + i]
      largest = max(largest, test)

  for row in range(3, len(grid)):
    for col in range(0, len(grid[row]) - 3):
      test = 1
      for i in range(0, 4):
        # if grid[row + i][col] == 0:
        #   break
        test *= grid[row - i][col + i]
      largest = max(largest, test)
  return largest
  
numGrid = getV2D("/Users/wilsonkenny/Desktop/Github-Repositories/Project-Euler-Solutions/Problem 11/number-grid.txt")
numGrid = intV2D(numGrid)

horiz = largestHoriz(numGrid)
vert = largestVert(numGrid)
diag = largestDiag(numGrid)

print(max(horiz, vert, diag))