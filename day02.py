import sys
import copy

data = [int(i) for i in open(sys.argv[1]).read().split(',')]
data2 = copy.copy(data)

for x in range(100):
    for y in range(100):

        data = copy.copy(data2)
        ptr = 0
        data[1] = x
        data[2] = y

        try:
            while data[ptr] != 99:
                if data[ptr] == 1:
                    data[data[ptr+3]] = data[data[ptr+1]] + data[data[ptr+2]]
                elif data[ptr] == 2:
                    data[data[ptr+3]] = data[data[ptr+1]] * data[data[ptr+2]]
                else:
                    print("Invalid opcode")
                    break
                ptr += 4

            if data[0] == 19690720:
                print(100 * x + y)
        except:
            continue
