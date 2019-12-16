import sys
import re
from math import gcd

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def step():
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

def makeState():
    state = []
    for i in range(len(moons)):
        state.append(moons[i][dim])
        state.append(vels[i][dim])
    return str(state)

data = [line for line in open(sys.argv[1])]

moons = []
vels = []
for d in data:
    pos = re.findall(r'-?\d+',d)
    moons.append([int(i) for i in pos])
    vels.append([0,0,0])

for _ in range(1000):
    step()

total_energy = 0

for i in range(len(moons)):
    m = moons[i]
    v = vels[i]
    pot = 0
    kin = 0
    for x in range(3):
        pot += abs(m[x])
        kin += abs(v[x])

    total_energy += pot * kin

print(total_energy)

xyz = []
for dim in range(3):
    seen = {}
    steps = 0

    state = makeState()

    while state not in seen:
        seen[state] = 1
        steps += 1
        step()

        state = makeState()

    xyz.append(steps)

print(lcm(lcm(xyz[0], xyz[1]), xyz[2]))
