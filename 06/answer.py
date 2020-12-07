puzzle = open('input.txt', 'r')
lines = [line.strip() for line in puzzle]

# Part 1
group_counts = []
group_answers = set()

for line in lines:
  if line == '':
    group_counts.append(len(group_answers))
    group_answers = set()
  else:
    for c in line:
      group_answers.add(c)

print(sum(group_counts))

# Part 2
group_counts = []
group_answers = ''
skip_rest = False
for line in lines:
  if line == '':
    group_counts.append(len(group_answers))
    group_answers = ''
    skip_rest = False
  elif not skip_rest:
    if group_answers == '':
      group_answers = line
    else:
      keep = ''
      for c in line:
        if c in group_answers:
          keep += c
      
      if keep == '':
        skip_rest = True
      
      group_answers = keep

print(sum(group_counts))