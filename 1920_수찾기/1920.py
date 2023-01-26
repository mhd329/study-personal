# 정석 풀이는 아닌것같다.
import sys
sys.stdin = open("1920.txt", 'r')
'''
N = int(sys.stdin.readline())
n = [*map(int, sys.stdin.readline().split())]
a = {}
for i in n:
    if i not in a:
        a[i] = 1
print(a)
M = int(sys.stdin.readline())
m = [*map(int, sys.stdin.readline().split())]
for j in m:
    try:
        if a[j]:
            print(1)
        else:
            print(0)
    except:
        print(0)
'''
# 정석 풀이
N = int(sys.stdin.readline())
n = [*map(int, sys.stdin.readline().split())]
n.sort()
M = int(sys.stdin.readline())
m = [*map(int, sys.stdin.readline().split())]
for i in m:
    mid = N // 2
    start = n[0:mid]
    end = n[mid:]
    while 1:
        if mid == 1:
            print(1)
            break
        elif i >= start[0] and i <= start[mid - 1]:
            mid //= 2
            end = start[mid:]
            start = start[0:mid]
        elif i >= end[0] and i <= end[-1]:
            mid //= 2
            start = end[0:mid]
            end = end[mid:]
        else:
            print(0)
            break