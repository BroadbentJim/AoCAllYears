target = "36000000"
# target = "1000"
low_target = int(target) // 10

def sum_divisors(n: int) -> int:
    ans = 0
    for i in range(1,n//2 + 1):
        if n % i == 0:
            ans += i
    return ans

i= 10
while True:
    score = sum_divisors(i)
    if score > low_target:
        print(i)
        break
    i *= 10
    
def binary_search(lower, upper):
    if upper - lower == 1:
        return upper
    mid_point = lower+upper // 2
    score = sum_divisors(mid_point)
    if score >= low_target:
        binary_search(lower, mid_point)
    else:
        binary_search(mid_point, upper)
        
ans = binary_search(i //10, i)
print("ANS: ans")