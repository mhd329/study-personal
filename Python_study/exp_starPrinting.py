n = 10
i = 0
j = 1
while i <= n:
    print(' ' * (10 - i), end = '')
    print('*' * i + '*' * (i - 1))
    i += 1
while j < n:
    print(' ' * j, end = '')
    print('*' * (10 - j) + '*' * (9 - j))
    j += 1
