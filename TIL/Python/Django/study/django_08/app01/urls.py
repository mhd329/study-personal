from django.urls import path
from app01 import views

app_name = "app01"

urlpatterns = [
    path("", views.index, name="index"),
    path("noticeboard/", views.noticeboard, name="noticeboard"),
    path("<int:pk>/create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/delete", views.delete, name="delete"),
]
