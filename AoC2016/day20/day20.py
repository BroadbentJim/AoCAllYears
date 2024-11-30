D = open("input.txt").readlines()
L = [x.strip() for x in D]

IP_ranges: list[tuple[int,int]] = []
for i, line in enumerate(L):
    lower, upper = [int(x) for x in line.split("-")]
    upper = min(2**32-1, upper)
    IP_ranges.append((lower,upper))

IP_ranges = sorted(IP_ranges)

def merge_ranges(upper_bound: int, IP_ranges: list[tuple[int,int]]) -> tuple[int, list[tuple[int,int]]]:
    initial_len = len(IP_ranges)
    for i, range in enumerate(IP_ranges):
        if range[0] <= upper_bound+1:
            upper_bound = max(upper_bound, range[1])
            IP_ranges.pop(i)
    if len(IP_ranges) == initial_len:
        return upper_bound, IP_ranges
    else:
        return merge_ranges(upper_bound, IP_ranges)

def complete_merge_ranges(IP_ranges: list[tuple[int,int]]) -> list[tuple[int,int]]:
    new_IP_ranges = []
    while IP_ranges:
        start_range = IP_ranges.pop(0)
        lower_bound, upper_bound = start_range[0], start_range[1]
        upper_bound, IP_ranges = merge_ranges(upper_bound, IP_ranges)
        new_IP_ranges.append((lower_bound, upper_bound))
    return new_IP_ranges
# start_range = IP_ranges.pop(0)
# print(start_range)
# upper_bound = start_range[1]
# upper_bound, IP_ranges = merge_ranges(upper_bound, IP_ranges)
# print(upper_bound)
# print(upper_bound+1)

new_IP_ranges = complete_merge_ranges(IP_ranges)
widths = sum([x[1]-x[0]+1 for x in new_IP_ranges])
answer = 2**32 - widths
print(answer)
