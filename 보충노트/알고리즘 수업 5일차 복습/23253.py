import sys

sys.stdin = open("23253.txt", "r")

N, M = map(int, sys.stdin.readline().split())


def ox(M):
    for _ in range(M):
        temp = int(sys.stdin.readline())
        books = [*map(int, sys.stdin.readline().split())]
        while True:
            if len(books) == 1:
                break
            b = books.pop()
            if b > books[-1]:
                return print("No")
    else:
        return print("Yes")


ox(M)