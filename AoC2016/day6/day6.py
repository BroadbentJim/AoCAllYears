from collections import defaultdict, Counter
D = open("input.txt").readlines()
L = [x.strip() for x in D]

W = len(L[0])
data_store = [Counter() for _ in range(W)]

def process_line(line: str):
    for i, char in enumerate(line):
        data_store[i].update(char)

for line in L:
    process_line(line)

ans = []
for counter in data_store:
    print(counter.most_common(1))
    ans += counter.most_common(1)[0][0]
print(ans)
print("".join(ans))

ans = []
for counter in data_store:
    ans += counter.most_common()[-1][0]
print(ans)
print("".join(ans))