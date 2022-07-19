import sys
sys.stdin = open("input.txt", 'r')

t = int(input())

for i in range(1, t + 1):
    n = list(map(int, input().split()))
    res = 0
    for j in n:
        res += j
    avg = res / len(n)
    print(f"#{i} {avg:.0f}")