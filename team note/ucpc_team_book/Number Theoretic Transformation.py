import math
w = 3
mod = 2281701377

def power(a, b):
    ret = 1
    while b:
        if b & 1: 
            ret = (ret * a) % mod
        a = (a * a) % mod
        b >>= 1
    return ret

def NTT(A, inv=False):
    n = len(A)    
    
    rev = [0] * n
    for i in range(n):
        rev[i] = rev[i >> 1] >> 1
        if i & 1:
            rev[i] |= n >> 1
        if i < rev[i]:
            A[i], A[rev[i]] = A[rev[i]], A[i]
    
    x = power(w, (mod - 1) // n)
    if inv: 
        x = power(x, mod - 2)
    
    root = [1]
    for i in range(1, n):
        root.append((root[i-1] * x) % mod)
    
    i = 2
    while i <= n:
        step = n // i
        for j in range(0, n, i):
            for k in range(i>>1):
                u = A[j|k]
                v = (A[j|k|i >> 1] * root[step*k]) % mod
                A[j|k] = (u + v) % mod
                A[j|k|i >> 1] = (u - v) % mod
                if A[j|k|i >> 1] < 0: A[j|k|i >> 1] += mod
        i <<= 1
    
    if inv:
        t = power(n, mod - 2)
        for i in range(n):
            A[i] = (A[i] * t) % mod
    return A

def multiple(a, b):
    n = max(len(a), len(b))
    n = 2 * 2 ** math.ceil(math.log2(n))
    a += [0] * (n - len(a))
    b += [0] * (n - len(b))
    A = NTT(a, inv=False)
    B = NTT(b, inv=False)
    return NTT([(A[i]*B[i]) % mod for i in range(n)], inv=True)

mod1 = 2281701377
mod2 = 998244353
mod3 = 2130706433

import copy
input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = copy.copy(a)
d = copy.copy(b)
C = multiple(c, d, mod1)
c = copy.copy(a)
d = copy.copy(b)
D = multiple(c, d, mod2)
E = multiple(a, b, mod3)

answer = 0
for i in range(len(C)):
    ans = 0
    ans += C[i] * mod2 * mod3 * power(mod2*mod3, mod1-2, mod1)
    ans += D[i] * mod1 * mod3 * power(mod1*mod3, mod2-2, mod2)
    ans += E[i] * mod1 * mod2 * power(mod1*mod2, mod3-2, mod3)
    ans %= mod1 * mod2 * mod3
    answer ^= ans