import sys
sys.stdin = open("2042.txt", 'r')
N, M, K = map(int, sys.stdin.readline().split())
arr = []
tree = [0] * (N * 4)
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
def segment(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    else:
        mid = (start + end) // 2
        tree[idx] = segment(start, mid, idx * 2) + segment(mid + 1, end, (idx * 2) + 1)
        return tree[idx]
segment(0, N - 1, 1)
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
print(tree)