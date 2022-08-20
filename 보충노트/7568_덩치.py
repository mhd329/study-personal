import sys
sys.stdin = open("7568_덩치.txt", 'r')

N = int(sys.stdin.readline())

body = []

for _ in range(N):
    body.append([*map(int, sys.stdin.readline().split()), 1])

for i in body:
    for j in body:
        if i[0] < j[0] and i[1] < j[1]:
            i[2] += 1
            
    print(i[2], end = ' ')