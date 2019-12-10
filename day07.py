import sys
from itertools import permutations
from copy import copy

def getParams(op1, op2):
    if op1 == "0":
        d1 = data[data[ptr+1]]
    else:
        d1 = data[ptr+1]

    if op2 == "0":
        d2 = data[data[ptr+2]]
    else:
        d2 = data[ptr+2]

    return d1, d2

data = [int(i) for i in open(sys.argv[1]).read().split(',')]

original = copy(data)

phases = [0,1,2,3,4]
input = 0
ptr = 0

highest = 0

for p in permutations(phases):
    for phase in p:
        phase_flag = 1
        while data[ptr] != 99:

            inst = str(data[ptr])
            inst = "0" * (5 - len(inst)) + inst

            op1 = inst[2]
            op2 = inst[1]
            op3 = inst[0]

            if inst[-1] == "1":
                d1, d2 = getParams(op1, op2)
                data[data[ptr+3]] = d1 + d2
                ptr += 4

            elif inst[-1] == "2":
                d1, d2 = getParams(op1, op2)
                data[data[ptr+3]] = d1 * d2
                ptr += 4

            elif inst[-1] == "3":
                if phase_flag:
                    data[data[ptr+1]] = phase
                    phase_flag = 0
                else:
                    data[data[ptr+1]] = input
                ptr += 2

            elif inst[-1] == "4":
                input = data[data[ptr+1]]
                ptr += 2

            elif inst[-1] == "5":
                d1, d2 = getParams(op1, op2)
                if d1 > 0:
                    ptr = d2
                else:
                    ptr += 3

            elif inst[-1] == "6":
                d1, d2 = getParams(op1, op2)
                if d1 == 0:
                    ptr = d2
                else:
                    ptr += 3

            elif inst[-1] == "7":
                d1, d2 = getParams(op1, op2)
                if d1 < d2:
                    data[data[ptr+3]] = 1
                else:
                    data[data[ptr+3]] = 0
                ptr += 4

            elif inst[-1] == "8":
                d1, d2 = getParams(op1, op2)
                if d1 == d2:
                    data[data[ptr+3]] = 1
                else:
                    data[data[ptr+3]] = 0
                ptr += 4

        data = copy(original)
        ptr = 0

    if input > highest:
        highest = input
    input = 0

print(highest)
