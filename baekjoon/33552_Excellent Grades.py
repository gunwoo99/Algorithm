w = int(input())
n = int(input())

G = [list(map(float, input().split())) for _ in range(n)]
G = [(round(g[0] * 10), int(g[1])) for g in G]

WS = sum([g[0] * g[1] for g in G])
N = w + sum([g[1] for g in G])
V = 'V'
for i in range(101):
    if 80 * N <= WS + i*w:
        V = i
        break

for i in range(n):
    if G[i][0] < 58:
        print('IMPOSSIBLE')
        exit(0)
print(round(V/10,1) if V != 'V' else 'IMPOSSIBLE')