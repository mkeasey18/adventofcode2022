with open('day4_inputs.txt') as f:
    input_list = f.readlines()
    input_list = [line.strip().split(',') for line in input_list]

overlap_count = 0
for elf1, elf2 in input_list:
    elf1_min, elf1_max = elf1.split('-')
    elf1_min, elf1_max = int(elf1_min), int(elf1_max)
    elf2_min, elf2_max = elf2.split('-')
    elf2_min, elf2_max = int(elf2_min), int(elf2_max)

    if elf1_min <= elf2_min and elf1_max >= elf2_max:
        overlap_count += 1
        continue

    if elf2_min <= elf1_min and elf2_max >= elf1_max:
        overlap_count += 1
        continue

print(f"The part 1 overlap count is: {overlap_count}")

overlap_count = 0
for elf1, elf2 in input_list:
    elf1_min, elf1_max = elf1.split('-')
    elf1_min, elf1_max = int(elf1_min), int(elf1_max)
    elf2_min, elf2_max = elf2.split('-')
    elf2_min, elf2_max = int(elf2_min), int(elf2_max)

    if elf1_min <= elf2_max and elf1_max >= elf2_min:
        overlap_count += 1
        continue

    if elf2_min <= elf1_max and elf2_max >= elf1_min:
        overlap_count += 1
        continue

print(f"The part 2 overlap is: {overlap_count}")
