from django.shortcuts import render, redirect
from .models import Article
from articles.forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib.auth import get_user_model
from accounts.models import UserSession

# Create your views here.
def bbs(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "articles/bbs.html", context)


@login_required
def create(request):
    session_key = UserSession.objects.get()
    session = Session.objects.get(session_key=session_key)
    session_data = session.get_decoded()
    uid = session_data.get("_auth_user_id")
    user = get_user_model().objects.get(id=uid)
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:bbs")
        else:
            pass
    else:
        article_form = ArticleForm(initial={"writer": user})
    context = {
        "article_form": article_form,
    }
    return render(request, "articles/form.html", context)


def detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        "article": article,
    }
    return render(request, "articles/detail.html", context)


@login_required
def update(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == "POST":
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            context = {
                "article": article,
            }
            return render(request, "articles/detail.html", context)
        else:
            pass
    else:
        article_form = ArticleForm(instance=article)
    context = {
        "article_form": article_form,
        "article_id": article.id,
    }
    return render(request, "articles/form.html", context)


@login_required
def delete(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return redirect("articles:bbs")
