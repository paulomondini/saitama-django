from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    """Um artigo da wiki/fórum (por exemplo, a página de um personagem)."""

    title = models.CharField('título', max_length=200)
    # O conteúdo é guardado como código HTML e exibido com o filtro |safe.
    content = models.TextField('conteúdo (HTML)')
    posted_at = models.DateTimeField('data de postagem', default=timezone.now)

    class Meta:
        ordering = ['-posted_at']
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})
