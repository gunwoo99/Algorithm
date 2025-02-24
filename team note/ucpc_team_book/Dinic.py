from collections import deque

N = 1
F = [[0 for _ in range(N)] for _ in range(N)]
L = [-1 for _ in range(N)]
P = [ 0 for _ in range(N)]
ADJ = [[] for _ in range(N)]
S, E = 0, N - 1

def bfs(S, E):
    global L
    L = [-1 for _ in range(N)]
    L[S] = 0
    queue = deque([S])
    while queue:
        u = queue.popleft()
        for v in ADJ[u]:
            if L[v] == -1 and F[u][v]:
                L[v] = L[u] + 1
                queue.append(v)
    return L[E] != -1

def dfs(u, f, E):
    global P
    if u == E:
        return f
    
    while P[u] <= E:
        v = P[u]
        if L[u] < L[v] and F[u][v]:
            add = dfs(v, min(f, F[u][v]), E)
            if add:
                F[u][v] -= add
                F[v][u] += add
                return add
        P[u] += 1
    return 0

MF = 0
while bfs(S, E):
    P = [0 for _ in range(N + 2)]
    while add := dfs(S, float('inf'), E):
        MF += add