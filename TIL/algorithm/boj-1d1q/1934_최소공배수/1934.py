import sys
sys.stdin = open("1934.txt", 'r')
T = int(sys.stdin.readline())

def gcd(a, b):
    res = a % b
    if res:
        return gcd(b, res)
    return b

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    N = gcd(max(A, B), min(A, B))
    print(A * B // N)