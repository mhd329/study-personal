from curses import start_color
import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# 아래에 코드를 기록하세요.
# 코드 실행은 터미널에서 shell을 실행시켜서 해주세요. 
# $ python manage.py shell_plus 

# 03

directors = [
    ("봉준호","1993-01-01","KOR"),
    ("김한민","1999-01-01","KOR"),
    ("최동훈","2004-01-01","KOR"),
    ("이정재","2022-01-01","KOR"),
    ("이경규","1992-01-01","KOR"),
    ("한재림","2005-01-01","KOR"),
    ("Joseph Kosinski","1999-01-01","KOR"),
    ("김철수","2022-01-01","KOR"),
]

for director in directors:
    name_ = director[0]
    debut_ = director[1]
    country_ = director[2]
    Director.objects.create(name=name_, debut=debut_, country=country_)

genres = ["액션","드라마","사극","범죄","스릴러","SF","무협","첩보","재난"]

for title_ in genres:
    genre = Genre()
    genre.title = title_
    genre.save()

# 04

mr_bong = Director.objects.get(name = "봉준호")
print("id :", mr_bong.id)
print("name :", mr_bong.name)
print("debut :", mr_bong.debut)
print("country :", mr_bong.country)

# 05

drama = Genre.objects.get(title = "드라마")
print("id :", drama.id)
print("title :", drama.title)

# 06

Movie.objects.create(
    director = mr_bong,
    genre = drama, title = "기생충",
    opening_date = "2019-05-30",
    running_time = 132,
    screening = False)

# 07

movies =\
[
    ("봉준호", "드라마", "괴물", "2006-07-27", 119, False),
    ("봉준호", "SF", "설국열차", "2013-10-30", 125, False),
    ("김한민", "사극", "한산", "2022-07-27", 129, True),
    ("최동훈", "SF", "외계+인", "2022-07-20", 142, False),
    ("이정재", "첩보", "헌트", "2022-08-10", 125, True),
    ("이경규", "액션", "복수혈전", "1992-10-10", 88, False),
    ("한재림", "재난", "비상선언", "2022-08-03", 140, True),
    ("Joseph Kosinski", "액션", "탑건 : 매버릭", "2022-06-22", 130, True),
]

for m in movies:
    movie = Movie()
    movie.director = Director.objects.get(name = m[0])
    movie.genre = Genre.objects.get(title = m[1])
    movie.title = m[2]
    movie.opening_date = m[3]
    movie.running_time = m[4]
    movie.screening = m[5]
    movie.save()

# 08

movies = Movie.objects.all()
for movie in movies:
    print(movie.director, end = ' ')
    print(movie.genre, end = ' ')
    print(movie.title, end = ' ')
    print(movie.opening_date, end = ' ')
    print(movie.running_time, end = ' ')
    print(movie.screening)

# 09

movies = Movie.objects.all()
for movie in movies:
    print(movie.director.name, end = ' ')
    print(movie.genre, end = ' ')
    print(movie.title, end = ' ')
    print(movie.opening_date, end = ' ')
    print(movie.running_time, end = ' ')
    print(movie.screening)

# 10

movies = Movie.objects.all()
for movie in movies:
    print(movie.director.name, end = ' ')
    print(movie.genre.title, end = ' ')
    print(movie.title, end = ' ')
    print(movie.opening_date, end = ' ')
    print(movie.running_time, end = ' ')
    print(movie.screening)

# 11

movies = Movie.objects.order_by("-opening_date")
for movie in movies:
    print(movie.director.name, end = ' ')
    print(movie.genre.title, end = ' ')
    print(movie.title, end = ' ')
    print(movie.opening_date, end = ' ')
    print(movie.running_time, end = ' ')
    print(movie.screening)

# 12

movie = Movie.objects.order_by("opening_date")[0]
print(movie.director.name, end = ' ')
print(movie.genre.title, end = ' ')
print(movie.title, end = ' ')
print(movie.opening_date, end = ' ')
print(movie.running_time, end = ' ')
print(movie.screening)

# 13

movies = Movie.objects.filter(screening = True).order_by("opening_date")
for movie in movies:
    print(movie.director.name, end = ' ')
    print(movie.genre.title, end = ' ')
    print(movie.title, end = ' ')
    print(movie.opening_date, end = ' ')
    print(movie.running_time, end = ' ')
    print(movie.screening)

# 14

mr_bong = Director.objects.get(name = "봉준호")
movies = Movie.objects.filter(director = mr_bong).order_by("opening_date")
for movie in movies:
    print(movie.director.name, end = ' ')
    print(movie.genre.title, end = ' ')
    print(movie.title, end = ' ')
    print(movie.opening_date, end = ' ')
    print(movie.running_time, end = ' ')
    print(movie.screening)

# 15

mr_bong = Director.objects.get(name = "봉준호")
movie = Movie.objects.filter(director = mr_bong).order_by("opening_date")[1]
print(movie.director.name, end = ' ')
print(movie.genre.title, end = ' ')
print(movie.title, end = ' ')
print(movie.opening_date, end = ' ')
print(movie.running_time, end = ' ')
print(movie.screening)

# 16

movies = Movie.objects.filter(running_time__gt = 119).order_by("running_time")
for movie in movies:
    print(movie.director.name, end = ' ')
    print(movie.genre.title, end = ' ')
    print(movie.title, end = ' ')
    print(movie.opening_date, end = ' ')
    print(movie.running_time, end = ' ')
    print(movie.screening)

# 17

movies = Movie.objects.filter(running_time__gte = 119).order_by("running_time")
for movie in movies:
    print(movie.director.name, end = ' ')
    print(movie.genre.title, end = ' ')
    print(movie.title, end = ' ')
    print(movie.opening_date, end = ' ')
    print(movie.running_time, end = ' ')
    print(movie.screening)

# 18

from datetime import date

start_date = ("2022-01-01")
today_ = date.today().isoformat()

movies = Movie.objects.filter(opening_date__range = (start_date, today_)).order_by("opening_date")

for movie in movies:
    print(movie.director.name, end = ' ')
    print(movie.genre.title, end = ' ')
    print(movie.title, end = ' ')
    print(movie.opening_date, end = ' ')
    print(movie.running_time, end = ' ')
    print(movie.screening)

# 19

drama = Genre.objects.get(title = "드라마")
mr_bong = Director.objects.get(name = "봉준호")
movies = Movie.objects.filter(director = mr_bong, genre = drama).order_by("opening_date")

for movie in movies:
    print(movie.director.name, end = ' ')
    print(movie.genre.title, end = ' ')
    print(movie.title, end = ' ')
    print(movie.opening_date, end = ' ')
    print(movie.running_time, end = ' ')
    print(movie.screening)

# 20

mr_bong = Director.objects.get(name = "봉준호")
movies = Movie.objects.exclude(director = mr_bong).order_by("opening_date")
for movie in movies:
    print(movie.director.name, end = ' ')
    print(movie.genre.title, end = ' ')
    print(movie.title, end = ' ')
    print(movie.opening_date, end = ' ')
    print(movie.running_time, end = ' ')
    print(movie.screening)