import sys
sys.stdin = open("2217.txt", "r")
N = int(sys.stdin.readline())
w = []
m = []
for _ in range(N):
    w.append(int(sys.stdin.readline()))
w.sort(reverse=True)
for i in range(len(w)):
    m.append(w[i] * (i + 1))
print(max(m))