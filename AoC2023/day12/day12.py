D = open("input12.txt").read().splitlines()

ans = 0
for line in D:
    parts, nums = line.split(" ")
    nums = [int(x) for x in nums.split(",")]
    part_groups = parts.split(".")
    while "" in part_groups:
        part_groups.remove("")
    print(parts, nums)
    print(part_groups)
    