from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Можно добавить дополнительные поля, например:
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    # Здесь могут быть другие расширения модели по желанию