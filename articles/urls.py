from . import views
from django.urls import path

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/add-like", views.add_like, name="add-like"),
    path(
        "<int:article_pk>/comment/<int:comment_pk>/update/",
        views.comment_update,
        name="comment_update",
    ),
    path(
        "<int:article_pk>/delete/<int:comment_pk>/delete/",
        views.comment_delete,
        name="comment_delete",
    ),
]
