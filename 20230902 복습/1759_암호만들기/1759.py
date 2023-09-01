import sys
sys.stdin = open("1759.txt", "r")
n, m = map(int, sys.stdin.readline().split())
C = sys.stdin.readline().split()
C.sort()
res = ''
def ans(idx):
    global res
    if len(res) == n:
        cnt = 0
        for i in ('a', 'e', 'i', 'o', 'u'):
            if i in res:
                cnt += 1
        if 1 <= cnt and (n - cnt) >= 2:
            print(res)
        return
    for i in range(idx, m):
        res += C[i]
        ans(i + 1)
        res = res[:-1]
ans(0)