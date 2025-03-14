n = int(input())
A = [list(input().split()) for _ in range(n)]

ans = []
for a in A:
    a[0], a[1] = str(min(int(a[0]), int(a[1]))), str(max(int(a[0]), int(a[1])))
    int_mul = int(a[0]) * int(a[1])
    str_mul = ''
    for i in range(len(a[0])):
        str_mul = str(int(a[0][len(a[0])-1-i]) * int(a[1][len(a[1])-1-i])) + str_mul
    
    str_mul = a[1][:len(a[1]) - len(a[0])] + str_mul

    if int_mul == int(str_mul):
        print(int_mul, str_mul)
        ans.append(1)
    else:
        ans.append(0)

print(*ans, sep='\n')