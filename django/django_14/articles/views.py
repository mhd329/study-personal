from .models import Article
from django.contrib import messages
from .forms import ArticleForm, CommentForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Article.objects.order_by("-id")
    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


@login_required
def create(request):
    user = request.user
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = user
            article.save()
            return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "articles/form.html", context)


def detail(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect("articles:detail", article.pk)
    else:
        form = CommentForm()
    context = {
        "article": article,
        "form": form,
    }
    return render(request, "articles/detail.html", context)


@login_required
def update(request, pk):
    user = request.user
    article = Article.objects.get(id=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("articles:detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        "form": form,
        "user": user,
        "article": article,
    }
    return render(request, "articles/form.html", context)


@login_required
def delete(request, pk):
    article = Article.objects.get(id=pk)
    user = request.user
    if request.method == "POST":
        article.delete()
        return redirect("articles:index")
    context = {
        "article": article,
        "user": user,
    }
    return render(request, "articles/delete.html", context)


@login_required
def add_comment(request):
    pass
