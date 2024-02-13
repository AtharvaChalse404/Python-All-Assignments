# models.py
from django.db import models

class AudioManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type='Audio')

class VideoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type='Video')

class ImageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type='Image')

class Media(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    format = models.CharField(max_length=100)
    size = models.IntegerField()
    duration_secs = models.IntegerField(default=0)

    audio = AudioManager()
    video = VideoManager()
    image = ImageManager()

    def __str__(self):
        return self.name
