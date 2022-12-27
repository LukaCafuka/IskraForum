from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Thread

# Create your forms here.

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = '__all__'
        


class NewUserForm(forms.Form):
    username = forms.CharField(label = "Username", max_length=25, required=True)
