import sys
sys.stdin = open("1652_누울자리를찾아라.txt", 'r')

room = []
r_bed = 0
c_bed = 0

N = int(sys.stdin.readline())

for _ in range(N):
    room.append(sys.stdin.readline().rstrip())

for r in range(N):
    space = 0
    for c in range(N):
        if room[r][c] == '.':
            space += 1
        else:
            if space >= 2:
                r_bed += 1
                space = 0
            else:
                space = 0
    if space >= 2:
        r_bed += 1
        
for r in range(N):
    space = 0
    for c in range(N):
        if room[c][r] == '.':
            space += 1
        else:
            if space >= 2:
                c_bed += 1
                space = 0
            else:
                space = 0
    if space >= 2:
        c_bed += 1

print(r_bed, c_bed)