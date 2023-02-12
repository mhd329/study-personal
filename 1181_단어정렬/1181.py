import sys
sys.stdin = open("1181.txt", 'r')
N = int(sys.stdin.readline())
st = set()
for _ in range(N):
    s = sys.stdin.readline().strip()
    st.add(s)
arr = list(st)
arr.sort()
arr.sort(key=lambda x:len(x))
for _ in arr:
    print(_)