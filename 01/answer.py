puzzle = open('input.txt', 'r')
numbers = [int(line) for line in puzzle]

# Part 1
found = False
for first in numbers:
  for second in numbers:
    if first+second == 2020:
      print(first*second)
      found = True
      break
  if found:
    break

# Part 2
found = False
for first in numbers:
  for second in numbers:
    for third in numbers:
      if first+second+third == 2020:
        print(first*second*third)
        found = True
        break
    if found:
      break
  if found:
    break

# The input is short engough that it does not matter if i use indecies 
# in the for loops to make it faster it not. Sometimes the first thing 
# that comes to mind can work ok i guess :)