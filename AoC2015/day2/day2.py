D = open("input.txt")
lines = [l.strip() for l in D.readlines()]

ans = 0
for line in lines:
    x,y,z = [int(x) for x in line.split("x")]
    surface_area = 2*(x*y+x*z+y*z)
    smallest_side = x*y*z / max(x,y,z)
    ans += surface_area + smallest_side
print(ans)

ans = 0
for line in lines:
    x,y,z = [int(x) for x in line.split("x")]
    wrapping = 2*(x+y+z-max(x,y,z))
    bow = x*y*z
    ans += wrapping + bow
print(ans)