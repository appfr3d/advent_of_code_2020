import re
puzzle = open('input.txt', 'r')

# Part 1
current_pass = ''
req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # cid is optional
num_fields_valid_passports = []
valid = 0

for line in puzzle:
  if line.strip() == '':
    passport_is_valid = True
    for field in req_fields:
      if not field in current_pass:
        passport_is_valid = False
        break
    if passport_is_valid:
      valid += 1
      num_fields_valid_passports.append(current_pass.strip())
    current_pass = ''
  else:
    current_pass += ' ' + line.strip()
print(valid)

# Part 2
byr_rule = lambda f: len(f) == 4 and f.isdigit() and 1920 <= int(f) <= 2002
iyt_rule = lambda f: len(f) == 4 and f.isdigit() and 2010 <= int(f) <= 2020
eyr_rule = lambda f: len(f) == 4 and f.isdigit() and 2020 <= int(f) <= 2030
hgt_rule = lambda f: f[:-2].isdigit() and 150 <= int(f[:-2]) <= 193 if (f[-2:] == 'cm') else (f[:-2].isdigit() and 59 <= int(f[:-2]) <= 76 if (f[-2:] == 'in') else False)
hcl_rule = lambda f: bool(re.search('^#[a-f0-9]{6}', f)) and len(f) == 7
ecl_rule = lambda f: f in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
pid_rule = lambda f: bool(re.search(r'\d{9}', f)) and len(f) == 9

# Same order as req_fields
rules = [byr_rule, iyt_rule, eyr_rule, hgt_rule, hcl_rule, ecl_rule, pid_rule]

valid = 0
for passport in num_fields_valid_passports:
  parts = passport.split(' ')
  passport_is_valid = True
  for part in parts:
    key_val = part.split(':')
    if len(key_val) != 2:
      print(part)
      continue
    field, val = key_val
    if field in req_fields and not rules[req_fields.index(field)](val):
      passport_is_valid = False
      break
  if passport_is_valid:
    valid += 1
print(valid)