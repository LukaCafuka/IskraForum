from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(forms.Form):
    username = forms.CharField(label = "Username", max_length=25, required=True)
