import re
D = open("input.txt").readlines()
L = [x.strip() for x in D]

def look_for_ABBA(text: str) -> bool:
    for a,b,c,d in zip(text, text[1:], text[2:], text[3:]):
        if a != b and b == c and d == a:
            return True
    return False
    

def process_line(line: str) -> bool:
    pattern = r"\[([a-z]*)\]"
    matches = re.findall(pattern, line)
    print(matches)
    ABBA_in_square_bracket = any(map(look_for_ABBA, matches))
    if ABBA_in_square_bracket:
        return False
    trimmed = re.sub(pattern, "|", line)
    # print(trimmed)
    acandiate = look_for_ABBA(trimmed)
    return acandiate
    
    
ans = 0
for l in L:
    ans += process_line(l)
print(ans)

def get_ABA_pairs(text: str) -> {tuple[str, str]}:
    ABA_pairs = set()
    for a,b,c in zip(text, text[1:], text[2:]):
        if a != b and c == a:
            ABA_pairs.add((a,b))
    return ABA_pairs

def process_line2(line: str) -> bool:
    pattern = r"\[([a-z]*)\]"
    trimmed = re.sub(pattern, "|", line)
    ABA_pairs = get_ABA_pairs(trimmed)
    matches = re.findall(pattern, line)
    interior_ABA_pairs = set().union(*[get_ABA_pairs(match) for match in matches])
    interior_BAB_pairs = {(x[1],x[0]) for x in interior_ABA_pairs}
    return bool(ABA_pairs.intersection(interior_BAB_pairs))

ans = 0
for l in L:
    ans += process_line2(l)
print(ans)