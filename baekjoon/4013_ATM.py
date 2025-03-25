
import sys
sys.setrecursionlimit(200000)

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    E[u - 1].append(v - 1)

H = [int(input()) for _ in range(N)]

S, P = map(int, input().split())
RN = list(map(int, input().split()))

def scc(edge, n):
    from collections import deque
    grouped = [False for _ in range(n)]
    level_of = [False for _ in range(n)]
    stack = deque([])
    level = 0
    groups = []

    def dfs(u):
        nonlocal level
        nonlocal groups
        level += 1
        last_level = level_of[u] = level

        stack.append(u)
        for v in edge[u]:
            if not level_of[v]:
                last_level = min(last_level, dfs(v))
            elif not grouped[v]:
                last_level = min(last_level, level_of[v])
        
        if last_level == level_of[u]:
            group = []
            while stack:
                p = stack.pop()
                group.append(p)
                grouped[p] = True
                if u == p:
                    break
            
            groups.append(group)
        return last_level

    for i in range(n):
        if not grouped[i]:
            dfs(i)
    
    return groups

groups = scc(E, N)
scc_num = len(groups)
U_SCC = [0 for _ in range(N)]
for i, group in enumerate(groups):
    for u in group:
        U_SCC[u] = i

SCC_C = [False for _ in range(scc_num)]
for i in range(P):
    SCC_C[U_SCC[RN[i] - 1]] = True

SCC_E = [set() for _ in range(scc_num)]
SCC_D = [0 for _ in range(scc_num)]
SCC_H = [0 for _ in range(scc_num)]
for i, group in enumerate(groups):
    for u in group:
        SCC_H[i] += H[u]
        for v in E[u]:
            if U_SCC[u] == U_SCC[v]:
                continue
            SCC_E[i].add(U_SCC[v])
    SCC_E[i] = list(SCC_E[i])

for SCC_u in SCC_E:
    for v in SCC_u:
        SCC_D[v] += 1

SCC_V = [False for _ in range(scc_num)]
def scc_dfs(u):
    SCC_V[u] = True

    for v in SCC_E[u]:
        if SCC_V[v]:
            continue

        scc_dfs(v)

scc_dfs(U_SCC[S - 1])
for i in range(scc_num):
    if SCC_V[i]:
        continue

    for v in SCC_E[i]:
        SCC_D[v] -= 1

from collections import deque
Q = deque([U_SCC[S - 1]])

DP = [SCC_H[i] for i in range(scc_num)]
while Q:
    u = Q.popleft()

    for v in SCC_E[u]:
        SCC_D[v] -= 1
        DP[v] = max(DP[v], SCC_H[v] + DP[u])
        if SCC_D[v] == 0:
            Q.append(v)

max_value = 0
for i in range(scc_num):
    if SCC_C[i] and SCC_V[i]:
        max_value = max(max_value, DP[i])

print(max_value)