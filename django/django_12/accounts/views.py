from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login as login_
from django.contrib.auth import logout as logout_
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):  # 전체 회원 목록
    users = get_user_model().objects.order_by("-id")
    context = {
        "users": users,
    }
    return render(request, "accounts/index.html", context)


def sign_up(request):  # 회원 가입
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login_(request, user)
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/sign-up.html", context)


def login(request):  # 로그인
    if request.method == "POST":
        print(request)
        print("#" * 30)
        print(request.POST)
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login_(request, get_user_model())
            return redirect(request.GET.get("next") or "accounts:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


@login_required
def user_info(request, pk):  # 회원 정보 조회 및 수정
    user = get_user_model().objects.get(id=pk)
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("accounts:userinfo", user.pk)
    else:
        form = CustomUserChangeForm(instance=user)
    context = {
        "form": form,
    }
    return render(request, "accounts/userinfo.html", context)


@login_required
def update(request, pk):
    user = get_user_model().objects.get(id=pk)
    return redirect("accounts:userinfo", user.pk)


@login_required
def update_password(request):  # 패스워드 변경
    return render(request, "accounts/update-password.html")


@login_required
def logout(request):  # 로그아웃
    logout_(request)
    return redirect("accounts:index")
