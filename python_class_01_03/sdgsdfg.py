a = 3951
print(a)

while a > 0:
    reverse_a = a % 10
    print(reverse_a)
    res = reverse_a * 10
    a //= 10
