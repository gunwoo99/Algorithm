# Fermat's little Theorem
# a ** (p-1) % p = 1 if p is prime
# Modular Inverse is a ** (p - 2) % p
# Divisor sum => PHI {(factor ** (facnum + 1) - 1) / (factor - 1)}
import sys, math
n, m = map(int, sys.stdin.readline().split())

factors = []
divisor_sum = 1
mod = 1_000_000_007  # modular must be prime

for factor in factors:
    fact = factor[0]
    fnum = factor[1] * m + 1
    numer = 1
    while fnum:
        if fnum & 1:
            numer = (numer * fact) % mod
        fact = (fact ** 2) % mod
        fnum >>= 1
    numer -= 1
    
    div = factor[0] - 1
    dnum = mod - 2 # Modular Inverse
    denom = 1
    while dnum:
        if dnum & 1:
            denom = (denom * div) % mod
        div = (div ** 2) % mod
        dnum >>= 1
    divisor_sum *= numer * denom
    divisor_sum %= mod