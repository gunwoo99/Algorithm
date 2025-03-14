n = int(input())
B = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
K = [0] + sorted(list(map(int, input().split())), reverse=True)

AK = [0 for _ in range(m+1)]
for i in range(1, m+1):
    AK[i] = K[i] + AK[i-1]

AB = [[0 for _ in range(n+1)] for _ in range(n+1)]
AZ = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        AB[i][j] = AB[i-1][j] + AB[i][j-1] - AB[i-1][j-1] + B[i][j]
        AZ[i][j] = AZ[i-1][j] + AZ[i][j-1] - AZ[i-1][j-1] + (B[i][j] == 0)

maxv = -1
for i in range(n):
    for j in range(n):
        for k in range(n - max(i, j)):
            curv = AB[i+k][j+k] - AB[i-1][j+k] - AB[i+k][j-1] + AB[i-1][j-1]
            curz = AZ[i+k][j+k] - AZ[i-1][j+k] - AZ[i+k][j-1] + AZ[i-1][j-1]

            if curz > m:
                break

            curv += AK[curz]
            maxv = max(maxv, curv)

print(maxv)