from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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


class Title(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='titles'
    )
    text = models.TextField(
        'Текст',
        max_length=200
    )
    pub_date = models.DateTimeField(
        'Дата',
        auto_now_add=True
    )


class Reviews(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор отзыва'
    )
    text = models.TextField(
        'Текст отзыва',
        max_length=200,
    )
    pub_date = models.DateTimeField(
        'Дата отзыва',
        auto_now_add=True,
    )
    score = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    constraints = [
        models.UniqueConstraint(
            fields=['author', ],
            name='unique_follow'
        )
    ]

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    review = models.ForeignKey(
        Reviews(),
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        User(),
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )
    text = models.TextField(
        'Текст комментария',
        max_length=200,
    )
    pub_date = models.DateTimeField(
        'Дата комментария',
        auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:15]
