
N, M = map(int, input().split())
B = [list(map(int, list(input()))) for _ in range(N)]
D = [[[float('inf'), float('inf')] for _ in range(M)] for _ in range(N)]

from collections import deque
Q = deque([(1, 0, 0, 0)])

directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
while Q:
    d, r, c, w = Q.pop()
    
    if D[r][c][w] < d:
        continue
    D[r][c][w] = d

    for direction in directions:
        x = r + direction[0]
        y = c + direction[1]

        if 0 <= x < N and 0 <= y < M:
            z = w + B[x][y]
            if z < 2 and d + 1 < D[x][y][z]:
                D[x][y][z] = d + 1
                Q.append((d + 1, x, y, z))

print(min(D[-1][-1]) if min(D[-1][-1]) != float('inf') else -1)
