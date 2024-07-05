def p(n, s, e):
    if s > e:
        return True
    if n[s] == n[e]:
        return p(n, s + 1, e - 1)
    else:
        return False
while 1:
    n = input()
    if not int(n):
        break
    print("yes" if p(n, 0, len(n) - 1) else "no")
