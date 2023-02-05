N = input()
n = ''
for i in range(1, len(N)):
    if int(N[i]) > int(N[i - 1]):
        n = N[i] + n
    else:
        
print(n)