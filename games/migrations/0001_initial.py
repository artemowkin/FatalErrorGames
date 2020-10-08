# Generated by Django 3.1.2 on 2020-10-08 13:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='game title')),
                ('preview', models.ImageField(upload_to='games', verbose_name='game preview')),
                ('short_description', models.CharField(max_length=1000, verbose_name='game short description in English')),
                ('short_description_ru', models.CharField(blank=True, max_length=1000, verbose_name='game short description in Russian')),
                ('description', tinymce.models.HTMLField(verbose_name='game description in English')),
                ('description_ru', tinymce.models.HTMLField(blank=True, verbose_name='game description in Russian')),
                ('video', models.URLField(validators=[django.core.validators.URLValidator(message='A video link need to be from YouTube', regex='https://(?:www.)?youtube.com/watch.*v=.*')], verbose_name='game video link on youtube')),
                ('pub_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GameImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='games', verbose_name='game image')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='games.game', verbose_name='game')),
            ],
        ),
    ]
