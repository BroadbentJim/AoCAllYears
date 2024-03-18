from collections import Counter
from bisect import insort, bisect
D = open("input7.txt").read().strip()



ans = 0
sorted_hands = []
D =D.replace("A", "E")
D =D.replace("K", "D")
D =D.replace("Q", "C")
D =D.replace("J", "1")
D =D.replace("T", "A")
L = D.splitlines()
print(len(L))
hand_type = [""] * len(L)
for i, line in enumerate(L):
    hand, bid = line.split()
    count_hand = Counter(hand)
    if set(hand) == set("1"):
        print(hand)
        hand_type[i] = "5"
        insort(sorted_hands, (hand_type[i], hand))
        continue
    if "1" in count_hand:
        # print(hand)
        if count_hand.most_common()[0][0] == "1":
            count_hand[count_hand.most_common()[1][0]] += count_hand["1"]
        else:
            count_hand[count_hand.most_common()[0][0]] += count_hand["1"]
        del count_hand["1"]
        # print(count_hand)
    counts = [x[1] for x in count_hand.most_common()]

    if len(counts) == 1:
        hand_type[i] = "5"
    elif counts[0] == 4:
        hand_type[i] = "4"
    elif len(counts) == 2:
        hand_type[i] = "3FH"
    elif counts[0] == 3:
        hand_type[i] = "3"
    elif counts[0] == 2 and counts[1] == 2:
        hand_type[i] = "2P"
    elif counts[0] == 2:
        hand_type[i] = "2"
    else:
        hand_type[i] = "0"
    insort(sorted_hands, (hand_type[i], hand))
hands = [x.split()[0] for x in L]
# sorted_hands = sorted(list(zip(hand_type, hands)))
print(sorted_hands)
for i, line in enumerate(L):
    hand, bid = line.split()
    sorter = (hand_type[i], hand)
    rank = bisect(sorted_hands, sorter)
    # print(i, hand, sorter, bid, rank)
    ans += rank * int(bid)
print(ans)