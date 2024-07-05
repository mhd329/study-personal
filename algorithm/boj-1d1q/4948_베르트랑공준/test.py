import sys ; sys.stdin = open("4948.txt", 'r')

while 1:
    n = int(sys.stdin.readline())
    p = [False, False] + ([True] * ((2 * n) - 1))
    cnt = 0
    if n:
        for i in range(2, (2 * n) + 1):
            if p[i] == True:
                for j in range(2 * i, (2 * n) + 1, i):
                    p[j] = False
        for k in range(n + 1, (2 * n) + 1):
            if p[k] == True:
                cnt += 1
        print(cnt)
    else:
        break