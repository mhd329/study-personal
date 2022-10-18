from django.contrib import messages
from .forms import UserPhoneNumberForm
from accounts.models import UserPhoneNumber
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login as login_
from django.contrib.auth import logout as logout_
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

# Create your views here.
@login_required
def members(request):
    users = get_user_model().objects.order_by("-id")
    context = {
        "users": users,
    }
    return render(request, "accounts/members.html", context)


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        pn_form = UserPhoneNumberForm(request.POST)
        if form.is_valid() and pn_form.is_valid():
            user = form.save()
            user_phone_number = pn_form.save(commit=False)
            user_phone_number.user = user
            phone = user_phone_number.phone
            p1 = "".join(phone[:3])
            p2 = "".join(phone[3:7])
            p3 = "".join(phone[7:])
            phone = "-".join([p1, p2, p3])
            user_phone_number.phone = phone
            user_phone_number.save()
            login_(request, user)
            return redirect("articles:index")
    else:
        form = CustomUserCreationForm()
        pn_form = UserPhoneNumberForm()
    context = {
        "form": form,
        "pn_form": pn_form,
    }
    return render(request, "accounts/form.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            login_(request, form.get_user())
            return redirect(request.GET.get("next") or "articles:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


@login_required
def profile(request, pk):
    now_user = request.user
    other_user = get_user_model().objects.get(id=pk)
    context = {
        "now_user": now_user,
        "other_user": other_user,
    }
    return render(request, "accounts/profile.html", context)


@login_required
def update(request, pk):
    now_user = request.user
    other_user = get_user_model().objects.get(id=pk)
    if other_user.username != "admin":
        phone = other_user.userphonenumber
    else:
        messages.error(request, "admin 계정은 일반 페이지에서 수정이 불가능합니다.")
        return redirect("accounts:profile", other_user.pk)
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=other_user)
        pn_form = UserPhoneNumberForm(request.POST, instance=phone)
        if form.is_valid() and pn_form.is_valid():
            user = form.save()
            user_phone_number = pn_form.save(commit=False)
            user_phone_number.user = user
            phone = user_phone_number.phone
            p1 = "".join(phone[:3])
            p2 = "".join(phone[3:7])
            p3 = "".join(phone[7:])
            phone = "-".join([p1, p2, p3])
            user_phone_number.phone = phone
            user_phone_number.save()
            return redirect("accounts:profile", other_user.pk)
    else:
        form = CustomUserChangeForm(instance=other_user)
        pn_form = UserPhoneNumberForm(instance=phone)
    context = {
        "form": form,
        "pn_form": pn_form,
        "now_user": now_user,
        "other_user": other_user,
    }
    return render(request, "accounts/form.html", context)


@login_required
def logout(request):
    logout_(request)
    return redirect("articles:index")


@login_required
def withdrawal(request):
    if request.method == "POST":
        request.user.delete()
        logout_(request)
        return redirect("articles:index")
    else:
        return render(request, "accounts/withdrawal.html")


@login_required
def change_pw(request):
    user = request.user
    if request.method == "POST":
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "비밀번호가 변경되었습니다.")
            return redirect("accounts:profile", user.pk)
    else:
        form = PasswordChangeForm(user)
    context = {
        "form": form,
        "user": user,
    }
    return render(request, "accounts/change.html", context)
