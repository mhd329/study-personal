from django.shortcuts import render, redirect
from .forms import ArticleForm

# Create your views here.
def articles(request):
    return render(request, "app01/articles.html")


def create(request):
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect("app01/articles")
        else:
            pass
    else:
        article_form = ArticleForm()
    context = {
        "article_form": article_form,
    }
    return render(request, "app01/articles.html", context)
