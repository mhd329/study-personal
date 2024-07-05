import sys
sys.stdin = open("10815.txt", 'r')
N = int(sys.stdin.readline())
n = [*map(int, sys.stdin.readline().split())]
M = int(sys.stdin.readline())
m = [*map(int, sys.stdin.readline().split())]
n.sort()
for i in m:
    start = 0
    end = N - 1
    mid = (start + end) // 2
    while start <= end:
        if i == n[mid]:
            print(1)
            break
        if i < n[mid]:
            end = mid - 1
        if i > n[mid]:
            start = mid + 1
        mid = (start + end) // 2
    else:
        print(0)

# 이렇게도 정답은 나온다.
'''
n = int(input())
n1 = set(map(int,input().split()))
m = int(input())
m1 = list(map(int,input().split()))
k = []
for i in m1:
    if i in n1:
        k.append(1)
    else:
        k.append(0)
print(*k)
'''