# Generated by Django 3.1.2 on 2020-10-15 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ('pub_date', 'title')},
        ),
    ]