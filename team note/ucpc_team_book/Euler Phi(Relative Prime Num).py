import math
# phi using primes => []
def phi(n, primes):
    RPsum = n
    for prime in primes:
        if n % prime != 0:
            continue
        
        while n % prime == 0:
            n //= prime
        RPsum //= prime
        RPsum *= prime - 1
        
        if n == 1:
            break
    
    if n != 1:
        RPsum *= n - 1
        RPsum //= n
    return RPsum

# phi using factorization
def phi_f(n, factor):
    factor = list(set(factor))
    return math.prod([fact - 1 for fact in factor])