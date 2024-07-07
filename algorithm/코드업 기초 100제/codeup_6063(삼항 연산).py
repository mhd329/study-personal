# 조건을 만족하는 값 = (a if 조건 else b)

a, b = input().split()
a = int(a)
b = int(b)

print(a if a >= b else b)