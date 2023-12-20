from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    return render(request, "app01/index.html")


def noticeboard(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "app01/noticeboard.html", context)


def create(request, pk):
    if pk:
        article = Article.objects.get(id=pk)
        if request.method == "POST":
            article_form = ArticleForm(request.POST, instance=article)
            article.change_cnt += 1
            article_form.save()
            context = {
                "article": article,
            }
            return render(request, "app01/detail.html", context)
        else:
            article_form = ArticleForm(instance=article)
        context = {
            "article_form": article_form,
        }
        return render(request, "app01/create.html", context)

    else:
        if request.method == "POST":
            article_form = ArticleForm(request.POST)
            if article_form.is_valid():
                article_form.save()
                return redirect("app01:noticeboard")
            else:
                pass
        else:
            article_form = ArticleForm()
        context = {
            "article_form": article_form,
            "pk": pk,
        }
        return render(request, "app01/create.html", context)


def detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        "article": article,
    }
    return render(request, "app01/detail.html", context)


def delete(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return redirect("app01:noticeboard")
