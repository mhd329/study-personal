import sys ; sys.stdin = open("9020.txt", 'r') ; T = int(sys.stdin.readline())

p = [False, False] + ([True] * 9999)

for i in range(2, 10001):
    if p[i] == True:
        for j in range(2 * i, 10001, i):
            p[j] = False

def distinguish(n):
    if p[n // 2] == True:
        print(n // 2, n // 2)
    else:
        i = 1
        while True:
            if p[(n // 2) - i] and p[(n // 2) + i]:
                print((n // 2) - i, (n // 2) + i)
                break
            else:
                i += 1

for _ in range(T):
    N = int(sys.stdin.readline())
    distinguish(N)