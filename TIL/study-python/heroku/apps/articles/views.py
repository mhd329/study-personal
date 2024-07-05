from django.views.decorators.http import require_safe, require_POST
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm, CommentForm, MiniCommentForm
from django.contrib.auth.decorators import login_required
from datetime import date, datetime, timedelta
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .models import Article, Comment
from django.contrib import messages
from django.db.models import Q

# Create your views here.
# 게시판 메인 페이지
def reviews(request):
    articles = Article.objects.order_by("-id")
    context = {
        "articles": articles,
    }
    return render(request, "articles/reviews.html", context)


# 글쓰기
@login_required
def create(request):
    user = request.user
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = user
            article.save()
            messages.success(request, "작성하였습니다.")
            return redirect("articles:reviews")
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "articles/form.html", context)


# 검색
def search(request):
    if request.method == "POST":
        search = request.POST["search"]
        searched_users = get_user_model().objects.filter(username__contains=search)
        searched_articles = Article.objects.filter(
            Q(title__icontains=search)
            | Q(content__icontains=search)
            | Q(movie_name__icontains=search)
        )
        context = {
            "search": search,
            "searched_users": searched_users,
            "searched_articles": searched_articles,
        }
        return render(request, "articles/reviews.html", context)


# 글보기
def detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    likes = article.like_users.all()
    likeCount = article.like_users.count()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            messages.success(request, "작성하였습니다.")
            context = {
                "comments": article.comment_set.all,
                "userName": comment.username,
            }
            return JsonResponse(context)
    else:
        form = CommentForm()
    context = {
        "likeCount": likeCount,
        "article": article,
        "likes": likes,
        "form": form,
    }
    return render(request, "articles/detail.html", context)
    # 조회수 로직 긁어옴
    # 올바른 작동에 대한 보장이 없기 때문에 일단 보류해두었음
    # expire_date, now = datetime.now(), datetime.now()
    # expire_date += timedelta(days=1)
    # expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    # expire_date -= now
    # max_age = expire_date.total_seconds()
    # cookie_value = request.COOKIES.get("hitboard", "_")
    # if not f"_{pk}_" in cookie_value:
    #     cookie_value += f"{pk}_"
    #     response.set_cookie(
    #         "hitboard", value=cookie_value, max_age=max_age, httponly=True
    #     )
    #     article.view += 1
    #     article.save()
    article.view += 1
    article.save()
    return response


# 글 수정
@login_required
def update(request, pk):
    user = request.user
    article = get_object_or_404(Article, id=pk)
    likes = article.like_users.all()
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "수정되었습니다.")
            return redirect("articles:detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        "likes": likes,
        "form": form,
        "user": user,
        "article": article,
    }
    return render(request, "articles/form.html", context)


# 글 삭제
@login_required
def delete(request, pk):
    article = get_object_or_404(Article, id=pk)
    user = request.user
    if request.method == "POST":
        article.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect("articles:reviews")
    context = {
        "article": article,
        "user": user,
    }
    return render(request, "articles/delete.html", context)


# 댓글 수정
@login_required
def comment_update(request, article_pk, comment_pk):
    form = CommentForm()
    user = request.user
    article = get_object_or_404(Article, id=article_pk)
    likes = article.like_users.all()
    target_comment = get_object_or_404(Comment, id=comment_pk)
    if user.pk == target_comment.user.pk:
        if request.method == "POST":
            comment_form = MiniCommentForm(request.POST, instance=target_comment)
            if comment_form.is_valid():
                comment_form.save()
                messages.success(request, "수정되었습니다.")
                return redirect("articles:detail", article.pk)
        else:
            comment_form = MiniCommentForm(instance=target_comment)
        context = {
            "target_comment": target_comment,
            "comment_form": comment_form,
            "article": article,
            "likes": likes,
            "form": form,
            "user": user,
        }
        return render(request, "articles/detail.html", context)
    else:
        messages.warning(request, "권한이 없습니다.")
        return redirect("articles:detail", article_pk)


# 댓글 삭제
@login_required
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, id=comment_pk)
    user = request.user
    if user.pk == comment.user.pk:
        comment.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect("articles:detail", article_pk)
    else:
        messages.warning(request, "권한이 없습니다.")
        return redirect("articles:detail", article_pk)


# 추천
@login_required
def add_like(request, pk):
    user = request.user
    article = get_object_or_404(Article, id=pk)
    if article.like_users.filter(id=user.id).exists():
        article.like_users.remove(user)
        is_liked = False
    else:
        article.like_users.add(user)
        is_liked = True
    context = {
        "isLiked": is_liked,
        "likeCount": article.like_users.count(),
    }
    return JsonResponse(context)


# 에러 처리


def error_400(request, exception):
    return render(request, "400.html", status=400)


def error_403(request, exception):
    return render(request, "403.html", status=403)


def error_404(request, exception):
    return render(request, "404.html", status=404)


def error_500(request):
    return render(request, "500.html", status=500)
