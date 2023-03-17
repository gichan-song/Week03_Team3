import sys

Input = sys.stdin.readline

V, E = map(int, Input().split())

edges = []
for _ in range(E):
    edges.append(list(map(int, Input().split())))

edges.sort(key=lambda x: x[2])

parent = []
answer = 0

for i in range(V+1):
    parent.append(i)


def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]


def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for a, b, cost in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost

print(answer)