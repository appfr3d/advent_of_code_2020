puzzle = open('input.txt', 'r')
lines = [line.strip() for line in puzzle]

# Part 1
accumulator = 0
i = 0
executed_indecies = []

while not i in executed_indecies:
  executed_indecies.append(i)
  
  code, val = lines[i].split(' ')
  if code == 'acc':
    accumulator += int(val)
    i += 1
  elif code == 'jmp':
    i += int(val)
  elif code == 'nop':
    i += 1
  
print(accumulator)


# Part 2

# Find num of nop and jmp
num_nop_and_jmp = 0
for line in lines:
  if line.startswith('nop') or line.startswith('jmp'):
    num_nop_and_jmp += 1

for change_num in range(num_nop_and_jmp):
  accumulator = 0
  i = 0
  current_num = 0
  executed_indecies = []
  infini_loop = False

  while i < len(lines):
    executed_indecies.append(i)
    
    code, val = lines[i].split(' ')

    if code == 'acc':
      accumulator += int(val)
      i += 1
    elif code == 'jmp':
      if current_num == change_num:
        # act as a nop
        i += 1
      elif i+int(val) in executed_indecies:
        infini_loop = True
        break
      else:
        i += int(val)
      current_num += 1
      
    elif code == 'nop':
      if current_num == change_num:
        # act as a jmp
        i += int(val)
      elif i+1 in executed_indecies:
        infini_loop = True
        break
      else:
        i += 1
      current_num += 1
  if not infini_loop:
    print(accumulator)
    break