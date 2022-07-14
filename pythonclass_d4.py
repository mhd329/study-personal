# 14번 문제
# 문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
# count() 메서드 사용 금지
'''
word = input()
cnt = 0
for s in word:
    if s == 'a':
        cnt += 1
        
print(cnt)
'''
# 15-1번 문제
# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

# 15-2번 문제
# 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지
'''
word = input()

def search(word):
    string_length = ""
    for s in word:
        if s != 'a':
            string_length += s
            if len(string_length) == len(word):
                return -1
        else:
            return len(string_length)
        
print(search(word))
'''
# 16번 문제
# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지
'''
word = input()
vowel = ""

for s in word:
    if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
        vowel += s

print(len(vowel))
'''
# 17번 문제
# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지
'''
word = input()

for s in word:
    ord_s = ord(s)
    lower_ord_s = ord_s - 32
    upper_s = chr(lower_ord_s)
    print(upper_s, end='')
'''
# 18번 문제
# 문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.
'''
word = input()
cnt_alphabet = {}

for i in word: # 'banana'
    cnt_alphabet[i] = 0
    for j in word:
        if j == i:
            cnt_alphabet[i] += 1

for a, b in cnt_alphabet.items():
    print(a, b)
'''