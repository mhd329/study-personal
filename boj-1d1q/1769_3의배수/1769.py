X = input()
res = 0

def y(x, cnt):
    if len(x) == 1:
        print(cnt)
        return print("YES" if not int(x) % 3 else "NO")
    
    int_x = 0
    int_x = sum(map(int, x))
    
    return y(str(int_x), cnt + 1)

y(X, res)

# 처음에 X 를 정수화시켜서 받아왔는데 그렇게 하니까 시간 초과가 났다.
# 변환 과정에서 시간이 많이 걸리나보다.