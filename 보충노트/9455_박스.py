import sys
sys.stdin = open("9455_박스.txt", 'r')

T = int(sys.stdin.readline())

for test_case in range(T):
    n, m = map(int, sys.stdin.readline().split())
    cell = []
    cnt = 0
    
    for _ in range(n):
        cell.append([*map(int, sys.stdin.readline().split())])
    
    for j in range(m):
        for i in range(n - 1, -1, -1):
            if cell[i][j] == 1:
                while i + 1 != n and cell[i + 1][j] == 0:
                    cell[i][j], cell[i + 1][j] = cell[i + 1][j], cell[i][j]
                    i += 1
                    cnt += 1
                
    print(cnt)