import sys
sys.stdin = open("3003.txt", 'r')
pieces = [*map(int, input().split())]

need = [1, 1, 2, 2, 2, 8]

for i in range(6):
    need[i] -= pieces[i]
    
print(*need)