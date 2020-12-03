import sys
from collections import defaultdict
from math import gcd

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

data = [line.strip() for line in open(sys.argv[1])]

formulas = defaultdict(list)

how_many = defaultdict(int)

for form in data:
    fields = form.split(' => ')
    fields1 = fields[0].split(', ')
    f2 = fields[1].split()
    f2[0] = int(f2[0])
    res = tuple(f2)
    for f in fields1:
        f2 = f.split()
        f2[0] = int(f2[0])
        formulas[res].append(tuple(f2))
        how_many[f2[1]] += f2[0]

queue = []
for k in formulas.keys():
    if k[1] == 'FUEL':
        queue.append(k)
        break
#
# while queue:
#     new = []
#     for el in queue:
#         curr = 0
#         for k in formulas.keys():
#             if k[1] == el[1]:
#                 curr = k
#                 break
#         amt = el[0]
#         for val in formulas[curr]:
#             new.append()
