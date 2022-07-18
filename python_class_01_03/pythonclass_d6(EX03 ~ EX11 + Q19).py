# -- coding: utf-8 --
# 03
'''
두 수를 Input으로 받아 합을 구하는 코드이다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.



numbers = list(map(int, input().split()))

print(sum(numbers))
'''
# 04
'''
아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.

words = input().split()
print(words)
'''
# 05
'''
아래 코드는 숫자의 길이를 구하는 코드입니다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.

number = str(22020718)
print(len(number))
'''
# 06
'''
아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.

N = 10
answer = []
for number in range(1, N + 1):
    answer.append(number * 2)

print(answer)
'''
# 07
'''
아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
코드에서 오류를 찾아 원인을 적고, 수정하세요.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)
'''
# 08
'''
아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
코드에서 오류를 찾아 원인을 적고, 수정하세요.

word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count += 1

print(count)
'''
# 09
'''
아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.

from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)
'''
# 10
'''
아래 코드는 리스트에서 최댓값을 구하는 코드입니다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.

number_list = [1, 23, 9, 6, 91, 59, 29]
max1 = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max1 > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max1 < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")
'''
# 11
'''
아래 코드는 영화의 장르id를 장르 이름으로 바꿔서 영화 정보를 출력하는 코드입니다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.

from pprint import pprint


def movie_info(movie, genres):
    genres_names = []
    genre_ids = movie["genre_ids"] # [18, 80]
    for genre_id in genre_ids: # [18]
        for genre in genres:
            if genre_id == genre["id"]:
                genre_name = genre["name"]
                genres_names.append(genre_name)

    new_movie_info = {
        "genre_names": genres_names,
        "id": movie["id"],
        "overview": movie["overview"],
        "title": movie["title"],
        "vote_average": movie["vote_average"],
    }
    
    return new_movie_info

if __name__ == "__main__":
    movie = {
        "adult": False,
        "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
        "genre_ids": [18, 80],
        "id": 278,
        "original_language": "en",
        "original_title": "The Shawshank Redemption",
        "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
        "popularity": 67.931,
        "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
        "release_date": "1995-01-28",
        "title": "쇼생크 탈출",
        "video": False,
        "vote_average": 8.7,
        "vote_count": 18040,
    }

    genres_list = [
        {"id": 28, "name": "Action"},
        {"id": 12, "name": "Adventure"},
        {"id": 16, "name": "Animation"},
        {"id": 35, "name": "Comedy"},
        {"id": 80, "name": "Crime"},
        {"id": 99, "name": "Documentary"},
        {"id": 18, "name": "Drama"},
        {"id": 10751, "name": "Family"},
        {"id": 14, "name": "Fantasy"},
        {"id": 36, "name": "History"},
        {"id": 27, "name": "Horror"},
        {"id": 10402, "name": "Music"},
        {"id": 9648, "name": "Mystery"},
        {"id": 10749, "name": "Romance"},
        {"id": 878, "name": "Science Fiction"},
        {"id": 10770, "name": "TV Movie"},
        {"id": 53, "name": "Thriller"},
        {"id": 10752, "name": "War"},
        {"id": 37, "name": "Western"},
    ]

    pprint(movie_info(movie, genres_list))
'''
# 19
'''
양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

n = int(input())

cnt = 0
while n >= 10:
    n //= 10
    cnt += 1
    
if cnt == 0:
    print('1')
else:
    print(cnt + 1)
'''