from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.bbs, name="bbs"),
    path("create/", views.create, name="create"),
    path("<int:pk>/detail/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/comment/", views.add_comment, name="add-comment"),
    path("<int:pk>/add-like/", views.add_like, name="add-like"),
]
