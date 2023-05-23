# Thank you Prim's Algorithm :)

def makeMatrix():
  file = open("Problem 107/p107_network.txt")
  matrix = file.readlines()
  for i in range(0, len(matrix)):
    matrix[i] = matrix[i].strip('\n').split(',')
  return matrix

def findWeight(matrix):
  weight = 0
  i = 0
  while i < len(matrix):
    for j in range(i, len(matrix)):
      if matrix[i][j] != '-':
        weight += int(matrix[i][j])
    i += 1
  return weight

matrix = makeMatrix()

start_total_weight = findWeight(matrix)

visited = [0]

total_min_weight = 0
while len(visited) < len(matrix):
  # find next lowest path connected to a visited node that leads to a non-visited node
  next_min_node = 0
  min_weight = 1000
  for v in visited:
    for adj in range(0, len(matrix[v])):
      if matrix[v][adj] != '-' and adj not in visited:
        if int(matrix[v][adj]) < min_weight:
          min_weight = int(matrix[v][adj])
          next_min_node = adj
  total_min_weight += min_weight
  visited.append(next_min_node)
  
print(start_total_weight)
print(total_min_weight)

print(start_total_weight - total_min_weight)

