r, g, b = input().split()

res = 0

r_list = list(range(int(r)))
g_list = list(range(int(g)))
b_list = list(range(int(b)))

for i in r_list:
    for j in g_list:
        for k in b_list:
            print(i,j,k)
            res += 1
print(res)

# 이 문제는 약간의 운이 좀 따른것같다.
# 감으로 했는데 맞았다.