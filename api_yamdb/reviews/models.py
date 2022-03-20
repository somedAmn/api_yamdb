from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

class Category(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Категория',
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Адрес',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Жанр',
    )
    slug = models.SlugField(
        unique=True,
        verbose_name = 'Адрес',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name = 'Произведение',
    )
    year = models.IntegerField(
        verbose_name='Год выхода',
        validators=(MaxValueValidator(
            timezone.now().year,
            message='Год не может быть больше текущего!'),)
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name = 'Описание',
    )
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Категория'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
