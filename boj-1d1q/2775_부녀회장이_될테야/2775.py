import sys
sys.stdin = open("2775.txt", 'r')

T = int(sys.stdin.readline())

for test_case in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    
    apt = []
    
    for i in range(k + 1):
        apt.append([])
        for _ in range(n):
            apt[i].append(0)
    
    for j in range(1, n + 1):
            apt[0][j - 1] = j
    
    for y in range(1, k + 1):
        for x in range(n):
            apt[y][x] = (sum(apt[y - 1][:(x + 1)]))
    
    print(apt[k][n - 1])

# 백준 다른 답
'''
t = int(input())

for i in range(t):
    f = int(input())
    n = int(input())
    b = [x for x in range(1, n+1)]
    for j in range(f):
        for k in range(1, n):
            b[k] += b[k-1]
    print(b[-1])
'''
# 나처럼 모든 층수를 미리 만들어서 0층에 ... 1층에 ... 이런식으로 하지 않고
# 처음 1 2 3 을 가지는 0층 하나 가지고 각 원소에 이전 원소를 계속 더해주면서 자기 자리의 값을 갱신하여
# 마지막에는 다 더해진 제일 끝 원소만 출력