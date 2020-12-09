puzzle = open('input.txt', 'r')
lines = [int(line.strip()) for line in puzzle]


# Part 1
invalid = 0
for i in range(25, len(lines)):
  found = False
  for n_1 in range(i-25, i):
    for n_2 in range(i-24, i):
      if lines[n_1] != lines[n_2] and lines[n_1] + lines[n_2] == lines[i]:
        found = True
        break
    if found:
      break
  if not found:
    invalid = lines[i]
    break
print(invalid)

# Part 2
start = 0
found = False
while not found:
  for i in range(start+1, len(lines)):
    if sum(lines[start:i+1]) == invalid:
      minst = min(lines[start:i+1])
      mest  = max(lines[start:i+1])
      print(minst, '+', mest, '=', minst+mest)
      found = True
      break
    elif sum(lines[start:i]) > invalid:
      break
  if found:
    break
  start += 1
