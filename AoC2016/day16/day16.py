from copy import deepcopy
INPUT = "11110010111001001"
DISK_LENGTH = 35651584

def extend_string(text: str) -> str:
    text_2 = deepcopy(text)
    text_2 = reversed(text_2)
    text_2 = "".join(map(lambda x: "0" if x == "1" else "1", text_2))
    
    ans = text + "0" + text_2
    return ans

text = INPUT
while len(text) < DISK_LENGTH:
    text = extend_string(text)
    
def calculate_checksum(text: str) -> str:
    ans = []
    for i in range(0, len(text), 2):
        a,b = text[i], text[i+1]
        if a == b:
            ans.append("1")
        else:
            ans.append("0")
    str_ans = "".join(ans)
    if len(ans) % 2 == 0:
        return calculate_checksum(str_ans)
    return str_ans

print(calculate_checksum("110010110100"))
print("ANSWER")
print(calculate_checksum(text[:DISK_LENGTH]))
