N = int(input())
P = [*map(int, input().split())]
P.sort()
t = 0
ans = 0
for i in range(N):
    t += P[i]
    ans += t
print(ans)
