from collections import defaultdict, Counter
D = open("input.txt").readline().strip()

def do_blink(cur_array: list[int]) -> list[int]:
    i = 0
    while i < len(cur_array):
        cur = cur_array[i]
        if cur == 0:
            cur_array[i] = 1
            i += 1
        elif len(str(cur)) % 2 == 0:
            str_cur = str(cur)
            L = len(str_cur)
            left_num = int(str_cur[:L // 2])
            right_num = int(str_cur[(L // 2):])
            cur_array[i] = left_num
            cur_array.insert(i+1, right_num)
            i += 2
        else:
            new_num = 2024*cur_array[i]
            cur_array[i] = new_num
            i += 1
    return cur_array


def do_blink_dict(cur_dict: dict[int, int]) -> dict[int,int]:
    new_dict = defaultdict(int)
    for loc, num in cur_dict.items():
        if loc == 0:
            new_dict[1] += num
        elif len(str(loc)) % 2 == 0:
            str_cur = str(loc)
            L = len(str_cur)
            left_num = int(str_cur[:L // 2])
            right_num = int(str_cur[(L // 2):])
            new_dict[left_num] += num
            new_dict[right_num] += num
        else:
            new_num = 2024*loc
            new_dict[new_num] += num
    return new_dict

L = [int(x) for x in D.split(" ")]
# for _ in range(25):
#     L = do_blink(L)
#     print(len(L))
# print(len(L))

start_dict = Counter(L)
cur_dict = dict(start_dict)
for _ in range(75):
    cur_dict = do_blink_dict(cur_dict)
print(sum(cur_dict.values()))
