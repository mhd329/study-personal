from .models import Article, Comment
from django import forms


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            "title",
            "content",
        )
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "제목은 80자 이내로 작성해주세요.",
                    "style": "height: 2.5rem; resize: none;",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "placeholder": "",
                    "style": "height: 15rem; resize: none;",
                }
            ),
        }
        labels = {
            "title": "제목",
            "content": "내용",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "placeholder": "",
                    "style": "height: 100px; resize: none;",
                }
            ),
        }
        labels = {
            "content": "댓글",
        }


class MiniCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "placeholder": "",
                    "style": "height: 50px; resize: none;",
                }
            ),
        }
        labels = {
            "content": "",
        }
