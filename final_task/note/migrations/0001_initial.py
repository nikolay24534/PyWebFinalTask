# Generated by Django 3.1.7 on 2021-04-11 12:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('massage', models.TextField(verbose_name='Текст')),
                ('date_time', models.DateTimeField(default=datetime.datetime(2021, 4, 12, 12, 41, 29, 490820), verbose_name='Дата публикации')),
                ('public', models.BooleanField(verbose_name='Опубликовано')),
                ('status', models.IntegerField(choices=[(0, 'Активно'), (1, 'Отложено'), (2, 'Выполнено')], default=0, verbose_name='Статус')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Заметки',
                'verbose_name_plural': 'Заметки',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('message', models.TextField(blank=True, default='', verbose_name='Текст комментария')),
                ('rating', models.IntegerField(choices=[(0, 'Без оценки'), (1, 'Ужасно'), (2, 'Плохо'), (3, 'Нормально'), (4, 'Хорошо'), (5, 'Отлично')], default=0, verbose_name='Оценка')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='note.note', verbose_name='Заметка')),
            ],
        ),
    ]
