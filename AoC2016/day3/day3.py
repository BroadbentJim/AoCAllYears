D = open("input.txt").readlines()
L = [l.strip() for l in D]

def process_line(nums: list[int]) -> bool:
    # words = line.split()
    assert len(nums) == 3, len(nums)
    # nums = [int(x) for x in words]
    valid_true = True
    valid_true &= nums[0]+nums[1] > nums[2]
    valid_true &= nums[0]+nums[2] > nums[1]
    valid_true &= nums[1]+nums[2] > nums[0]
    return valid_true

split_lines = [[int(x) for x in line.split()] for line in L]
ans = 0
for l in split_lines:
    ans += process_line(l)
print(ans)

from itertools import zip_longest
def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


ans = 0
for lines in grouper(3, split_lines):
    columns = [[x[i] for x in lines] for i in range(3)]
    # print(columns)
    for col in columns:
        ans += process_line(col)
print(ans)
