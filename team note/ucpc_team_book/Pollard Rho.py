import math, random
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
    for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]:
        if n == i:
            return True
        
        if miller_rabin(n, i):
            return False
    return True

def func(c, x, n):
    return (c + ((x ** 2) % n)) % n

def rho(n):
    if n == 1:
        return
    
    if n % 2 == 0:
        factor.append(2)
        rho(n // 2)
        return
    
    if prime_test(n):
        factor.append(n)
        return
    
    a, b, c = 0, 0, 0
    g = n
    
    while 1:
        if g == n:
            b = random.randint(2, n - 1)
            a = b
            c = random.randint(1, 20)
        a = func(c, a, n)
        b = func(c, func(c, b, n), n)
        g = math.gcd(abs(a - b), n)
        if g != 1:
            break
    rho(g)
    rho(n // g)

factor = []