N, K = map(int, input().split())
def e(n, k):
    cnt = 0
    sieve = [0, 1]
    sieve += [_ for _ in range(2, n + 1)]
    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            if sieve[j]:
                temp = sieve[j]
                sieve[j] = 0
                cnt += 1
            if cnt == k:
                return temp
print(e(N, K))