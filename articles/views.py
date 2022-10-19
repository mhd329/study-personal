from django.contrib import messages
from .models import Article, Comment, Like
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm, CommentForm, MiniCommentForm

# Create your views here.


def index(request):
    articles = Article.objects.order_by("-id")
    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


def search(request):
    if request.method == "GET":
        articles_search = request.GET.get("article-search")
        searched_articles = Article.objects.filter(
            title__icontains=articles_search
        ).order_by("-id")
        context = {
            "searched_articles": searched_articles,
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
            messages.success(request, "작성하였습니다.")
            return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "articles/form.html", context)


def detail(request, pk):
    target_article = Article.objects.get(id=pk)
    like_ = Like.objects.filter(article=target_article)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = target_article
            comment.user = request.user
            comment.save()
            messages.success(request, "작성하였습니다.")
            return redirect("articles:detail", target_article.pk)
    else:
        form = CommentForm()
    context = {
        "article": target_article,
        "like_": like_,
        "form": form,
    }
    return render(request, "articles/detail.html", context)


@login_required
def update(request, pk):
    user = request.user
    like_ = Like.objects.all()
    article = Article.objects.get(id=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "수정되었습니다.")
            return redirect("articles:detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        "form": form,
        "user": user,
        "like_": like_,
        "article": article,
    }
    return render(request, "articles/form.html", context)


@login_required
def delete(request, pk):
    article = Article.objects.get(id=pk)
    user = request.user
    if request.method == "POST":
        article.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect("articles:index")
    context = {
        "article": article,
        "user": user,
    }
    return render(request, "articles/delete.html", context)


@login_required
def comment_update(request, article_pk, comment_pk):
    user = request.user
    article = Article.objects.get(id=article_pk)
    target_comment = Comment.objects.get(id=comment_pk)
    if user.pk == target_comment.user.pk:
        if request.method == "POST":
            form = MiniCommentForm(request.POST, instance=target_comment)
            if form.is_valid():
                form.save()
                messages.success(request, "수정되었습니다.")
                return redirect("articles:detail", article.pk)
        else:
            form = MiniCommentForm(instance=target_comment)
        context = {
            "target_comment": target_comment,
            "article": article,
            "form": form,
            "user": user,
        }
        return render(request, "articles/detail.html", context)
    else:
        messages.warning(request, "권한이 없습니다.")
        return redirect("articles:detail", article_pk)


@login_required
def comment_delete(request, article_pk, comment_pk):
    user = request.user
    comment = Comment.objects.get(id=comment_pk)
    if user.pk == comment.user.pk:
        comment.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect("articles:detail", article_pk)
    else:
        messages.warning(request, "권한이 없습니다.")
        return redirect("articles:detail", article_pk)


@login_required
def add_like(request, article_pk, user_pk):
    target_article = Article.objects.get(id=article_pk)
    target_user = get_user_model().objects.get(id=user_pk)
    if Like.objects.filter(user=target_user):
        l = Like.objects.filter(user=target_user)
        print(l)
        if l.get(article_id=target_article.pk).exists():
            like_ = Like.objects.get(user=target_user)
            like_.delete()
            return redirect("articles:detail", target_article.pk)
    like_ = Like.objects.create(article=target_article, user=target_user)
    like_.save()
    return redirect("articles:detail", target_article.pk)


# error 처리


def error_400(request, exception):
    return render(request, "400.html", status=400)


def error_403(request, exception):
    return render(request, "403.html", status=403)


def error_404(request, exception):
    return render(request, "404.html", status=404)


def error_500(request):
    return render(request, "500.html", status=500)
