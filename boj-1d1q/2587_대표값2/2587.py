import sys
import statistics
sys.stdin = open("2587.txt", 'r')
n = []
for _ in range(5):
    n.append(int(sys.stdin.readline()))
n.sort()

print(statistics.mean(n))
print(n[2])