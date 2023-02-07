import sys
sys.stdin = open("2072.txt", 'r')
board = [[0] * 20 for _ in range(20)]
N = int(sys.stdin.readline())
dx = [0, -1, -1, -1, 0, 1, 1, 1, 0]
dy = [0, -1, 0, 1, 1, 1, 0, -1, -1]
winner = 0
for turn in range(1, N + 1):
    x, y = map(int, sys.stdin.readline().split())
    tempx = x
    tempy = y
    board[x][y] = 1 if turn % 2 else 2
    for i in range(1, 9):
        j = 1
        while 0 < x + dx[i] < 20 and 0 < y + dy[i] < 20:
            if board[x][y] == board[x + dx[i]][y + dy[i]]:
                x = x + dx[i]
                y = y + dy[i]
                j += 1
            else:
                break
        x = tempx
        y = tempy
        if j < 5:
            if i < 5:
                while 0 < x + dx[i + 4] < 20 and 0 < y + dy[i + 4] < 20:
                    if board[x][y] == board[x + dx[i + 4]][y + dy[i + 4]]:
                        x = x + dx[i + 4]
                        y = y + dy[i + 4]
                        j += 1
                    else:
                        break
            else:
                while 0 < x + dx[i - 4] < 20 and 0 < y + dy[i - 4] < 20:
                    if board[x][y] == board[x + dx[i - 4]][y + dy[i - 4]]:
                        x = x + dx[i - 4]
                        y = y + dy[i - 4]
                        j += 1
                    else:
                        break
            x = tempx
            y = tempy
            if j == 5:
                winner = turn
                break
        elif j == 5:
            if i < 5:
                if 0 < x + dx[i + 4] < 20 and 0 < y + dy[i + 4] < 20:
                    if board[x][y] != board[x + dx[i + 4]][y + dy[i + 4]]:
                        winner = turn
                        break
            else:
                if 0 < x + dx[i - 4] < 20 and 0 < y + dy[i - 4] < 20:
                    if board[x][y] != board[x + dx[i - 4]][y + dy[i - 4]]:
                        winner = turn
                        break
        else:
            break
    if j == 5:
        if winner:
            break
if winner:
    print(winner)
else:
    print(-1)

# 구현 문제는 조건 맞추기랑 범위 맞추기가 참 까다로운것같다.