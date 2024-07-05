import sys
sys.stdin = open("17249.txt", 'r')

TaeBo = sys.stdin.readline().rstrip()
l_cnt = 0
r_cnt = 0
for s in TaeBo[:TaeBo.index('(')]:
    if s == '@':
        l_cnt += 1

for s in TaeBo[TaeBo.index(')'):]:
    if s == '@':
        r_cnt += 1

print(l_cnt, r_cnt)

# 감탄스러운 코드
# a,b = input().split("(^0^)")
# print(a.count('@'),b.count("@"))

# 숏코딩 1등
# print(*[a.count('@')for a in input().split('0')])