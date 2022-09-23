# Generated by Django 2.2.16 on 2022-09-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20220922_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default=1, verbose_name='Биография'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Administator'), ('moderator', 'Moderator'), ('user', 'User')], default='user', max_length=50),
        ),
    ]
