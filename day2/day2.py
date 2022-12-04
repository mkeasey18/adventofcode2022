# part 1
# with open('day2_inputs.txt') as f:
#     inputs = [[line[0], line[2]] for line in f.readlines()]

# choice_dict = {
#     'X': {
#         'value': 1,
#         'beats': 'C',
#         'draws': 'A'
#     },
#     'Y': {
#         'value': 2,
#         'beats': 'A',
#         'draws': 'B'
#     },
#     'Z': {
#         'value': 3,
#         'beats': 'B',
#         'draws': 'C'
#     },
# }

# total_score = 0

# for opp, player in inputs:
#     total_score += choice_dict[player]['value']
#     if opp in choice_dict[player]['draws']: total_score += 3
#     if opp in choice_dict[player]['beats']: total_score += 6

# print(total_score)
    
# part 2
with open('day2_inputs.txt') as f:
    inputs = [[line[0], line[2]] for line in f.readlines()]

choice_dict = {
    'A': {
        'value': 1,
        'beats': 'C',
        'draws': 'A',
        'loses': 'B'
    },
    'B': {
        'value': 2,
        'beats': 'A',
        'draws': 'B',
        'loses': 'C'
    },
    'C': {
        'value': 3,
        'beats': 'B',
        'draws': 'C',
        'loses': 'A'
    },
}

total_score = 0

for opp, match_end in inputs:
    if match_end == 'X': 
        player = choice_dict[opp]['beats']
    if match_end == 'Y': 
        player = choice_dict[opp]['draws']
        total_score += 3
    if match_end == 'Z': 
        player = choice_dict[opp]['loses']
        total_score += 6
    
    total_score += choice_dict[player]['value']

print(total_score)