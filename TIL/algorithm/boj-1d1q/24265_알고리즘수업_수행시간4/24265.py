# n = int(input())
# def f(n):
#     if n == 1:
#         return 1
#     n += f(n - 1)
#     return n
# print(f(n - 1))
# print(2)

n = int(input())
n -= 1
res = 0
while n > 0:
    res += n
    n -= 1
print(res)
print(2)
