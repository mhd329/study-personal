from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("sign-up/", views.sign_up, name="sign-up"),
    path("login/", views.login, name="login"),
    path("<int:pk>/userinfo/", views.user_info, name="userinfo"),
    path("<int:pk>/update/", views.update, name="update"),
    path("update-password/", views.update_password, name="update-password"),
    path("logout/", views.logout, name="logout"),
]
