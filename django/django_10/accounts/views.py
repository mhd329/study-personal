from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# Create your views here.
def user(request):
    return render(request, "accounts/user.html")


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index:main")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)
