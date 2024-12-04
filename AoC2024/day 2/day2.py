D = open("input2.txt").read().splitlines()

ans = 0
for line in D:
    levels = [int(x) for x in line.split()]
    a,b = levels[:2]
    increasing = True    
    if a == b or abs(b-a) > 3:
        continue
    if a < b:
        increasing = True
    else:
        increasing = False
    for left, right in zip(levels[1:], levels[2:]):
        if left == right or abs(right-left) > 3:
            break
        if (increasing and (right - left < 0)) or (not increasing and (right-left > 0)):
            break
    else:
        ans += 1
print(ans)

def process_level(levels, has_removed = False):
    has_removed
    a,b = levels[:2]
    if not has_removed:
        g = max(process_level(levels[1:], True), process_level([levels[0]] + levels[2:], True))
        if g:
            return g
    if a == b or abs(b-a) > 3:
        if has_removed:
            return 0
        return max(process_level(levels[1:], True), process_level([levels[0]] + levels[2:], True))
    if a < b:
        increasing = True
    else:
        increasing = False
    
    for i, coords in enumerate(zip(levels[1:], levels[2:])):
        left, right = coords
        if left == right or abs(right-left) > 3:
            if has_removed:
                return 0
            return max(process_level(levels[:i+1] + levels[i+2:], True), process_level(levels[:i+2] + levels[i+3:], True))
        if (increasing and (right - left < 0)) or (not increasing and (right-left > 0)):
            if has_removed:
                return 0
            return max(process_level(levels[:i+1] + levels[i+2:], True), process_level(levels[:i+2] + levels[i+3:], True))
    else:
        return 1


ans = 0
for line in D:
    levels = [int(x) for x in line.split()]
    ans += process_level(levels, False)
print(ans)