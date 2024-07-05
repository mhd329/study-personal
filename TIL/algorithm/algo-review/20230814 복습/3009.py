import sys

sys.stdin = open("3009.txt", "r")
x = {}
y = {}
for i in range(3):
    a, b = map(int, sys.stdin.readline().split())
    if a not in x:
        x[a] = 0
    x[a] += 1
    if b not in y:
        y[b] = 0
    y[b] += 1
for k, v in x.items():
    if v == 1:
        a = k
        break
for k, v in y.items():
    if v == 1:
        b = k
        break
print(a, b)

# 더 쉬운방법

# x_p = []
# y_p = []

# for _ in range(3):
#     x, y = map(int, input().split())
#     x_p.append(x)
#     y_p.append(y)

# for i in range(3):
#     if x_p.count(x_p[i]) == 1:
#         x4 = x_p[i]
#     if y_p.count(y_p[i]) == 1:
#         y4 = y_p[i]

# print(x4, y4)

# 아직 감을 다 회복 못했다.
