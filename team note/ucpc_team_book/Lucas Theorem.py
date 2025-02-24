import sys, math

n, k, M = map(int, sys.stdin.readline().split())

def lucas(n, k, m):
    ans = 1
    while k != 0:
        ans = (ans * math.comb(n % m, k % m)) % m
        n //= m
        k //= m
    return ans