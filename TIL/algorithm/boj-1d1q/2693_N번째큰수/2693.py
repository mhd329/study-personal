import sys
sys.stdin = open("2693.txt", 'r')

T = int(sys.stdin.readline())

for test_case in range(T):
    A = [*map(int, sys.stdin.readline().split())]
    
    A.sort(reverse = True)
    print(A[2])