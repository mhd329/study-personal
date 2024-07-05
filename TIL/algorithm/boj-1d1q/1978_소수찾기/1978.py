import sys
sys.stdin = open("1978.txt", 'r')

N = int(sys.stdin.readline())
divisor = []
prime = 0

for _ in range(N):
    p = [*map(int, sys.stdin.readline().split())]
    
    for n in p:
        for i in range(1, n + 1):
            if not n % i:
                divisor.append(n)
    
        if len(divisor) == 2:
            prime += 1
        divisor = []
    
print(prime)