from django.db import models
from django.contrib.auth.models import User
from users.models import CustomUser

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title