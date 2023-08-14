N = int(input())
p = 4
r = 2
for _ in range(N):
    r = 2 * r - 1
    p = r**2
print(p)

# 더 나은 풀이

# n = int(input())
# side = (1 + 2**n)
# print(side**2)
