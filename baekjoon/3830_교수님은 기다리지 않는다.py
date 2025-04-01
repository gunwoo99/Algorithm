
ANS = []
G = []
def union(a, b, v):
    pa, topa = find(a)
    pb, topb = find(b)
    if pa == pb:
        return

    if G[pa][2] < G[pb][2]:
        # pa가 pb에 합쳐짐
        G[pa][0] = pb
        G[pa][1] = v + topb - topa
        G[pb][2] = max(G[pb][2], G[pa][2] + 1)
    else:
        # pb가 pa에 합쳐짐
        G[pb][0] = pa
        G[pb][1] = topa - topb - v
        G[pa][2] = max(G[pa][2], G[pb][2] + 1)


def find(a):
    topo = 0
    while G[a][0] != a:
        topo += G[a][1]
        a = G[a][0]
        
    return a, topo

def difference(a, b):
    pa, topa = find(a)
    pb, topb = find(b)

    if pa != pb:
        return 'UNKNOWN'

    return topa - topb

while True:
    N, M = map(int, input().split())

    if N == M == 0:
        break
    
    G = [[i, 0, 1] for i in range(N + 1)]
    for _ in range(M):
        I = input().split()

        for i in range(1, len(I)):
            I[i] = int(I[i])
        if I[0] == '!':
            union(I[1], I[2], I[3])
        else:
            ANS.append(difference(I[1], I[2]))

for ans in ANS:
    print(ans)