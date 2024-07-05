from django.urls import path
from . import views

app_name = "app01"

urlpatterns = [
    path("", views.movies, name="movies"),
    path("create/", views.create, name="create"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/detail/", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/add-score/", views.add_score, name="add-score"),
]
