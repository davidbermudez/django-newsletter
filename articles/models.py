from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    body = models.TextField(verbose_name='Cuerpo')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    author = models.ForeignKey(
        # settings.AUTH_USER_MODEL,
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


def get_absolute_url():
    return reverse('article_list')


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    comment = models.CharField(
        max_length=140,
        verbose_name='Comentario'
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Autor'
    )

    def __str__(self):
        return self.comment
