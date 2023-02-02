import sys
sys.stdin = open("1806.txt", 'r')
N, S = map(int, sys.stdin.readline().split())
n = [0] + [*map(int, sys.stdin.readline().split())]
total = [0] * (N + 1)
for idx in range(1, N + 1):
    total[idx] = total[idx - 1] + n[idx]
def interval(N, S, n):
    flag = False
    j = 1
    m = N
    for i in range(N + 1):
        while j < N + 1 and total[j] - total[i] < S:
            j += 1
        if j < N + 1 and total[j] - total[i] >= S:
            flag = True
            if j - i < m:
                m = j - i
            if m == 1:
                return print(m)
    if flag:
        return print(m)
    else:
        return print(0)
interval(N, S, n)

# 문제를 잘 읽자!!!
# 합이 S 인 것이 아니라 합이 S 이상이 되는 모든 값...