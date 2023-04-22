import sys
sys.stdin = open("1920.txt", 'r')
N = int(sys.stdin.readline())
A = [*map(int, sys.stdin.readline().split())]
A.sort()
M = int(sys.stdin.readline())
B = [*map(int, sys.stdin.readline().split())]
def find(start, mid, end, target):
    while start <= end:
        if target == A[mid]:
            return 1
        elif target < A[mid]:
            end = mid - 1
            mid = end // 2
        elif target > A[mid]:
            start = mid + 1
            mid = (start + end) // 2
    return 0
for i in B:
    print(find(0, N//2, N-1, i))