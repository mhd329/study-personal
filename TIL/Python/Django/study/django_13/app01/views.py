from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib import messages
import os

# Create your views here.
def index(request):
    articles = Article.objects.order_by("-id")
    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "글 작성 완료")
            return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "articles/form.html", context)


def detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        "article": article,
    }
    return render(request, "articles/detail.html", context)


def update(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)

        if article.thumbnail:
            thumbnail_path = str(article.thumbnail.path)
            if article.thumbnail and request.FILES.get("thumbnail"):
                os.remove(article.thumbnail.path)
        if article.image:
            image_path = str(article.image.path)
            if article.image and request.FILES.get("image"):
                os.remove(article.image.path)

        if form.is_valid():
            if request.POST.get("thumbnail-clear"):
                os.remove(thumbnail_path)
            if request.POST.get("image-clear"):
                os.remove(image_path)
            form.save()
            return redirect("articles:index")
    else:
        form = ArticleForm(instance=article)
    context = {
        "form": form,
    }
    return render(request, "articles/form.html", context)


def delete(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    if article.thumbnail:
        os.remove(article.thumbnail.path)
    if article.image:
        os.remove(article.image.path)
    return redirect("articles:index")
