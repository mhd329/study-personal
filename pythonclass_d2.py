# 1번 문제
# 주어진 수 n이 3의 배수이면서 짝수인 경우 ‘참’을 거짓인 경우 ‘거짓'을 출력하시오.
'''
n = int(input())

if (n % 3 == 0) and (n % 2 == 0):
    print("참")
else:
    print("거짓")
'''
# 2번 문제
# 문자열 word의 길이를 출력하는 코드를 각각 작성하시오.

# len() 함수를 바로 쓰기보다는 반복문을 활용하세요.
'''
word_1 = input() # "Happy!"
alphabet_length_1 = 0
for alphabet in word_1:
    alphabet_length_1 += 1
    
print(alphabet_length_1)
'''
# 3번 문제
# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

# sum() 함수 사용 금지
'''
list_n = range(int(input()) + 1)

res_1 = 0

# 1)

i = 0
while i < len(list_n):
    res_1 += list_n[i]
    i += 1
    
print("while 문을 이용한 방법 :",res_1)

# 2)

res_2 = 0

for i in list_n:
    res_2 += i
    
print("for 문을 이용한 방법 :",res_2)
'''
# 4번 문제
# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
'''
n = int(input())

list_n = range(1 , n + 1)

# 1)

res_1 = 1

i = 0

while i < len(list_n):
    res_1 *= list_n[i]
    i += 1
    
print("while 문 사용 :",res_1)

# 2)

res_2 = 1

for i in list_n:
    res_2 *= i
    
print("for 문 사용 :",res_2)
'''
# 5번 문제
# 주어진 숫자의 평균을 구하는 코드를 작성하시오.

# sum(), len()  함수 사용 금지
'''
set_of_n = input().split() # 3 10 20

sum_of_n = 0
length_of_n = 0

for i in set_of_n:
    sum_of_n += int(i)
    length_of_n += 1

print(f"{sum_of_n/length_of_n:.2f}")
'''
# 6번 문제
# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.

# max() 함수 사용 금지
'''
set_of_n = input().split() # [-10, -100, -30]
for i in range(len(set_of_n)):
    set_of_n[i] = int(set_of_n[i])
    
# 1) sort 사용
set_of_n.sort(reverse = True)
print("sort 사용 :",set_of_n[0])

# 2) sort 미사용
res = set_of_n[i]
for i in range(len(set_of_n)): # [0, 20, 100, 50, -60, 50, 100]
    if set_of_n[i] >= res:
        res = set_of_n[i]
        
print("sort 미사용 :",res)
'''
# 7번 문제
# 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.

# min() 함수 사용 금지
'''
set_of_n = input().split()
for i in range(len(set_of_n)):
    set_of_n[i] = int(set_of_n[i])
    
# 1) sort 사용
set_of_n.sort()
print("sort 사용 :",set_of_n[0])

# 2) sort 미사용
res = set_of_n[i]
for i in range(len(set_of_n)): # [0, 20, 100, 50, -60, 50, 100]
    if set_of_n[i] <= res:
        res = set_of_n[i]
        
print("sort 미사용 :",res)
'''
# 8번 문제
# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.

# max() 함수 사용 금지
'''
set_of_n = set(input().split()) # 중복되는 값을 제거
list_of_n = list(set_of_n)
for i in range(len(list_of_n)):
    list_of_n[i] = int(list_of_n[i]) # 리스트 원소 정수화

# 1) sort 사용
list_of_n.sort(reverse=True)
print("sort 사용 :",list_of_n[1])

# 2) sort 미사용
first = list_of_n[0]
second = list_of_n[1] # [0] 을 헀을 때 리스트 전체가 음수이고
for i in list_of_n:   # 처음 들어오는 값이 제일 큰 값인 경우
    if (i < 0) and (first < 0): # second 값이 first 랑 같아져버리기 때문에 다르게 해야한다.
        if i < first:
            if i > second:
                second = i
    if i > first: # else 를 해버리면 second 가 first 랑 같아져버리기 때문에 안된다.
        second = first
        first = i
        
print("sort 미사용 :",second)
'''