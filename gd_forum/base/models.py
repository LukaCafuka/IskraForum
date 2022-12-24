from django.db import models

# Create your models here.

class Thread(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    #uploader =
    #category =
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)