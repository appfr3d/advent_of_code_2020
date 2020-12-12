puzzle = open('input.txt', 'r')
lines = [int(line.strip()) for line in puzzle]
lines.sort()

# Part 1
# 3 stars on one because of the built-in adapter 
diffs = { 1:0, 2:0, 3:1 }
last = 0
for line in lines:
  diffs[line - last] += 1
  last = line
print(diffs[1]*diffs[3])

# Part 2
# 
lines.insert(0,0)
lines.append(lines[-1]+3)

groups = []
group = []
for line in lines:
  if len(group) == 0:
    group.append(line)
  elif group[-1] + 1 == line:
    group.append(line)
  else:
    groups.append(group)
    group = [line]
# Append the last group
groups.append(group)


# Possible combinations for different lenghts of groups
# 1: 1
# 2: 1 2
# 3: 1 2 3, 1 3
# 4: 1 2 3 4, 1 2 4, 1 3 4, 1 4
# 5: 1 2 3 4 5, 
#    1 2 3 5  , 1 2 4 5, 1 3 4 5,
#    1 2 5    , 1 3 5  , 1 4 5
combo_multiplier = [1, 1, 2, 4, 7]
combos = 1
for g in groups:
  combos *= combo_multiplier[len(g)-1]
print(combos)