from collections import Counter

A = []
for _ in range(int(input())):
    V = list(map(int, list(input())))
    
    S = sum(V)
    N1 = Counter(V)[1]
    N5 = Counter(V)[5]

    if S % 3 == 0:
        A.append([0, 3])
    elif S % 3 == 1:
        if N1:
            A.append([V.index(1)+1, 3])
        else:
            A.append([0, 5])
    else:
        if N5:
            A.append([V.index(5)+1, 3])
        else:
            if N1 % 2 == 0:
                A.append([0, 11])
            else:
                A.append([1, 11])
for a in A:
    print(*a)
