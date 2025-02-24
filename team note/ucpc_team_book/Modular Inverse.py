def inverse(n, p):
    value = 1
    inv = p - 2
    while inv:
        if inv & 1:
            value = (value * n) % p
        n = (n ** 2) % p
        inv >>= 1
    return value

print(2113 * inverse(6, 998244353) % 998244353)