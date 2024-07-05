from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("sign-up/", views.sign_up, name="sign-up"),
    path("<int:pk>/", views.user, name="user"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
