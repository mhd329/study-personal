import sys
sys.stdin = open("6588.txt", 'r')

p = [0, 0]
p += [1 for _ in range(999999)]

for i in range(2, len(p)):
    if p[i]:
        for j in range(i * 2, len(p), i):
            p[j] = 0

def searching(n):
    for i in range(3, (n // 2) + 1):
        j = n - i
        if p[i] and p[j] % 2:
            return print(f"{n} = {i} + {j}")

while 1:
    N = int(sys.stdin.readline())
    if not N:
        break
    searching(N)