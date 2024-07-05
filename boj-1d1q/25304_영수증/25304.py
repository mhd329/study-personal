import sys
sys.stdin = open("25304.txt", 'r')

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
total = 0

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    
    total += a * b

print("Yes") if total == X else print("No")