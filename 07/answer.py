puzzle = open('input.txt', 'r')
lines = [line.strip() for line in puzzle]

# Part 1
can_be_held_by = {}

for line in lines:
  outer_bag, rest = line.split(' bags contain ')
  if rest != 'no other bags.':
    inner_bags = rest.split(', ')
    for bag in inner_bags:
      parts = bag.split(' ')
      color = parts[1] + ' ' + parts[2]
      # print('adding or updating', outer_bag)
      if color in can_be_held_by:
        can_be_held_by[color].append(outer_bag)
      else:
        can_be_held_by[color] = [outer_bag]

all_holders = set()
bag_queue = can_be_held_by['shiny gold']

while len(bag_queue) != 0:
  # Save the bag
  all_holders.add(bag_queue[0]) 

  # Add more to the queue if needed
  if bag_queue[0] in can_be_held_by:
    for bag in can_be_held_by[bag_queue[0]]:
      if not bag in all_holders:
        # print(bag)
        bag_queue += [bag]

  # Remove bag from queue
  bag_queue.remove(bag_queue[0])

print(len(all_holders))


# Part 2
is_holding = {}

for line in lines:
  outer_bag, rest = line.split(' bags contain ')
  is_holding[outer_bag] = []
  if rest != 'no other bags.':
    inner_bags = rest.split(', ')
    for bag in inner_bags:
      parts = bag.split(' ')
      color = parts[1] + ' ' + parts[2]
      is_holding[outer_bag] += [(int(parts[0].strip()), color)]

def get_bag_nums(bag):
  new_bag_nums = 1 # denne baggen
  for new_bag in is_holding[bag[1]]:
    # + antall av baggene den inneholder
    new_bag_nums += new_bag[0]*get_bag_nums(new_bag)
  return new_bag_nums

total = 0
for bag in is_holding['shiny gold']:
  total += bag[0]*get_bag_nums(bag)
print(total)
