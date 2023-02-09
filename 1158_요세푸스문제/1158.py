'''
N, K = map(int, input().split())
seq = [i for i in range(1, N + 1)]
i = K - 1
ans = []
while seq:
    while i >= len(seq):
        if i >= len(seq):
            i -= len(seq)
    ans.append(seq.pop(i))
    i = i + K - 1
print("<", end='')
for j in range(len(ans)):
    if j + 1 == len(ans):
        print(ans[j], end='')
    else:
        print(ans[j], end=', ')
else:
    print(">")
'''
# rotate 라는 것을 몰랐다.
# rotate 쓰면 더 쉽게 풀 수 있다.
# rotate 써서 풀기

from collections import deque
N, K = map(int, input().split())
dq = deque([str(_) for _ in range(1, N + 1)])
idx = K
ans = []
while dq:
    dq.rotate(-idx)
    ans.append(dq.pop())
print("<" + ', '.join(ans) + ">")

# 그 외 deque 안쓰고 엄청 짧은 풀이
'''
n, k = map(int, input().split())
l = [i for i in range(1, n+1)]
s = []
i = 0
for _ in range(n):
    i += k-1
    i %= len(l)
    s.append(str(l.pop(i)))

print("<"  + ', '.join(s) + ">")
'''