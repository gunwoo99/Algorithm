n, m = map(int, input().split())

B = [[0 for _ in range(n)] for _ in range(n)]
C = {}
for i in range(n):
    I = list(input().split())
    for j in range(n):
        if i == j == n//2:
            continue
        C[I[j]] = (i, j)

RS = [0 for _ in range(n)]
CS = [0 for _ in range(n)]
RS[n//2], CS[n//2] = 1, 1
LD, RD = 1, 1
continueing = False
ans = ":-("
for i in range(m):
    I = input()
    if I not in C or continueing:
        continue
    
    L = C[I]
    if L[0] == L[1]:
        LD += 1
    if L[0] == n - 1 - L[1]:
        RD += 1
    RS[L[0]] += 1
    CS[L[1]] += 1

    if n in [LD, RD, RS[L[0]], CS[L[1]]]:
        continueing = True
        ans = i + 1

print(ans if n != 1 else 0)