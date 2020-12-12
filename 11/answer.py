original_grid_1 = [[c for c in line.strip()] for line in open('input.txt', 'r')]
original_grid_2 = [[c for c in line.strip()] for line in open('input.txt', 'r')]

def adjacent(grid, i, j, part):
  ''' Returns the adjacent seats '''
  seats = []
  # Part 1
  if part == 1:
    for r in [-1, 0, 1]:
      if i + r >= 0 and i + r < len(grid):
        for c in [-1, 0, 1]:
          if j + c >= 0 and j + c < len(grid[0]):
            if not (r == 0 and c == 0):
              seats.append(grid[i+r][j+c])
  # Part 2
  elif part == 2:
    for r, c in [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]:
      mult = 1
      while 0 <= i + r*mult < len(grid) and 0 <= j + c*mult < len(grid[0]):
        val = grid[i+r*mult][j+c*mult]
        if val == '.':
          mult += 1
        else:
          seats.append(val)
          break
  return seats


def iterate(grid, part):
  ''' looks over the grid and performs changes based on the given rules '''
  changes = {}
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == 'L' and '#' not in adjacent(grid, i, j, part):
        changes[i*len(grid[0])+j] = '#'
      elif grid[i][j] == '#' and adjacent(grid, i, j, part).count('#') >= (4 + part - 1):
        changes[i*len(grid[0])+j] = 'L'

  # Perform changes
  for key, val in changes.items():
    j = key%len(grid[0])
    i = (key-j)//len(grid[0])
    grid[i][j] = val
  return grid, len(changes.keys()) > 0

def perform_iterations(seat_grid, part):
  changed = True
  while changed:
    seat_grid, changed = iterate(seat_grid, part)

  occupied = 0
  for row in seat_grid:
    occupied += row.count('#')
  print(occupied)


perform_iterations(original_grid_1, 1)
perform_iterations(original_grid_2, 2)
