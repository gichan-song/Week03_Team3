import sys

Input = sys.stdin.readline

coms = int(Input())
connections = int(Input())

graph = [[] for _ in range(coms+1)]
visited = [False] * (coms+1)

for _ in range(connections):
    a, b = map(int, Input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


dfs(1)

print(visited.count(True)-1)
