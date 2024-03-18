from collections import defaultdict
import re
D = open("input.txt").readlines()
L = [x.strip() for x in D]

instructs = L[:-2]
data = L[-1]

dict_actions: dict[str, list[str]] = defaultdict(list)
for instruct in instructs:
    start, finish = instruct.split(" => ")
    dict_actions[start].append(finish)

split_data = re.findall("[A-Z][^A-Z]*", data)
options: set[str] = set()
for i, word in enumerate(split_data):
    for option in dict_actions[word]:
        new = split_data[:i] + [option] + split_data[i+1:]
        new = "".join(new)
        options.add(new)
print(len(options))
# print(dict_actions)
dict_split_actions = {chem: [re.findall("[A-Z][^A-Z]*", data) for data in option] for chem, option in dict_actions.items()}
# print(dict_split_actions)
def shortest_path(current: list[str], target: list[str]) -> int:
    if current == target:
        return 0
    if len(current) >= len(target):
        return False
    min_dist = float('inf')
    for i, chem in enumerate(current):
        for option in dict_split_actions[chem]:
            # print(option)
            new_chem = current[:i] + option + current[i+1:]
            # print(new_chem)
            new_dist = shortest_path(new_chem, target)
            if new_dist is False:
                print(new_chem)
                continue
            new_dist = 1+new_dist
            min_dist = min(min_dist, new_dist)
    return min_dist

print(shortest_path(["e"], split_data))
            

 