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