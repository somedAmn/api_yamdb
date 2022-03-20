from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractUser

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'
CHOICES = (
    (USER, 'Аутентифицированный пользователь'),
    (MODERATOR, 'Модератор'),
    (ADMIN, 'Администратор '),
)


class User(AbstractUser):
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=150,
        unique=True
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=254,
        unique=True
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
        blank=True
    )
    bio = models.TextField(
        verbose_name='О себе',
        blank=True
    )
    role = models.CharField(
        verbose_name='Пользовательская роль',
        max_length=10,
        choices=CHOICES,
        default=USER
    )

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    @property
    def is_admin(self):
        return self.role == ADMIN

    class Meta:
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)
        constraints = [
            models.CheckConstraint(
                check=~models.Q(username__iexact='me'),
                name='username_me_is_not_allowed'
            )
        ]

    def __str__(self):
        return self.username


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
