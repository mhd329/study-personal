from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def today_dinner(request):
    foods = {
        '더덕구이' : 'https://recipe1.ezmember.co.kr/cache/recipe/2017/03/22/2bd7f1fb93d4410effbd88ff3414998c1.jpg',
        '냉모밀 소바' : 'https://shop4.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop4.daumcdn.net%2Fshophow%2Fp%2FH13228978643.jpg%3Fut%3D20211229230053',
        '그냥 라면' : 'https://health.chosun.com/site/data/img_dir/2020/09/07/2020090702900_0.jpg',
        '굽네치킨' : 'http://www.dailymedipharm.com/news/photo/201701/32696_163_815.jpg',
        '햄버거' : 'https://newsimg.sedaily.com/2021/01/28/22HFJRTY6N_2.jpg',
    }
    menu = []
    
    for k, v in foods.items():
        menu.append([k, v])
    
    food = random.choice(menu)
    
    context = {
        'food' : food[0],
        'img' : food[1],
    }
    return render(request, 'today-dinner.html', context)

def lotto_pick(request):
    prize = [{3, 11, 15, 29, 35, 44}, 10]
    # numbers = [3, 11, 15, 29, 35, 44]
    numbers = random.sample(range(1, 46), 7)
    cnt = 0
    bonus = False
    for num in numbers:
        if num in prize[0]:
            cnt += 1
    else:
        if prize[1] in numbers:
            bonus = True
            
        if cnt == 6:
            rank = '1등'
        elif cnt == 5 and bonus:
            rank = '2등'
        elif cnt == 5:
            rank = '3등'
        elif cnt == 4:
            rank = '4등'
        elif cnt == 3:
            rank = '5등'
        else:
            rank = '꽝'
        
    context = {
        'nums' : numbers,
        'rank' : rank,
    }
    return render(request, 'lotto-pick.html', context)