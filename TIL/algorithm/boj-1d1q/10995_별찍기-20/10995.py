n = int(input())

n_square = n ** 2
i = 1
line = 1

while i <= n_square:
    if line % 2 != 0:
        print('* ', end = '')
    else:
        print(' *', end = '')
        
    if i % n == 0:
        print("\n", end = '')
        line += 1
    
    i += 1