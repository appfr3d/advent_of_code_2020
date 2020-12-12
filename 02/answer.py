puzzle = open('input.txt', 'r')
lines = [line.strip() for line in puzzle]

# Part 1
num_valid = 0
for line in lines:
  parts = line.split(': ')
  password = parts[1].strip()
  values = parts[0].split(' ')
  min_max = values[0].split('-')
  minimum = int(min_max[0].split(' ')[0])
  maximum = int(min_max[1].split(' ')[0])
  char = values[1]
  if minimum <= password.count(char) <= maximum:
    num_valid += 1
print(num_valid)

# Part 2
num_valid = 0
for line in lines:
  parts = line.split(': ')
  password = parts[1].strip()
  values = parts[0].split(' ')
  first_last = values[0].split('-')
  first = int(first_last[0].split(' ')[0])
  last = int(first_last[1].split(' ')[0])
  char = values[1]
  if password[first-1] == char and password[last-1] != char:
    num_valid += 1
  elif password[first-1] != char and password[last-1] == char:
    num_valid +=1

print(num_valid)

  
