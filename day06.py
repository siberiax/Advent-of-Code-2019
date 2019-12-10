import sys
from collections import defaultdict
data = open(sys.argv[1]).read().split()

c_to_p = defaultdict()
orbits = defaultdict(list)
left = set()

for el in data:
    fields = el.split(')')
    orbits[fields[0]].append(fields[1])
    left.add(fields[1])
    c_to_p[fields[1]] = fields[0]

queue =  []

for k in orbits.keys():
    if k not in left:
        queue.append(k)

total = 0
iter =  0
while queue:
    new  = []
    for el in queue:
        total += iter
        if el in orbits:
            new.extend(orbits[el])

    iter += 1
    queue = new

print(total)

start = "YOU"
end  = "SAN"
searched = set(start)

curr  = c_to_p[start]
total = 0

while end not in orbits[curr]:
    old_total = total
    queue = orbits[curr]
    found = 0
    while queue:
        new = []
        for node in queue:
            if node not in searched:
                searched.add(node)
                new.extend(orbits[node])
            if node == end:
                found = 1
                break

        if found:
            break
        total +=1
        queue = new

    if found:
        break
    total = old_total
    total += 1
    curr = c_to_p[curr]

print(total)
