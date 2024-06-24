from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(
        max_length=50,
        verbose_name='Никнейм'
    )
    avatar = models.ImageField(
        upload_to= 'avatar/',
        verbose_name='аватарка'
    )
    bio = models.TextField(
        verbose_name='Биография',
    )


    def __str__(self):
        return self.username


    class Meta:
        verbose_name="Пользователь"
        verbose_name_plural="Пользователи"