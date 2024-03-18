from collections import Counter
D = open("input.txt").readlines()
L = [x.strip() for x in D]

def extract_most_common(most_common: list[tuple[str, int]]) -> str:
    ans = []
    cur_score = most_common[0][1]
    cur_candidates = [most_common[0][0]]
    for item in most_common[1:]:
        if item[1] < cur_score:
            candidates = sorted(cur_candidates)
            ans += candidates[:5-len(ans)]
            cur_score = item[1]
            cur_candidates = [item[0]]
        else:
            cur_candidates.append(item[0])
            
    candidates = sorted(cur_candidates)
    ans += candidates[:5-len(ans)]
    return "".join(ans)
            
# print(extract_most_common([("a", 4), ("b", 3), ("x", 1), ("y",1),("t", 1)]))
def process_line(line: str) -> int:
    dash_sections = line.split("-")
    encrypted_name = dash_sections[:-1]
    # print(encrypted_name)
    counter = Counter("".join(encrypted_name))
    most_common = counter.most_common()
    str_most_common = extract_most_common(most_common)
    sector_id, hash_chars = dash_sections[-1].split("[")    
    sector_id = int(sector_id)
    hash_chars = hash_chars[:-1]
    # print(str_most_common, hash_chars)
    if str_most_common == hash_chars:
        return sector_id
    else:
        return 0
    
ans = 0
for l in L:
    ans += process_line(l)
print(ans)