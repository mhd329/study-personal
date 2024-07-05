from django.urls import path
from . import views

app_name = "articles"


urlpatterns = [
    # 게시판 페이지
    path("reviews/", views.reviews, name="reviews"),
    # 검색된 페이지
    path("search/", views.search, name="search"),
    # 글 생성 페이지
    path("create/", views.create, name="create"),
    # 글 보기
    path("<int:pk>/", views.detail, name="detail"),
    # 글 수정 페이지
    path("<int:pk>/update/", views.update, name="update"),
    # 글 삭제 페이지
    path("<int:pk>/delete/", views.delete, name="delete"),
    # 댓글 수정
    path(
        "<int:article_pk>/comment/<int:comment_pk>/update/",
        views.comment_update,
        name="comment_update",
    ),
    # 댓글 삭제
    path(
        "<int:article_pk>/comment/<int:comment_pk>/delete/",
        views.comment_delete,
        name="comment_delete",
    ),
    # 좋아요 버튼
    path("<int:pk>/add-like/", views.add_like, name="add-like"),
]
