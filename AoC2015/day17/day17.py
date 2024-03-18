from functools import cache
D = open("input.txt").readlines()
L = [l.strip() for l in D]

container_sizes = tuple([int(x) for x in L])
TARGET = 150

@cache
def sum_to_target(input_list: tuple[int], target: int) -> list[int]:
    if target < 0:
        return []
    if len(input_list) == 0:
        return [0] if target == 0 else []
    if input_list[0] > target:
        return sum_to_target(input_list[1:], target)
    incl_first = [x+ 1 for x in sum_to_target(input_list[1:], target-input_list[0])]
    excl_first = sum_to_target(input_list[1:], target)
    return incl_first + excl_first

solutions = (sum_to_target(container_sizes, TARGET))
print(len(solutions))
shortest_path = min(solutions)
ans = solutions.count(shortest_path)
print(ans)