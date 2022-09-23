from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    ROLES = [
        (ADMIN, 'Administator'),
        (MODERATOR, 'Moderator'),
        (USER, 'User')
    ]
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        max_length=50,
        choices=ROLES
    )


class Categories(models.Model):
    name = models.CharField(
        'Название категории'
    )
    slug = models.SlugField(
        'Слаг категории',
        unique=True
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title


class Genre(models.Model):
    name = models.CharField(
        'Название жанра',
    )
    slug = models.SlugField(
        'Слаг жанра',
        unique=True,
    )


class Title(models.Model):
    name = models.CharField(
        'Название произведения',
    )
    year = models.IntegerField(
        'Год выпуска произведения',
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        verbose_name='Категория произведения'
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='Жанр произведения'
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self) -> str:
        return self.name
