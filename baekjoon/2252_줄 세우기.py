N, M = map(int, input().split())

E = [[] for _ in range(N + 1)]
D = [0 for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    D[v] += 1

from collections import deque
Q = deque([i for i in range(1, N + 1) if D[i] == 0])

ans = []
while Q:
    u = Q.pop()

    ans.append(u)
    for v in E[u]:
        D[v] -= 1
        if D[v] == 0:
            Q.append(v)

print(*ans)