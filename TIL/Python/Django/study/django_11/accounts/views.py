from .forms import CustomCreationUserForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as login_
from django.contrib.auth import logout as logout_
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = CustomCreationUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login_(request, user)
            return redirect("index:main")
        else:
            pass
    else:
        form = CustomCreationUserForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/sign-up.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login_(request, form.get_user())
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
