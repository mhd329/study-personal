import sys
sys.stdin = open("1004.txt", 'r')

T = int(sys.stdin.readline())

for i in range(T):
    cnt = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    for j in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())
        R = r ** 2
        a = (x1 - cx) ** 2
        b = (y1 - cy) ** 2
        c = (x2 - cx) ** 2
        d = (y2 - cy) ** 2
        if (a + b < R and c + d < R) or (a + b > R and c + d > R):
            pass
        else:
            cnt += 1
    print(cnt)