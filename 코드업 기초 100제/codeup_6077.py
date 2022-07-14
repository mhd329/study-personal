n = int(input())

# 1~100
res = 0
for i in range(n):
    if (i+1) % 2 == 0:
        res += (i+1)
        
print(res)