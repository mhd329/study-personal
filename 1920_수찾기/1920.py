# 정석 풀이는 아닌것같다.
import sys
sys.stdin = open("1920.txt", 'r')
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