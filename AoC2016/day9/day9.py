D = open("input.txt").readlines()
L = [x.strip() for x in D]
text = L[0]
ans = []
in_paren = False
paren_left = -1
paren_right = -1

def process_marker(left, right: int) -> tuple[str, int]:
    A,B = [int(x) for x in text[left+1:right].split("x")]
    bonus = text[right+1:right+1+A]
    ans = bonus * B
    return ans,right+A
i = 0
while i < len(text):
    char = text[i]
    if not in_paren and char != "(":
        ans.append(char)
    elif char == "(":
        assert not in_paren and paren_left == -1
        in_paren = True
        paren_left = i
    elif in_paren and char == ")":
        assert paren_left != -1
        paren_right = i
        bonus, i = process_marker(paren_left, paren_right)
        ans.append(bonus)
        paren_left = -1
        paren_right = -1
        in_paren = False
    i += 1
text_ans = "".join(ans)
print(text_ans)
print(len(text_ans))