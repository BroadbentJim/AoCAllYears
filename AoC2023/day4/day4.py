import re
D = open("input4.txt")
N_cards = 223
print(D)
total_cards = 0
extra_work = [1] * N_cards

for i, line in enumerate(D):
    print(extra_work)
    line = line.split(":")[1]
    # print(line)
    left,right = line.split("|")
    winning_numbers = []
    for match in re.finditer(r"\d+",left):
        winning_numbers.append(match.group(0))
    # print(winning_numbers)
    c =0
    for match in re.finditer(r"\d+",right):
        num = match.group(0)
        if num in winning_numbers:
            c += 1
    num_cards = extra_work[i]
    for j in range(i+1, min(i+c+1, N_cards)):
        extra_work[j] += num_cards
    total_cards += num_cards

print(total_cards)