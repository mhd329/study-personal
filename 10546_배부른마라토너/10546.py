import sys
sys.stdin = open("10546.txt", 'r')

p = set()

N = int(sys.stdin.readline())

for _ in range(N + (N - 1)):
    w = sys.stdin.readline().rstrip()
    if w in p:
        p.remove(w)
    else:
        p.add(w)

print(*p)