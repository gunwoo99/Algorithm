import sys
sys.setrecursionlimit(100000)
n, m, A, B = map(int, input().split())
Ve = [list(map(int, input().split())) for _ in range(n)]
E = [[] for _ in range(n)]
for _ in range(m):
    c, d, k = map(int, input().split())
    c -= 1
    d -= 1
    E[c].append(d)
    if k == 2:
        E[d].append(c)

LM = [i for i in range(n) if Ve[i][0] == 0]
RM = [i for i in range(n) if Ve[i][0] == A]

def scc(edge, n):
    from collections import deque
    grouped = [False for _ in range(n)]
    level_of = [False for _ in range(n)]
    stack = deque([])
    level = 0
    groups = []

    def dfs(u):
        nonlocal level
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

groups = scc(E, n)
V_SCC = [None for _ in range(n)]
for i in range(len(groups)):
    for j in range(len(groups[i])):
        V_SCC[groups[i][j]] = i
groups_edge = {}
for i in range(len(groups)):
    groups_edge[i] = set()

for u in range(n):
    for v in E[u]:
        if V_SCC[u] != V_SCC[v]:
            groups_edge[V_SCC[u]].add(V_SCC[v])

SCC_E = [[] for _ in range(len(groups))]
for i in range(len(groups_edge)):
    SCC_E[i] = list(groups_edge[i])

V = [[False, float("inf"), -float("inf")] for _ in range(len(groups))]
for rm in RM:
    V[V_SCC[rm]][1] = min(V[V_SCC[rm]][1], Ve[rm][1])
    V[V_SCC[rm]][2] = max(V[V_SCC[rm]][2], Ve[rm][1])
SLM = sorted(LM, key=lambda x:Ve[x][1], reverse=True)
SRM = sorted(RM, key=lambda x:Ve[x][1], reverse=True)

SRMI = {}
for i in range(len(SRM)):
    SRMI[Ve[SRM[i]][1]] = len(SRM) - i
def dfs(u):
    if V[u][0]:
        return V[u][1], V[u][2]
    
    V[u][0] = True
    for v in SCC_E[u]:
        low, top = dfs(v)
        V[u][1] = min(V[u][1], low)
        V[u][2] = max(V[u][2], top)
    return V[u][1], V[u][2]

ans = []
for i in range(len(SLM)):
    low, top = dfs(V_SCC[SLM[i]])
    if low > top:
        ans.append(0)
    else:
        ans.append(SRMI[top] - SRMI[low] + 1)
print(*ans, sep="\n")
