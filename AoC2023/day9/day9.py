D = open("input9.txt").read()
L = D.splitlines()

def f(nums):
    # if len(nums) == 1:
        
    #     return nums[0]
    nums = list(reversed(nums))
    final_diffs = [nums[-1]]
    curr_nums = nums    
    first_diffs = [curr_nums[i+1]-curr_nums[i] for i in range(len(curr_nums)-1)]
    num_differences = len(set(first_diffs))
    final_diffs.append(first_diffs[-1])
    curr_nums = first_diffs    
    while num_differences != 1:
        new_diff = 0
        diffs = []
        for i in range(len(curr_nums)-1):
            new_diff = curr_nums[i+1]-curr_nums[i]
            diffs.append(new_diff)
        # print("Diffs", diffs)
        final_diffs.append(new_diff)
        num_differences = len(set(diffs))
        curr_nums = diffs
    # print(final_diffs)
    
    return sum(final_diffs)
        
ans = 0
for line in L:
    numsS = [int(x) for x in line.split()]
    print(numsS)
    new = f(numsS)
    print(new)
    ans += new
print(ans)