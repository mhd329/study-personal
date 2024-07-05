A, B, C = map(int, input().split())


def moduler(a, b):
    if b == 1:
        return a % C
    r = moduler(a, b // 2)

    if b % 2:
        return r * r * a % C
    else:
        return r * r % C


print(moduler(A, B))
