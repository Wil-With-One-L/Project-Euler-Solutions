class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __str__(self):
    return f"({self.x}, {self.y})"

class Triangle:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
    
  def __str__(self):
    return f"{self.a}, {self.b}, {self.c}"

def trianglesFromFile(filename):
  file = open(filename, "r")
  lines = file.readlines()
  file.close()

  triangles = []
  for line in lines:
    points = line.split(',')
    a = Point(int(points[0]), int(points[1]))
    b = Point(int(points[2]), int(points[3]))
    c = Point(int(points[4]), int(points[5]))
    triangles.append(Triangle(a,b,c))
  
  return triangles

def area(a, b, c):
  return abs(float((a.x * (b.y - c.y)) + (b.x * (c.y - a.y)) + (c.x * (a.y - b.y)) / 2))

    
count = 0

triangles = trianglesFromFile("/Users/wilsonkenny/Desktop/Github-Repositories/Project-Euler-Solutions/Problem 102/p102_triangles.txt")

for triangle in triangles:
  abc = area(triangle.a, triangle.b, triangle.c)
  
  abx = area(triangle.a, triangle.b, Point(0,0))
  axc = area(triangle.a, Point(0,0), triangle.c)
  xbc = area(Point(0,0), triangle.b, triangle.c)


  if abc == abx + axc + xbc:
    count += 1
  
print(count)