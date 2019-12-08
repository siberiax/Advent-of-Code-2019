import sys
import copy

positions = {}

data = open(sys.argv[1]).read().split()

wire1 = data[0].split(',')
wire2 = data[1].split(',')

def makeWire(wire, b):
    curr = [0,0]
    smallest = 999999
    total = 1
    for direction in wire:
        dir = direction[0]
        paces = int(direction[1:])

        for i in range(paces):
            if dir == 'L':
                curr[0] -= 1
            elif dir == 'R':
                curr[0] += 1
            elif dir == 'U':
                curr[1] += 1
            else:
                curr[1] -= 1

            if str(curr) in positions and b:
                # if abs(curr[0]) + abs(curr[1]) < smallest:
                #     smallest = abs(curr[0]) + abs(curr[1])
                if positions[str(curr)] + total < smallest:
                    smallest = positions[str(curr)] + total
            if not b:
                positions[str(curr)] = total

            total += 1

    return smallest


makeWire(wire1, 0)
print(makeWire(wire2, 1))
