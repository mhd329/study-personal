import sys
sys.stdin = open("17298.txt", 'r')

N = int(sys.stdin.readline())
A = [*map(int, sys.stdin.readline().split())]

while len(A) != 0:
    a = A.pop(0)
    for i in A:
        if i > a:
            print(i, end = ' ')
            break
    else:
        print(-1, end = ' ')