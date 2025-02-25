A, B = map(int, input().split())

L, R = [], []
n = int(input())
for i in range(n):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

sorted_L = sorted(L)
sorted_R = sorted(R, reverse=True) + [float('inf')]
sorted_index_L = sorted(range(n), key=lambda x: L[x])
sorted_index_R = sorted(range(n), key=lambda x: R[x], reverse=True)

D = A - B
min_value = float('inf')
min_i, min_j = -1, -1

j = 0
for i in range(n):
    while j < n and sorted_L[i] + sorted_R[j] > D:
        if sorted_index_L[i] == sorted_index_R[j]:
            cand_j = j - 1
        else:
            cand_j = j

        if min_value > sorted_L[i] + sorted_R[cand_j]:
            min_value = sorted_L[i] + sorted_R[cand_j]
            min_i, min_j = sorted_index_L[i], sorted_index_R[cand_j]

        j += 1

for i in range(n):    
    if D < sorted_L[i] < min_value:
        min_value = sorted_L[i]
        min_i = sorted_index_L[i]
        min_j = -2
    if D < sorted_R[i] < min_value:
        min_value = sorted_R[i]
        min_i = -2
        min_j = sorted_index_R[i]

if D < 0:
    print('-1 -1')
elif min_value == float('inf'):
    print('No')
else:
    print(min_i + 1, min_j + 1)

