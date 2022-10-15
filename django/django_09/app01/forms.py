from .models import Movie
from django import forms


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = (
            "total_score",
            "avg_score",
            "vote_cnt",
        )
        fields = "__all__"
