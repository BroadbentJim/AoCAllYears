from math import sqrt, floor, ceil
D = open("input6.txt").read().strip().splitlines()
print(D)
# times = [int(x) for x in D[0].split(":")[1].split()]
time = int("".join(D[0].split(":")[1].split()))
distance = int("".join(D[1].split(":")[1].split()))
# print(times, distances)
ans = 1
# for time, distance in zip(times, distances):
record_beaters = 0
discrim = time**2 - 4*distance
sqrt_discrim = sqrt(discrim)
if int(sqrt_discrim) == sqrt_discrim:
    print(sqrt_discrim-1)
    ans *= sqrt_discrim-1
else:
    # print((time-sqrt_discrim)/2, (time+sqrt_discrim)/2)
    lower = ceil((time-sqrt_discrim)/2)
    upper = floor((time+sqrt_discrim)/2)
    new = upper-lower+1
    print(new)
    ans *= new
print(int(ans))