from django.db import models

from apps.user.models import User

class News(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название',
    )
    description = models.TextField(
        verbose_name='Текст',
    )
    image = models.ImageField(
        upload_to='news/',
        verbose_name='Изображение',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )



    
    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'