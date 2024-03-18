from collections import defaultdict
from itertools import permutations
D = open("input.txt").readlines()
L = [x.strip() for x in D]

distance_map : dict[str, dict[str, int]] = defaultdict(dict)
for l in L:
    words = l.split()
    start, finish, dist = words[0], words[2], int(words[-1])
    distance_map[start][finish] = dist
    distance_map[finish][start] = dist
print(distance_map)
locations = list(distance_map.keys())
# import networkx as nx
# H = nx.Graph(distance_map)
# K8 = nx.complete_graph(n=8)
# import matplotlib.pyplot as plt
# print(nx.is_isomorphic(H, K8))
# nx.draw(H, with_labels=True)
# plt.show()
def cost_perm(perm: list[str]) -> int:
    total_cost = 0
    current_location = perm[0]
    for new_location in perm[1:]:
        cost= distance_map[current_location][new_location]
        total_cost += cost
        current_location = new_location
    return total_cost

costs = set()
ans = 0
for perm in permutations(locations):
    cost = cost_perm(perm)
    costs.add(cost)
    if cost > ans:
        ans = cost
        print(cost)
        print(perm)

print(f"{ans=}")
print(costs)