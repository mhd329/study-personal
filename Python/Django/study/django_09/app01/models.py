from email.policy import default
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Movie(models.Model):
    img = models.ImageField(upload_to="", default="dummy.png")
    title = models.CharField(max_length=30)
    summary = models.TextField()
    running_time = models.IntegerField()
    director = models.TextField()
    release = models.DateField(auto_now=False, auto_now_add=False)
    total_score = models.IntegerField(
        default=0, validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    avg_score = models.IntegerField(default=0)
    vote_cnt = models.IntegerField(default=0)
