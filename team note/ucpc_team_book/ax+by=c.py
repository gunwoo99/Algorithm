
def modsol(a, b, n):
    N = n
    A = a
    numn = [1, 0]
    numa = [0, 1]
    while n % a != 0:
        numn, numa = [(x - y * (n // a)) for x, y in zip(numn, numa)]
        n, a = a, n % a
    
    gcd = a
    if b % gcd != 0:
        return False
    
    mult = b // gcd
    numa[1] *= mult
    numa[1] %= N // gcd
    return numa[1]

# ax = 1 (mod n)
# ny + ax = 1  => 4, -43
# (a %= n) ax = gcd(n, a) (mod n) 의 해는
# gcd 함수의 B[1]
# ax = k (mod n) 의 해는 (n % gcd(n, a) == 0)
# gcd 함수의 B[1] * (n // gcd(n, a)) % (n // gcd(n, a))