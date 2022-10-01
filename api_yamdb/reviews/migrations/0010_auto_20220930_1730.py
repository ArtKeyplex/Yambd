# Generated by Django 2.2.16 on 2022-09-30 14:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_categories_comment_genre_reviews_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=300, verbose_name='Описание произведения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='rating',
            field=models.IntegerField(default=None, null=True, verbose_name='Рейтинг произведения'),
        ),
    ]