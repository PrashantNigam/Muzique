from django.db import models
from django.urls import reverse


class Album(models.Model):

    artist = models.CharField(max_length=250)
    albumTitle = models.CharField(max_length=500, blank=True)
    genre = models.CharField(max_length=100)
    albumLogo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.albumTitle + ' - ' + self.artist


class Song(models.Model):

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    fileType = models.CharField(max_length=10)
    songTitle = models.CharField(max_length=250)
    songImage = models.FileField(null=True, blank=True)
    isFavourite = models.BooleanField(default=False)

    def __str__(self):
        return self.songTitle