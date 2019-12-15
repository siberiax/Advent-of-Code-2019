import sys
from collections import deque, defaultdict

def getThird(op):
    if op == "2":
        return rel_ptr + data[ptr + 3]
    else:
        return data[ptr + 3]

def getParams(ops):
    ret = []
    for i, op in enumerate(ops):
        i += 1
        if op == "0":
            ret.append(data[data[ptr+i]])
        elif op == "2":
            ret.append(data[rel_ptr + data[ptr+i]])
        else:
            ret.append(data[ptr+i])

    return ret

filedata = [int(i) for i in open(sys.argv[1]).read().split(',')]

data = defaultdict(int)
for i, d in enumerate(filedata):
    data[i] = d

directions = deque(('u', 'r', 'd', 'l'))
panels = defaultdict(int)
curr = [0,0]
output_switch = 0

min_x = 0
min_y = 0
max_x = 0
max_y  = 0

input = 1
ptr = 0
rel_ptr = 0
while data[ptr] != 99:
    inst = str(data[ptr])
    inst = "0" * (5 - len(inst)) + inst

    op1 = inst[2]
    op2 = inst[1]
    op3 = inst[0]

    if inst[-1] == "1":
        ds = getParams([op1, op2])
        d1, d2  = ds[0], ds[1]
        d3 = getThird(op3)
        data[d3] = d1 + d2
        ptr += 4

    elif inst[-1] == "2":
        ds = getParams([op1, op2])
        d1, d2  = ds[0], ds[1]
        d3 = getThird(op3)
        data[d3] = d1 * d2
        ptr += 4

    elif inst[-1] == "3":
        if op1 == "0":
            data[data[ptr+1]] = input
        elif op1 == "2":
            data[rel_ptr + data[ptr+1]] = input
        else:
            data[ptr+1] = input

        ptr += 2

    elif inst[-1] == "4":
        ds = getParams([op1])
        d1 = ds[0]

        if output_switch == 0:
            output_switch = 1
            panels[str(curr)] = d1
        else:
            output_switch = 0
            if d1 == 0:
                directions.rotate()
            else:
                directions.rotate(-1)

            if directions[0] == 'u':
                curr[1] -= 1
            elif directions[0] == 'l':
                curr[0] -= 1
            elif directions[0] == 'd':
                curr[1] += 1
            else:
                curr[0] += 1

            input = panels[str(curr)]

            if curr[0] < min_x:
                min_x = curr[0]
            elif curr[0] > max_x:
                max_x = curr[0]

            if curr[1] < min_y:
                min_y = curr[1]
            elif  curr[1] > max_y:
                max_y = curr[1]

        ptr += 2

    elif inst[-1] == "5":
        ds = getParams([op1, op2])
        d1, d2  = ds[0], ds[1]
        if d1 > 0:
            ptr = d2
        else:
            ptr += 3

    elif inst[-1] == "6":
        ds = getParams([op1, op2])
        d1, d2 = ds[0], ds[1]
        if d1 == 0:
            ptr = d2
        else:
            ptr += 3

    elif inst[-1] == "7":
        ds = getParams([op1, op2])
        d1, d2 = ds[0], ds[1]
        d3 = getThird(op3)
        if d1 < d2:
            data[d3] = 1
        else:
            data[d3] = 0
        ptr += 4

    elif inst[-1] == "8":
        ds = getParams([op1, op2])
        d1, d2 = ds[0], ds[1]
        d3 = getThird(op3)
        if d1 == d2:
            data[d3] = 1
        else:
            data[d3] = 0
        ptr += 4

    elif inst[-1] == "9":
        ds = getParams([op1])
        d1 = ds[0]
        rel_ptr += d1

        ptr += 2

#print(len(panels.keys()))

for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        if panels[str([x,y])] == 0:
            print(' ', end = '')
        else:
            print('0', end = '')
    print()
