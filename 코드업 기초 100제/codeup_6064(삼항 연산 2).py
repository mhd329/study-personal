a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

# a if a < b else b /// a 가 b 보다 작을 때 a 를 출력

# 조건 검사 후

# (a if a < b else b) < c /// (a 가 b 보다 작을 때 a) (를 c 와 비교해서 작을 때) a 를 출력

# (a if a < b else b) if (a if a < b else b) < c else c ///
# (a 가 b 보다 작을 때 a 를) ~할 것이다. 만약 (a 가 b 보다 작을 때 a) (를 c 와 비교해서 a 가 작다면). 그게 다 아니면 c
# 뭔가 하려는 대상 if 비교 조건 else 아닐경우

print((a if a < b else b) if (a if a < b else b) < c else c)