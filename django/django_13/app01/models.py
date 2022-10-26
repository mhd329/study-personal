from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to="images/",
        blank=True,
    )
    thumbnail = ProcessedImageField(
        upload_to="thumbnail/",
        processors=[ResizeToFill(500, 400)],
        format="JPEG",
        options={"quality": 60},
        blank=True,
    )
