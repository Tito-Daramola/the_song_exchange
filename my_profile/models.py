from django.db import models
from django.contrib.auth.models import User
from blog.models import Post


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_song = models.CharField(max_length=100)
    favorite_artist = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

    def get_user_posts(self):
        return Post.objects.filter(author=self.user)
