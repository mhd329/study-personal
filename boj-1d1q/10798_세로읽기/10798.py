import sys
sys.stdin = open("10798.txt", 'r')

S = []
length_ = []

for _ in range(5):
    S.append(sys.stdin.readline().rstrip())

for list_ in S:
    length_.append(len(list_))

column_len = max(length_)

for j in range(column_len):
    for i in range(len(S)):
        if j > len(S[i]) - 1:
            pass
        else:
            print(S[i][j], end ='')