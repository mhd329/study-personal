import sys
from pprint import pprint
sys.stdin = open("1018.txt", 'r')

N, M = map(int, sys.stdin.readline().split())

board = []
res = []

for y in range(N):
    board.append(sys.stdin.readline().rstrip())
    
for y in range(N):
    board.append(sys.stdin.readline().rstrip())

cnt = 0
for y in range(N - 7):
    for x in range(M - 7):
        for j in range(8):
            for i in range(8):
                if board[y][x] == 'W': # 탐색의 시작점이 W 이면
                    if j % 2: # 홀수행일때
                        if i % 2: # 홀수열일때
                            if board[y + j][x + i] != 'W':
                                cnt += 1
                        else: # 짝수열
                            if board[y + j][x + i] != 'B':
                                cnt += 1
                    else: # 짝수행일때
                        if i % 2: # 홀수열일때
                            if board[y + j][x + i] != 'B':
                                cnt += 1
                        else: # 짝수열
                            if board[y + j][x + i] != 'W':
                                cnt += 1
                else:
                    if j % 2: # 홀수행일때
                        if i % 2 == 1: # 홀수열
                            if board[y + j][x + i] != 'B':
                                cnt += 1
                        else: # 짝수열
                            if board[y + j][x + i] != 'W':
                                cnt += 1
                    else: # 짝수행일때
                        if i % 2: # 홀수열일때
                            if board[y + j][x + i] != 'W':
                                cnt += 1
                        else: # 짝수열
                            if board[y + j][x + i] != 'B':
                                cnt += 1
        res.append(cnt)
        cnt = 0

for y in range(N - 7):
    for x in range(M - 7):
        for j in range(8):
            for i in range(8):
                if board[y][x] != 'W': # 탐색의 시작점이 !W 이면
                    if j % 2: # 홀수행일때
                        if i % 2: # 홀수열일때
                            if board[y + j][x + i] != 'W':
                                cnt += 1
                        else: # 짝수열
                            if board[y + j][x + i] != 'B':
                                cnt += 1
                    else: # 짝수행일때
                        if i % 2: # 홀수열일때
                            if board[y + j][x + i] != 'B':
                                cnt += 1
                        else: # 짝수열
                            if board[y + j][x + i] != 'W':
                                cnt += 1
                                
                elif board[y][x] != 'B': # 시작점이 !B 이면
                    if j % 2: # 홀수행일때
                        if i % 2 == 1: # 홀수열
                            if board[y + j][x + i] != 'B':
                                cnt += 1
                        else: # 짝수열
                            if board[y + j][x + i] != 'W':
                                cnt += 1
                    else: # 짝수행일때
                        if i % 2: # 홀수열일때
                            if board[y + j][x + i] != 'W':
                                cnt += 1
                        else: # 짝수열
                            if board[y + j][x + i] != 'B':
                                cnt += 1
                                
        res.append(cnt)
        cnt = 0

print(min(res))

# 더 좋은 백준 풀이
# 훨씬 짧을 수 있을거라고 예상했고 실제로도 그랬다.

'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

board = []
count = []
for x in range(N):
    board.append(list(map(str,input().strip())))

for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] != 'W':
                        first_W += 1
                    if board[k][l] != 'B':
                        first_B += 1
                
                else:
                    if board[k][l] != 'B':
                        first_W += 1
                    if board[k][l] != 'W':
                        first_B += 1
        count.append(min(first_W,first_B))
        
print(min(count))
'''