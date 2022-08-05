import sys
sys.stdin = open("1316.txt", 'r')

N = int(sys.stdin.readline())

for _ in range(N):
    chk = []
    group_word = sys.stdin.readline().rstrip()
    
    for char in group_word:
        if char not in chk:
            chk.append(char)
        else:
            chk = []
            break
        ########################