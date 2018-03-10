# Generated by Django 2.0.2 on 2018-02-28 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_songimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='isFavourite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='album',
            name='albumLogo',
            field=models.FileField(max_length=1000, upload_to=''),
        ),
    ]