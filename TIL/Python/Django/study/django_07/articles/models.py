from django.db import models

# Create your models here.
class Article(models.Model):
    # 제목 캐릭터필드
    # 내용 텍스트필드
    # 작성일 날짜 필드
    # 수정일 날짜 필드
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
