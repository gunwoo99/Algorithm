import math

def FFT(f, w):
    n = len(f)
    if n == 1:
        return f
    
    even = [f[i] for i in range(0, n, 2)]
    odd = [f[i] for i in range(1, n, 2)]
    
    even = FFT(even, w ** 2)
    odd = FFT(odd, w ** 2)
    wp = complex(1)
    
    for i in range(n//2):
        f[i] = even[i] + wp * odd[i]
        f[i + n//2] = even[i] - wp * odd[i]
        wp *= w
    return f

# A, B => index = degree
def multiple(A, B):
    n = max(len(A), len(B))
    N = 2 ** math.ceil(math.log2(2 * n))
    A += [0] * (N - len(A))
    B += [0] * (N - len(B))
    rw = complex(math.cos(math.tau / N), math.sin(math.tau / N))

    # FFT된 A와 B의 inner product
    AA = FFT(A, rw)
    BB = FFT(B, rw)
    CC = [AA[i] * BB[i] for i in range(N)]

    # inner product된 값을 다시 inverse FFT (1 / rw)
    C = FFT(CC, complex(1) / rw)
    for i in range(N):
        C[i] /= complex(N)
        C[i] = round(C[i].real)
    return C