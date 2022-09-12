N = int(input())
seat = [0] * 101

reject = 0
for i in map(int, input().split()):
    if seat[i] == 0:
        seat[i] = 1
    else:
        reject += 1

print(reject)

'''
N = int(input())
seat = [0] * (N + 1)

reject = 0
for i in map(int, input().split()):
    if seat[i] == 0:
        seat[i] = 1
    else:
        reject += 1

print(reject)
'''
# 이렇게 하면 왜 런타임 에러가 나는걸까?