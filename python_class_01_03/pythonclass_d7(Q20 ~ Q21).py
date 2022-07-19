# 20
# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요.
'''
n = int(input())

n = str(n)
res = 0

for i in n:
    i = int(i)
    res += i
    
print(res)
'''
# 21
# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지
'''
n = int(input()) # 3951
length = 0
res = 0
cnt = n

while cnt > 0:
    cnt //= 10
    length += 1

for i in range(length, 0, -1):
    reverse_n = n % 10
    res += reverse_n * (10 ** (i-1))
    n //= 10
'''