# import sys

with open("day1_input.txt") as file:
    ans = 0
    first = sum([int(x) for x in ])
    for line in file:
        # print(line)
        if int(line) > first:
            ans +=1
        first = int(line)
    
    print(ans)