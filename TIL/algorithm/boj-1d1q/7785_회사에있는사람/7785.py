import sys
sys.stdin = open("7785.txt", 'r')

N = int(sys.stdin.readline())
working = set()

for i in range(N):
    log = sys.stdin.readline().split()
    if log[1] == 'enter':
        working.add(log[0])
    else:
        working.remove(log[0])
        
working = sorted([*working], reverse = True)
for j in working:
    print(j)