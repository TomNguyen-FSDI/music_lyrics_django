from django.db import models
from django.urls import reverse

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.TextField()
    lyrics = models.TextField()
    user = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("music_detail", args=[str(self.id)])