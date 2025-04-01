N, M = map(int, input().split())

E = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, g = map(int, input().split())
    E[u].append((v, g))
    E[v].append((u, g))

import heapq
Q = []
B = [False for _ in range(N + 1)]
V = [False for _ in range(N + 1)]
G = [float('inf') for _ in range(N + 1)]

heapq.heappush(Q, (0, 0, 1))
while Q:
    g, b, u = heapq.heappop(Q)
    if G[u] < g:
        continue

    V[u] = True
    B[u] = b
    G[u] = g

    for v in E[u]:
        if (G[v[0]] <= g + v[1]) or V[v[0]]:
            continue
        
        G[v[0]] = g + v[1]
        heapq.heappush(Q, (g + v[1], u, v[0]))

print(len([0 for i in range(N + 1) if V[i] != False]) - 1)
for i in range(2, N + 1):
    if not V[i]:
        continue

    print(i, B[i])