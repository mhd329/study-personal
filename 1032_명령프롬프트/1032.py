import sys

sys.stdin = open("1032.txt", "r")
N = int(sys.stdin.readline())
for i in range(N):
    S = list(sys.stdin.readline().strip())
    if not i:
        ans = S
    else:
        for j in range(len(S)):
            if S[j] != ans[j]:
                ans[j] = "?"
ans = "".join(ans)
print(ans)
