INPUT = 3018458

def MSB(n):
    pos = 0
    while n != 0:
        pos += 1
        n = n >> 1
    return pos

def josephus(n):
    pos =  MSB(n)
    j = 1 << (pos-1)
    n = n ^ j
    n = n << 1
    n = n | 1
    return n

print(josephus(5))
print(josephus(INPUT))