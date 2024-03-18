from dataclasses import dataclass
D = open("input.txt").readlines()
L = [x.strip() for x in D]

@dataclass
class Disc:
    positions: int
    offset: int
    
disc_store: list[Disc] = []   

def process_line(text: str):
    words = text.split()
    positions = int(words[3])
    offset = int(words[-1][:-1])
    new_disc = Disc(positions=positions, offset=offset)
    disc_store.append(new_disc)
    
for line in L:
    process_line(line)
print(disc_store)    
"""
Methodology:
CRT.
Find the least T s.t:
offset_i + T+i == 0 mod positions_i
"""
from functools import reduce

def mul_inv(a, b):
    b0 = b
    x0,x1 = 0,1
    if b== 1: return 1
    while a > 1:
        q = a // b
        a,b = b, a%b
        x0,x1 = x1-q*x0, x0
    if x1 < 0: x1 += b0
    return x1

def CRT(discs: list[Disc]):
    sum = 0
    prod = reduce(lambda x, y: x*y, [x.positions for x in discs])
    for i, disc in enumerate(discs):
        pos, offset = disc.positions, disc.offset
        offset += i+1
        offset %= pos
        p = prod // pos
        sum += offset * mul_inv(p, pos) * p
    return sum % prod

print(CRT(disc_store))