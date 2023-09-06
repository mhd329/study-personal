import sys

sys.stdin = open("9020.txt", "r")
T = int(sys.stdin.readline())
sieve = [0] * 10001
for i in range(2, 10001):
    if not sieve[i]:
        for j in range(i * 2, 10001, i):
            sieve[j] = 1
for _ in range(T):
    n = int(sys.stdin.readline())
    a = b = n // 2
    while sieve[a] or sieve[b]:
        a -= 1
        b += 1
    print(a, b)
