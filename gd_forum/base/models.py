from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Thread(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    #uploader =
    #category =
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)