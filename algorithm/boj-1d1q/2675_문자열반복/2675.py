import sys
sys.stdin = open("2675.txt", 'r')

T = int(sys.stdin.readline())

for test_case in range(T):
    R, S = sys.stdin.readline().split()
    
    for s in S:
        for _ in range(int(R)):
            print(s, end = '')
    print()