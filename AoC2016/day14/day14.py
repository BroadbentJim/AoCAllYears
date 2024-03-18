from hashlib import md5
from functools import cache

INPUT = "cuanljph"
# INPUT = "abc"
TARGET_KEYS = 64
CHECK_NEXT = 1000

@cache
def hash_int(num: int) -> str:
    str_input = (INPUT + str(num)).encode()
    hash = md5(str_input).hexdigest()
    # pt 2
    for _ in range(2016):
        hash = md5(hash.encode()).hexdigest()
    return hash

@cache
def get_5_repeats(text: str) -> set[str]:
    repeats = set()
    for a,b,c,d,e in zip(text, text[1:], text[2:], text[3:], text[4:]):
        if len(set([a,b,c,d,e])) == 1:
            repeats.add(a)
    return repeats

CUR_KEYS = 0
cur_int = 0
while CUR_KEYS < TARGET_KEYS:
    str_hash = hash_int(cur_int)
    triple_chars = set()
    for a,b,c in zip(str_hash, str_hash[1:], str_hash[2:]):
        if a == b and b == c:
            triple_chars.add(a)
            break
    for i in range(cur_int+1, cur_int+CHECK_NEXT):
        new_hash = hash_int(i)
        five_repeats = get_5_repeats(new_hash)
        if triple_chars.intersection(five_repeats):
            CUR_KEYS += 1
            print("FOUND A 5", cur_int, i, triple_chars, five_repeats)
            break
    cur_int += 1
        
print("ANSWER")
print(cur_int-1)