# Generated by Django 3.1.2 on 2020-10-08 13:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('avatar', models.ImageField(upload_to='persons', verbose_name='person avatar')),
                ('name', models.CharField(max_length=255, verbose_name='person name in English')),
                ('name_ru', models.CharField(blank=True, max_length=255, verbose_name='person name in Russian')),
                ('profession', models.CharField(max_length=255, verbose_name='person profession in English')),
                ('profession_ru', models.CharField(blank=True, max_length=255, verbose_name='person profession in Russian')),
                ('about', models.CharField(max_length=1000, verbose_name='information about person in English')),
                ('about_ru', models.CharField(blank=True, max_length=1000, verbose_name='information about person in Russian')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
