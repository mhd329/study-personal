from django.db import models
from .models import Article, Comment
from django import forms


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "제목은 100자 이내로 작성해주세요.",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "placeholder": "",
                }
            ),
            "writer": forms.HiddenInput(),
        }
        labels = {
            "title": "제목",
            "content": "내용",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "placeholder": "",
                    "style": "height: 100px; resize: none;",
                }
            ),
            "article": forms.HiddenInput(),
            "writer": forms.HiddenInput(),
        }
        labels = {
            "content": "댓글 쓰기",
        }