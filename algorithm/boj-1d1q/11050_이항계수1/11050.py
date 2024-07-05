N, K = map(int, input().split())

def f(n):
    if n:
        if n == 1:
            return n
        return n * f(n - 1)
    return 1

print(f(N) // (f(K) * f(N - K)))