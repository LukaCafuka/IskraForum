from django.contrib import admin
from .models import Thread, Category, Comment
# Register your models here.

admin.site.register(Thread)
admin.site.register(Category)
admin.site.register(Comment)