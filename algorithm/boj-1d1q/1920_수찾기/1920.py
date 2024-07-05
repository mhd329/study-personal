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
# 정석 풀이 (함수를 쓰지 않음)
N = int(sys.stdin.readline())
n = [*map(int, sys.stdin.readline().split())]
n.sort()
M = int(sys.stdin.readline())
m = [*map(int, sys.stdin.readline().split())]
for i in m:
    flag = 0
    f = 0
    b = N - 1
    while f <= b:
        mid = (f + b) // 2
        if i < n[mid]:
            b = mid - 1
        elif i > n[mid]:
            f = mid + 1
        else:
            flag = 1
            break
    print(1 if flag else 0)