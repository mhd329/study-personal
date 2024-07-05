from . import views
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path("", views.members, name="members"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("<int:pk>/", views.profile, name="profile"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/password/", views.change_pw, name="password"),
    path("<int:pk>/withdrawal/", views.withdrawal, name="withdrawal"),
]
