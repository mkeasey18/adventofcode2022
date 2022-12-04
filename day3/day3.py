import string

# part 1
alphabet = list(string.ascii_letters)
alpha_dict = {}
for i, letter in enumerate(alphabet):
    alpha_dict[letter] = i + 1

with open('day3_inputs.txt') as f:
    input = f.readlines()
    input = [line.strip('\n') for line in input]

priorities_sum = 0
for rucksack in input:
    midway = int(len(rucksack)/2)
    comp1 = set(rucksack[:midway])
    comp2 = set(rucksack[midway:])
    common_item = comp1.intersection(comp2)
    common_item = ''.join(common_item)
    
    priorities_sum += alpha_dict[common_item]

print(priorities_sum)

# part 2

alphabet = list(string.ascii_letters)
alpha_dict = {}
for i, letter in enumerate(alphabet):
    alpha_dict[letter] = i + 1

with open('day3_inputs.txt') as f:
    input = f.readlines()
    input = [line.strip('\n') for line in input]

priorities_sum = 0
group_counter = 0

for i, rucksack in enumerate(input):
    if group_counter == 2:
        common_item = set(rucksack).intersection(set(input[i-1]), set(input[i-2]))
        common_item = ''.join(common_item)
        priorities_sum += alpha_dict[common_item]
        group_counter = 0
        continue

    group_counter += 1
    

print(priorities_sum)

