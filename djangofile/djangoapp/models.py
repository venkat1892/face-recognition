from django.db import models

# Create your models here.
class Post(models.Model):
    username = models.TextField(max_length=100)
    password = models.TextField(max_length=100)
    def __str__(self):
        return self.username

