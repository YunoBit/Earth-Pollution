# from django.db import models

# from apps.news.models import News
# from apps.user.models import User

# class Comment(models.Model):
#     news = models.ForeignKey(
#         News,
#         on_delete=models.CASCADE,
#         verbose_name="News",
#         related_name="comments"
#     )
#     author = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         verbose_name="Пользователь",
#     )
#     text = models.CharField(
#         max_length=500,
#         verbose_name="Текст",
#     )
#     created_at = models.DateTimeField(
#         auto_now_add=True,
#         verbose_name="Время добавления",
#     )
#     reply_comment = models.ForeignKey(
#         'self',
#         on_delete=models.SET_NULL,
#         related_name='replies',
#         null=True,
#         blank=True,
#         verbose_name="Ответ на комментарий"
#     )

#     def __str__(self):
#         return f"{self.author} - {self.news.title} - {self.text}"

#     class Meta:
#         verbose_name = "Комментарий"
#         verbose_name_plural = "Комментарии"
