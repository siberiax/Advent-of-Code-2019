import sys
import re
from math import gcd

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

data = [line for line in open(sys.argv[1])]

moons = []
vels = []
for d in data:
    pos = re.findall(r'-?\d+',d)
    moons.append([int(i) for i in pos])
    vels.append([0,0,0])

xyz = []
for dim in range(3):
    seen = {}
    steps = 0

    state = []
    for i in range(len(moons)):
        state.append(moons[i][dim])
        state.append(vels[i][dim])

    state = str(state)

    while state not in seen:
        seen[state] = 1
        steps += 1
        for i in range(len(moons)):
            for j in range(len(moons)):
                if i == j:
                    continue
                m1 = moons[i]
                m2 = moons[j]
                for x in range(3):
                     if m1[x] > m2[x]:
                         vels[i][x] -= 1
                     elif m1[x] < m2[x]:
                         vels[i][x] += 1

        for i in range(len(moons)):
            for x in range(3):
                moons[i][x] += vels[i][x]

        state = []
        for i in range(len(moons)):
            state.append(moons[i][dim])
            state.append(vels[i][dim])

        state = str(state)

    xyz.append(steps)

print(lcm(lcm(xyz[0], xyz[1]), xyz[2]))
