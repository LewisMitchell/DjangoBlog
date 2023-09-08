from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField("Posted on")