'''
N, M = map(int, input().split())
arr = []
cnt = 0
for i in range(2, M + 1):
    if i ** 2 > M:
        break
    arr.append(i ** 2)
for j in range(N, M + 1):
    for k in arr:
        if j >= k and not (j % k):
            break
    else:
        cnt += 1
print(cnt)
'''
'''
N, M = map(int, input().split())
p = [0, 1] + [_ for _ in range(2, M + 1)]
cnt = M
for i in range(2, M + 1):
    for j in range(i * i, M + 1, i * i):
        if p[j]:
            p[j] = 0
            cnt -= 1
print(cnt)
'''
N, M = map(int, input().split())
p = [0 for _ in range(N, M + 1)]
cnt = M
for i in range(N, M + 1):
    for j in range(2, (i**0.5) + 1):
        if p[j]:
            p[j] = False
            cnt -= 1
print(cnt)
# 뭐가 문제인거지