from django.db import models
from django.contrib.auth.models import User
from blog.models import Post

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    favourite_song = models.CharField(max_length=100)
    favourite_artist = models.CharField(max_length=100)
    favourite_song_url = models.URLField(max_length=200)
    posts = models.ManyToManyField(Post, related_name = 'profiles')

    def __str__(self):
        return self.user.username