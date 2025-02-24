
def power(x, y, p):
    res = 1
    piv = x % p
    while y:
        if y & 1:
            res *= piv
            res %= p
        piv *= piv
        piv %= p
        y >>= 1
    return res

# True => 합성수이다
def miller_rabin(n, p):
    if n % p == 0:
        return True
    
    d = n - 1
    while 1:
        cur = power(p, d, n)
        if cur == n - 1:
            return False
        elif d & 1:
            return not (cur == 1 or cur == n - 1)
        d >>= 1

# 소수면 True
def prime_test(n):
    #for i in [2, 7, 61]:
    for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]:
        if n == i:
            return True
        
        if miller_rabin(n, i):
            return False
    return True

r = 10000
primesA = []
primesB = []
isprime = [True for _ in range(r + 1)]
for i in range(2, r + 1):
    if prime_test(i):
        primesA.append(i)
    
    if not isprime[i]:
        continue
    
    primesB.append(i)
    j = 2 * i
    while j <= r:
        isprime[j] = False
        j += i

print(*primesA[:20])
print(*primesB[:20])
