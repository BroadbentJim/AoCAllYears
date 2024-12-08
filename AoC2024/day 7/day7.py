D = open("input.txt").readlines()



def solve_row(nums, target, cur_val=0):
    if cur_val == 0:
        if len(nums) == 0 and target == 0:
            return True
        if len(nums) == 1 and target == nums[0]:
            return True
        num_1, num_2 = nums[0], nums[1]
        mul_ans = False
        if num_1*num_2 <= target:
            mul_ans = solve_row(nums[2:], target, num_1*num_2)
        sum_ans = False
        if num_1+num_2 <= target:
            sum_ans = solve_row(nums[2:], target, num_1+num_2)
        return mul_ans or sum_ans
    if not nums:
        return cur_val == target
    mul_ans = False
    if nums[0]*cur_val <= target:
        mul_ans = solve_row(nums[1:], target, cur_val*nums[0])
    sum_ans = False
    if nums[0]+cur_val <= target:
        sum_ans = solve_row(nums[1:], target, cur_val+nums[0])
    return mul_ans or sum_ans
    
    
def solve_row_2(nums, target, cur_val=0):
    if cur_val == 0:
        if len(nums) == 0 and target == 0:
            return True
        if len(nums) == 1 and target == nums[0]:
            return True
        num_1, num_2 = nums[0], nums[1]
        mul_ans = False
        if num_1*num_2 <= target:
            mul_ans = solve_row_2(nums[2:], target, num_1*num_2)
        sum_ans = False
        if num_1+num_2 <= target:
            sum_ans = solve_row_2(nums[2:], target, num_1+num_2)
        concat_ans = False
        concat = int(str(num_1)+ str(num_2))        
        if concat <= target:           
            concat_ans = solve_row_2(nums[2:], target, concat)
        return mul_ans or sum_ans or concat_ans
    if not nums:
        return cur_val == target
    mul_ans = False
    if nums[0]*cur_val <= target:
        mul_ans = solve_row_2(nums[1:], target, cur_val*nums[0])
    sum_ans = False
    if nums[0]+cur_val <= target:
        sum_ans = solve_row_2(nums[1:], target, cur_val+nums[0])
    concat_ans = False
    concat = int(str(cur_val)+ str(nums[0]))
    if concat <= target:
        concat_ans = solve_row_2(nums[1:], target, concat)
    return mul_ans or sum_ans or concat_ans



ans = 0
for l in [x.strip() for x in D]:
    left,right = l.split(':')
    target =  int(left)
    nums = [int(x) for x in right[1:].split(' ')]
    # print(left, nums)
    if solve_row(nums, target):
        ans += target
print(ans)


ans = 0
for l in [x.strip() for x in D]:
    left,right = l.split(':')
    target =  int(left)
    nums = [int(x) for x in right[1:].split(' ')]
    # print(left, nums)
    if solve_row_2(nums, target):
        print(nums, target)
        ans += target
print(ans)