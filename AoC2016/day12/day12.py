from collections import defaultdict
D = open("input.txt").readlines()
L = [x.strip() for x in D]
    
registers = defaultdict(int)
registers["c"] = 1 #pt2
cur_instr = 0
while 0 <= cur_instr and cur_instr < len(L):
    line = L[cur_instr]
    words = line.split()
    match words[0]:
        case "inc":
            target = words[1]
            registers[target] += 1
            cur_instr += 1
        case "dec":
            target = words[1]
            registers[target] -= 1
            cur_instr += 1
        case "cpy":
            target = words[2]
            source = words[1]
            if source in ["a", "b", "c", "d"]:
                registers[target] = registers[source]
            else:
                value =int(source)
                registers[target] = value
            cur_instr += 1
        case "jnz":
            source = words[1]
            value : int = None
            if source in ["a", "b", "c", "d"]:
                value = registers[source]
            else:
                value = int(source)
            if value != 0:
                step = words[2]
                cur_instr += int(step)
            else:
                cur_instr += 1
print(registers["a"])
    
