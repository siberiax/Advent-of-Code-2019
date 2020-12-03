import sys
from collections import defaultdict

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

curr = (0,0)
grid = {}
grid[curr] = [1,2,3,4]
chain = [(0,0)]

inp = 1
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
            data[data[ptr+1]] = inp
        elif op1 == "2":
            data[rel_ptr + data[ptr+1]] = inp
        else:
            data[ptr+1] = inp

        ptr += 2

    elif inst[-1] == "4":
        ds = getParams([op1])
        d1 = ds[0]
        print(d1)
        inp = int(input("Enter: "))

        # if d1 == 0:
        #     grid[curr] = grid[curr][1:]
        #     while not len(grid[curr]):
        #         chain = chain[:-1]
        #         curr = chain[-1]
        #     input = gird[curr][0]
        # else:
        #     if input == 1:
        #         curr[0] -= 1
        #         grid[curr] = [1,3,4]
        #     elif input == 2:
        #         curr[0] += 1
        #         grid[curr] = [2,3,4]
        #     elif input == 3:
        #         curr[1] -= 1
        #         grid[curr] = [1,2,3]
        #     else:
        #         curr[1] += 1
        #         grid[curr] = [1,2,4]
        #     chain.append(curr)
        #     if d1 == 2:
        #         print(len(chain))
        #         break

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
