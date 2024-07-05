def solution(board):
    answer = -1
    cnt_o = 0
    cnt_x = 0
    winner = set()
    for x in range(3):
        for y in range(3):
            if board[x][y] == 'O':
                cnt_o += 1
            elif board[x][y] == 'X':
                cnt_x += 1
    if not (cnt_o + cnt_x):
        return 1
    elif cnt_o < cnt_x or cnt_o - cnt_x > 1:
        return 0
    # 이 아래는 최소한 두개의 개수가 같거나 O가 한 개 많음
    for x in range(3):
        for y in range(3):
            if board[x][y] != '.':
                mark = board[x][y]
                dx = [-1, -1, 0, 1, 1, 1, 0, -1]
                dy = [0, 1, 1, 1, 0, -1, -1, -1]
                for i in range(8):
                    end = 1
                    nx = x + dx[i]
                    ny = y + dy[i]
                    while -1 < nx < 3 and -1 < ny < 3:
                        if board[nx][ny] == mark:
                            end += 1
                            if end == 3:
                                winner.add(mark)
                            nx += dx[i]
                            ny += dy[i]
                        else:
                            break
    if 'O' in winner and 'X' in winner:
        return 0
    elif 'O' in winner:
        if cnt_o - cnt_x != 1:
            return 0
        else:
            return 1
    elif 'X' in winner:
        if cnt_o - cnt_x != 0:
            return 0
        else:
            return 1
    else:
        return 1

print(solution(["OXO", "XOX", "OXO"]))