# 9번 문제
# 주어진 리스트가 반장 선거 투표 결과일 때 이영희의 총 득표수를 출력하시오.

# students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
'''
student = input().split()
def elect(votes):
    candidates = set(votes)
    candidates_list = list(candidates)
    num_of_votes = {}
    for candidate in candidates_list:
        num_of_votes[candidate] = 0
        for whose_name in votes:
            if whose_name == candidate:
                num_of_votes[whose_name] += 1
    
    num_of_votes.items()
    return sorted(num_of_votes.items(), key = lambda x : x[1], reverse = True)

print(elect(student))
'''
# 10번 문제
# 주어진 리스트의 요소 중에서 5의 개수를 출력하시오.
'''
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

# numbers = input().split()
def count(numbers):
    num = set(numbers)
    numbers_list = list(num) # 중복되는 값들이 제거된 숫자 리스트
    number_of_counts = {}
    for num in numbers_list:
        number_of_counts[num] = 0
        for n in numbers:
            if n == num:
                number_of_counts[n] += 1
    
    # return sorted(number_of_counts.items(), reverse = True)
    return number_of_counts[5]

print(count(numbers))
'''
# 11번 문제
# 2단부터 9단까지 반복하여 구구단을 출력하세요.
# * 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.
'''
for i in range(2, 10):
    print()
    for j in range(1, 10):
        print(i,"단 :",i * j)
'''
# 12번 문제
# 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.
'''
# 1) replace 함수를 사용했을 때

word = input()
print(word.replace('a',''))

# 2) 사용하지 않고 풀기

word = input()
string_without_a = ''
for s in word:
    # if s is not 'a':
    if s != 'a':
        string_without_a += s
        
print(string_without_a)
'''
'''
일단 == 과 != 는 값 자체를 비교하고,
is 와 is not은 객체를 비교한다.

3과 3.0은 어쨌든 같은 값을 가지니 True가 나온 것이지만,
정수객체와 실수객체는 분명하게 다르기에 False가 나온 것이다.

요즘은 아예 ide 에서 이런 경고메시지가 뜨기도 한다.

SyntaxWarning: "is" with a literal. Did you mean "=="?

is 를 값 비교에 쓰지 말라는 경고 문구다.

is 는 True나 False, None 과 비교할 때만 사용하자!
출처 : https://ffoorreeuunn.tistory.com/465
'''
# 13번 문제
# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
'''
word = input() # a, p, p, l, e
reversed_word = ''
for s in word:
    reversed_word = s + reversed_word # a + '' / p + a / p + pa ...

print(reversed_word)

# 다른 사람의 풀이

word = 'apple'

for i in range(len(word)):
    print(word[(len(word)-1)-i], end='')


'''
# 예제 01 기초함수
# 숫자 n을 받아 세제곱 결과를 반환하는 함수 cube를 정의하시오. 
# cube 함수를 호출하여 12의 세제곱 결과를 출력하시오
'''
n = int(input())

def cube(n):
    return n**3

print(cube(n))
'''
# 예제 02 기초함수
# 가로와 세로의 길이를 각각 a, b로 받아 사각형 넓이와 둘레를 함께 반환하는 함수 rectangle을 정의하시오. 
# 사각형이 가로가 20, 세로가 30일 때의 결과를 출력하시오.

# * 사각형 넓이 : 가로 * 세로
# * 사각형 둘레 : (가로 + 세로) * 2
'''
a, b = input().split()
def rectangle(a, b):
    a = int(a)
    b = int(b)
    rectangle_properties = {}
    rectangle_properties["가로"] = a
    rectangle_properties["세로"] = b
    rectangle_properties["둘레"] = (a + b) * 2
    rectangle_properties["넓이"] = a * b
    return rectangle_properties["넓이"], rectangle_properties["둘레"]

print(rectangle(a, b))
'''