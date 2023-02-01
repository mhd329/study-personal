import sys
sys.stdin = open("1806.txt", 'r')
N, S = map(int, sys.stdin.readline().split())
n = [*map(int, sys.stdin.readline().split())]
def interval(N:int, S:int, n:list) -> int:
    m = N # 최소 길이 초기화
    l = 0 # 지금 길이
    end = 0
    total = 0
    for start in range(N):
        while total < S and end < N:
            total += n[end]
            end += 1
            l += 1
        if total == S:
            if l < m:
                m = l
            l = 2
            if m == 1:
                return print(m)
        total -= n[start]
        l -= 1
    else:
        if total == S:
            return print(m)
        else:
            return print(0)
interval(N, S, n)