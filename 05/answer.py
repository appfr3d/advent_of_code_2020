import numpy as np
puzzle = open('input.txt', 'r')
lines = [line.strip() for line in puzzle]

seats = np.zeros((128, 8))
max_id = 0
max_row = 0
min_row = 127

for line in lines:
  row = [0,127]
  col = [0,7]
  for c in line.strip():
    if c == 'F':
      row[1] = (row[1] - row[0])//2 + row[0]
    elif c == 'B':
      row[0] = (row[1] - row[0])//2 + 1 + row[0]
    elif c == 'L':
      col[1] = (col[1] - col[0])//2 + col[0]
    elif c == 'R':
      col[0] = (col[1] - col[0])//2 + 1 + col[0]
  max_id = np.max([max_id, row[0]*8 + col[0]])
  seats[row[0], col[0]] = 1
  max_row = np.max([max_row, row[0]])
  min_row = np.min([min_row, row[0]])

# Part 1
print(max_id)

# Part 2
occupied_seats = seats[min_row:max_row+1, :]
my_row, my_col = np.where(occupied_seats == np.min(occupied_seats))
print(((my_row[0] + min_row)*8 + my_col[0]))
