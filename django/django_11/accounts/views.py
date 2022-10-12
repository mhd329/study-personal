from .forms import CustomCreationUserModel
from django.contrib.auth import get_user_model
from django.contrib.auth import login as login_
from django.contrib.auth import logout as logout_
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from django.contrib.sessions.models import Session
from .models import UserSession

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = CustomCreationUserModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index:main")
        else:
            pass
    else:
        form = CustomCreationUserModel()
    context = {
        "form": form,
    }
    return render(request, "accounts/sign-up.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login_(request, form.get_user())
            UserSession.objects.create(
                user=form.get_user(), session_id=request.session.session_key
            )
            return redirect(request.GET.get("next") or "index:main")
        else:
            pass
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def user(request, pk):
    user = get_user_model().objects.get(id=pk)
    context = {
        "user": user,
    }
    return render(request, "accounts/user.html", context)


def logout(request):
    logout_(request)
    return redirect("index:main")
