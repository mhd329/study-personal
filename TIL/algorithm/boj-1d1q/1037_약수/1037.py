N = int(input())
M = [*map(int, input().split())]
n = max(M)
m = min(M)
print(m * n)