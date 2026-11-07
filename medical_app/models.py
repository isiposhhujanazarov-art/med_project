from django.db import models

# Create your models here.

max_length = 255

class category(models.Model):
    name = models.CharField(max_length=max_length, verbose_name='Название категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'    