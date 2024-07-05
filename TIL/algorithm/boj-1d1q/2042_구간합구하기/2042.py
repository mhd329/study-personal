import sys
sys.stdin = open("2042.txt", 'r')

N, M, K = map(int, sys.stdin.readline().split())

def build(n):
    p = 0
    m = 0
    while n > m:
        m = 2 ** p
        p += 1
    tree = [0] * (m * 2)
    for i in range(N):
        tree[i + m] = int(sys.stdin.readline())
    for i in range(m - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[(2 * i) + 1]
    return tree, m
tree, leaf = build(N)

def change(tree, b, c, leaf):
    idx = leaf + b - 1
    delta = c - tree[idx] if tree[idx] < c else -(tree[idx] - c)
    while idx:
        tree[idx] += delta
        idx //= 2
    return tree

def interval_sum(tree, b, c, leaf):
    total = []
    start = leaf + b - 1
    end = leaf + c - 1
    while start < end:
        if start % 2:
            total.append(tree[start])
        start = (start + 1) // 2
        if not end % 2:
            total.append(tree[end])
        end = (end - 1) // 2
    if start == end:
        total.append(tree[start])
    return sum(total)

for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        tree = change(tree, b, c, leaf)
    else:
        answer = interval_sum(tree, b, c, leaf)
        print(answer)