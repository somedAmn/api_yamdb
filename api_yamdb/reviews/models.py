from django.contrib.auth.models import AbstractUser
from django.db import models

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
