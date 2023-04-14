import sys
sys.stdin = open("11005.txt", 'r')

N, B = map(int, sys.stdin.readline().split())

def ans(n, b):
    answer = ""
    while n > 0:
        n, x = divmod(n, b)
        if x > 10:
            x = str(chr(x + 55))
        else:
            x = str(x)
        answer += x
    return answer

print(ans(N, B))