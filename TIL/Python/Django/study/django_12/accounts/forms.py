from dataclasses import field
from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)
        labels = {
            "username": "아이디",
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "first_name",
            "last_name",
            "email",
        )
        labels = {
            "first_name": "이름",
            "last_name": "성",
            "email": "이메일",
        }
