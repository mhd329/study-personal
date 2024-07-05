from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, "index.html")


def is_odd_even(request, num):
    context = {
        "num": num,
    }
    return render(request, "is-odd-even.html", context)


def calc(request, num1, num2):
    context = {
        "num1": num1,
        "num2": num2,
    }
    return render(request, "calc.html", context)


def random_life(request):
    return render(request, "random-life.html")


def life(request):
    name = request.GET.get("q")
    prefix_list = ["귀여운", "엉뚱한", "날렵한", "힘쌘", "건강한", "장수한", "작은", "커다란"]
    animals = [
        "호랑이",
        "사자",
        "개",
        "고양이",
        "양",
        "소",
        "말",
        "쥐",
        "뱀",
        "오리",
        "펭귄",
        "가물치",
        "넙치",
        "닭",
        "원숭이",
    ]
    animal = random.choice(animals)
    prefix = random.choice(prefix_list)
    context = {
        "name": name,
        "animal": animal,
        "prefix": prefix,
    }
    return render(request, "life.html", context)


def kripsum(request):
    return render(request, "kripsum.html")


def kripsum_print(request):
    total_words = request.GET.get("total-words")
    total_paragraph = request.GET.get("total-paragraph")
    words = [
        "작은",
        "나의",
        "여름이었다.",
        "봄날에,",
        "귀여운",
        "친구",
        "참으로",
        "나에게",
        "좋았다!!!",
        "지루했다...",
        "반가운",
        "얼굴",
        "나는",
        "너의",
        "영원한",
        "형제",
        "유리컵",
        "물병",
        "매화",
        "꽃",
        "한송이",
    ]
    section = []
    for _ in range(int(total_paragraph)):
        body = ""
        for _ in range(int(total_words)):
            body += random.choice(words) + " "
        section.append(body)
    context = {
        "section": section,
    }
    return render(request, "kripsum-print.html", context)
