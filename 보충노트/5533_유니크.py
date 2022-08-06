import sys
sys.stdin = open("5533_유니크.txt", 'r')

N = int(sys.stdin.readline())

ref = []
sco = []
total = []
    
for _ in range(N):
    ref.append(0)
    sco.append([*map(int, sys.stdin.readline().split())])
    total.append(0)

for c in range(3):
    for r in range(N):
        ref[r] = sco[r][c]
    
    for i in range(len(ref)):
        if ref.count(ref[i]) == 1:
            total[i] += ref[i]

for i in range(N):
    print(total[i])