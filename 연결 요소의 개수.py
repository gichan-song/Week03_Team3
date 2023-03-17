import sys

Input = sys.stdin.readline

N, M = map(int, Input().split())

lines = []


for _ in range(M):
    a, b = map(int, Input().split())
    lines.append([a, b])
sets = [set(lines[0])]

for a, b in lines:
    is_in = False
    for i in range(len(sets)):
        if a in sets[i] or b in sets[i]:
            is_in = True
            break
    if not is_in:
        for c, d in lines:
            if a == c or a == d or b == c or b == d:
                is_in = True
                break
            else:
                Set = set([a, b])
                sets.append(Set)
                break
    if is_in:
        for i in range(len(sets)):
            if a in sets[i] or b in sets[i]:
                sets[i].add(a)
                sets[i].add(b)

print(sets)
