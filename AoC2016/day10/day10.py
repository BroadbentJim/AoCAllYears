from dataclasses import dataclass
D = open("input.txt").readlines()
L = [x.strip() for x in D]

@dataclass
class Instruction:
    index: int
    low_dir: tuple[str, int]
    high_dir: tuple[str, int]

@dataclass
class Bot:
    index: int
    values: list[int]
    instruction: Instruction | None = None
    
robot_store: dict[int, Bot] = {}
output_store: dict[int, int] = {}
start_index = -1

for line in L:
    words = line.split()
    if words[0] == "value":
        value = int(words[1])
        target = int(words[-1])
        if target in robot_store:
            robot_store[target].values.append(value)
            if len(robot_store[target].values) == 2:
                assert start_index == -1
                start_index = target
        else:
            new_bot = Bot(index=target, values=[value])
            robot_store[target] = new_bot
        continue
    index = int(words[1])
    low_dir = words[5:7]
    low_dir = (low_dir[0], int(low_dir[1]))
    high_dir = words[-2:]
    high_dir = (high_dir[0], int(high_dir[1]))
    instruction = Instruction(index, low_dir, high_dir)
    if index in robot_store:
        assert robot_store[index].instruction is None
        robot_store[index].instruction = instruction
    else:
        new_bot = Bot(index=index, values=[], instruction=instruction)
        robot_store[index] = new_bot
# print(robot_store)
    
task_queue: list[int] = [start_index]

def pass_value(pass_val: int, dir_data: tuple[str, int], bot_store: dict[int, Bot], output_store: dict[int, int]):
    if dir_data[0] == "bot":
        target = bot_store[dir_data[1]]
        target.values.append(pass_val)
        if len(target.values) == 2:
            task_queue.append(dir_data[1])
    elif dir_data[0] == "output":
        output_store[dir_data[1]] = pass_val

def process_instruction(bot: Bot, bot_store: dict[int, Bot], output_store: dict[int, int]):
    instr = bot.instruction
    if set(bot.values) == {17, 61}:
        print("ANSWER")
        print(bot.index)
    sorted_values = sorted(bot.values)
    low_val = sorted_values.pop(0)
    pass_value(low_val, instr.low_dir, bot_store, output_store)
    high_val = sorted_values.pop(0)
    pass_value(high_val, instr.high_dir, bot_store, output_store)

while task_queue:
    cur_worker = task_queue.pop()
    bot = robot_store[cur_worker]
    process_instruction(bot, robot_store, output_store)
print(output_store)
    
ans = output_store[0] * output_store[1] * output_store[2]
print(ans)