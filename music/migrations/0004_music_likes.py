# Generated by Django 4.1.1 on 2022-09-24 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_remove_music_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]