import sys
from collections import deque

Input = sys.stdin.readline

N, M = map(int, Input().split())

graph = [[] for _ in range(N+1)]

cnt = 0
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, Input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(v):
    visited[v] = True
    q = deque([v])

    while q:
        pop = q.popleft()
        for i in graph[pop]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


for i in range(1, N+1):
    if not visited[i]:
        if not graph[i]:
            visited[i] = True
            cnt += 1
        else:
            bfs(i)
            cnt += 1

print(cnt)