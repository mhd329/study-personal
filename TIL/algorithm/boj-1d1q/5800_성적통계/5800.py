import sys
sys.stdin = open("5800.txt", 'r')

K = int(sys.stdin.readline())

for test_case in range(1, K + 1):
    N = [*map(int, sys.stdin.readline().split())]
    m = N.pop(0)
    N.sort(reverse = True)
    
    gap = 0
    for i in range(1, m):
        if abs(N[i] - N[i - 1]) > gap:
            gap = abs(N[i] - N[i - 1])
    
    print(f"Class {test_case}")
    print(f"Max {max(N)}, Min {min(N)}, Largest gap {gap}")