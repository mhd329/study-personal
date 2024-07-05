N = int(input())

fibonacci = [0, 1]

i = 0
while i <= (N - 1):
    n1 = fibonacci.pop() # 1
    n2 = fibonacci.pop() # 0
    m = n1 + n2
    fibonacci.append(n1)
    fibonacci.append(m)
    i += 1
    
print(fibonacci[-2])