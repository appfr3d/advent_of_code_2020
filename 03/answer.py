import math
puzzle = open('input.txt', 'r')
lines = [line.strip() for line in puzzle]

# Part 1
x = 0
trees = 0
for line in lines:
  if line[x % len(line)] == '#':
    trees += 1
  x += 3

print(trees)

# Part 2
slopes = [[1,1], [1,3], [1,5], [1,7], [2, 1]]
trees = [0,0,0,0,0]
for s in range(len(slopes)):
  x = 0
  for y in range(0, len(lines), slopes[s][0]):
    if lines[y][x % len(lines[y])] == '#':
      trees[s] += 1 
    x += slopes[s][1]
print(trees)
print(math.prod(trees))