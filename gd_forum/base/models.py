from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Thread(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    uploader = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey("Category", verbose_name=("Category"), null=True, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Comment(models.Model):
    text = models.TextField(max_length=700, blank=False, null=False)
    thread = models.ForeignKey("Thread", verbose_name=("Thread"), null=True, on_delete=models.CASCADE)
    uploader = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text[0:20])