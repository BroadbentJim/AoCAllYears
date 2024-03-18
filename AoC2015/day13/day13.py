from collections import defaultdict
from itertools import permutations
D = open("input.txt").readlines()
L = [x.strip() for x in D]

dict_happiness: dict[str, dict[str, int]] = defaultdict(dict)

for l in L:
    words = l.split()
    first, direction, number, target = words[0], words[2], int(words[3]), words[-1]
    target = target[:-1]
    if direction == 'gain':
        number = number
    else:
        number = -number
    dict_happiness[first][target] = number
print(dict_happiness)
people = list(dict_happiness.keys())

def evaluate_assignment(assignment: list[str]) -> int:
    cost = 0
    for person_a, person_b in zip(assignment, assignment[1:]):
        # print(person_a, person_b)
        cost += dict_happiness[person_a][person_b]
        cost += dict_happiness[person_b][person_a]
    cost += dict_happiness[assignment[0]][assignment[-1]] + dict_happiness[assignment[-1]][assignment[0]]
    return cost

# max_happiness= -float('inf')
# first_person = people[0]
# for group in permutations(people[1:]):
#     print(group)
#     assignment = (first_person, *group)
#     score_happiness = evaluate_assignment(assignment)
#     max_happiness = max(max_happiness, score_happiness)
# print(max_happiness)

# pt 2
for dict_person in dict_happiness.values():
    dict_person["You"] = 0
dict_happiness["You"] = {person: 0 for person in people}
people = list(dict_happiness.keys())
max_happiness= -float('inf')
first_person = people[0]
print(dict_happiness)
for group in permutations(people[1:]):
    # print(group)
    assignment = (first_person, *group)
    score_happiness = evaluate_assignment(assignment)
    max_happiness = max(max_happiness, score_happiness)
print(max_happiness)