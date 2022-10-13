from django.shortcuts import render, redirect
from .models import Article, Comment, Like
from articles.forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required


# from django.contrib.sessions.models import Session
# from django.contrib.auth import get_user_model
# def get_session_key(request):
#     session_key = request.session.session_key
#     session = Session.objects.get(session_key=session_key)
#     session_data = session.get_decoded()
#     uid = session_data.get("_auth_user_id")
#     return get_user_model().objects.get(id=uid)


# Create your views here.
def bbs(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "articles/bbs.html", context)


@login_required
def create(request):
    user = request.user
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
    user = request.user
    article = Article.objects.get(id=pk)
    like_ = Like.objects.all()
    comments = Comment.objects.all()
    comment_form = CommentForm(
        initial={
            "article": article,
            "writer": user,
        }
    )
    context = {
        "like_": like_,
        "article": article,
        "comments": comments,
        "comment_form": comment_form,
    }
    return render(request, "articles/detail.html", context)


@login_required
def update(request, pk):
    user = request.user
    like_ = Like.objects.all()
    article = Article.objects.get(id=pk)
    comments = Comment.objects.all()
    comment_form = CommentForm(
        initial={
            "article": article,
            "writer": user,
        }
    )
    if request.method == "POST":
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            context = {
                "like_": like_,
                "article": article,
                "comments": comments,
                "comment_form": comment_form,
            }
            return render(request, "articles/detail.html", context)
        else:
            pass
    else:
        article_form = ArticleForm(instance=article)
    context = {
        "like_": like_,
        "article": article,
        "article_form": article_form,
        "user": user,
    }
    return render(request, "articles/form.html", context)


@login_required
def delete(request, pk):
    user = request.user
    article = Article.objects.get(id=pk)
    if article.writer == user or user.is_superuser:
        article.delete()
        return redirect("articles:bbs")
    else:
        return render(request, "articles/form.html")


@login_required
def add_comment(request, pk):
    article = Article.objects.get(id=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment_form.save()
    return redirect("articles:detail", article.pk)


@login_required
def add_like(request, pk):
    user = request.user
    article = Article.objects.get(id=pk)
    if Like.objects.filter(user=user).exists():
        already_like = Like.objects.get(user=user)
        already_like.delete()
        return redirect("articles:detail", article.pk)
    else:
        like_ = Like.objects.create(article=article, user=user)
        like_.save()
        return redirect("articles:detail", article.pk)
