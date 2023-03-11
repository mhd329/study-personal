import sys
sys.stdin = open("9506.txt", 'r')
def gen(n, arr):
    if sum(arr) == n:
        print(f"{n} =", " + ".join(map(str, arr)))
    else:
        print(f"{n} is NOT perfect.")

while 1:
    factors = []
    N = int(sys.stdin.readline())
    if N == -1:
        break
    for i in range(1, (N // 2) + 1):
        if not N % i:
            factors.append(i)
    gen(N, factors)