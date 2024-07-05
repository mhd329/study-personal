import sys
sys.stdin = open("10815.txt", 'r')
N = int(sys.stdin.readline())
n = [*map(int, sys.stdin.readline().split())]
M = int(sys.stdin.readline())
m = [*map(int, sys.stdin.readline().split())]
n.sort()
def find(start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == n[mid]:
            return 1
        elif target < n[mid]:
            end = mid - 1
        elif target > n[mid]:
            start = mid + 1
    else:
        return 0
for target in m:
    print(find(0, N - 1), end=' ')