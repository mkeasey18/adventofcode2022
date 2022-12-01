# part 1
# input = []
# with open('day1_inputs.txt') as f:
#     for line in f.readlines():
#         input.append(line.strip('\n'))

# max_cal = 0
# current_sum = 0
# for row in input:
#     if row == '':
#         current_sum = 0
#     else:
#          current_sum += int(row)

#     if current_sum > max_cal:
#         max_cal = current_sum

# print(max_cal)

# part 2
input = []
with open('day1_inputs.txt') as f:
    for line in f.readlines():
        input.append(line.strip('\n'))

max_cal = 0
current_sum = 0
list_of_sums = []

for row in input:
    if row == '':
        list_of_sums.append(current_sum)
        current_sum = 0
    else:
         current_sum += int(row)

list_of_sums.sort(reverse=True)

print(sum(list_of_sums[:3]))