from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator


# Create your models here.
class User(AbstractUser):
    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"


class UserPhoneNumber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(
        max_length=11,
        validators=[MinLengthValidator(11), MaxLengthValidator(11)],
        blank=True,
    )
