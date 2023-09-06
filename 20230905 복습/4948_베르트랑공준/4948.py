import sys

sys.stdin = open("4948.txt", "r")
sieve = [0] * 246913
for i in range(2, 246913):
    if not sieve[i]:
        for j in range(i * 2, 246913, i):
            sieve[j] = 1

while 1:
    cnt = 0
    n = int(sys.stdin.readline())
    if not n:
        break
    for i in range(n + 1, 2 * n + 1):
        if not sieve[i]:
            cnt += 1
    print(cnt)
