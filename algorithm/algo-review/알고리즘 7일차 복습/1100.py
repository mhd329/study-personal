import sys
sys.stdin = open("1100.txt", 'r')

cnt = 0
for i in range(8):
    board = sys.stdin.readline().rstrip()
    cnt += board[i % 2 : : 2].count('F')

print(cnt)