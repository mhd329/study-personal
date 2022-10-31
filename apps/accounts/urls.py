from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    # 회원가입 페이지
    path("signup/", views.signup, name="signup"),
    # 로그인 페이지
    path("login/", views.login, name="login"),
    # 로그아웃 페이지
    path("logout/", views.logout, name="logout"),
    # 유저 프로필 페이지
    path("detail/<int:pk>/", views.detail, name="detail"),
    # 회원정보 수정 페이지
    path("update/<int:pk>/", views.update, name="update"),
    # 비밀번호 변경 페이지
    path("<int:pk>/password/", views.change_pw, name="password"),
    # 회원탈퇴 페이지
    path("<int:pk>/withdrawal/", views.withdrawal, name="withdrawal"),
    # 팔로우 버튼
    path("<int:pk>/follow/", views.follow, name="follow"),
]
