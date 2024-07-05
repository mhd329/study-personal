import sys
sys.stdin = open("1874.txt", 'r')
N = int(sys.stdin.readline())
tmp = []
res = []
ans = []
m = 1
flag = True
for _ in range(N):
    n = int(sys.stdin.readline())
    while m <= n and flag:
        tmp.append(m)
        ans.append("+")
        m += 1
    else:
        if tmp[-1] == n:
            res.append(tmp.pop())
            ans.append("-")
        else:
            flag = False
if flag:
    for s in ans:
        print(s)
else:
    print("NO")