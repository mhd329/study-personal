from django.db import models
from django.conf import settings
from pytz import timezone

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=80)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    created_at = models.DateField(auto_now_add=True)
    completed_at = models.DateField(null=True)
    deadline = models.DateField(null=True)