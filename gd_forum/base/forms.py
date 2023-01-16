from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Thread

# Create your forms here.

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = '__all__'
        exclude = ['created', 'uploader']
    def __init__(self, *args, **kwargs):
        super(ThreadForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['id'] = 'floatingInput'
        self.fields['title'].widget.attrs['placeholder'] = 'title'
        self.fields['description'].widget.attrs['class'] = 'form-control textarea'
        self.fields['description'].widget.attrs['placeholder'] = 'description'
        self.fields['description'].widget.attrs['cols'] = '8'
        self.fields['description'].widget.attrs['id'] = 'floatingInput'
        self.fields['category'].widget.attrs['class'] = 'form-select'
        self.fields['category'].widget.attrs['id'] = 'floatingInput'
        
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e-mail'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['username'].widget.attrs['id'] = 'floatingInput'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password1'].widget.attrs['id'] = 'floatingInput'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'password confirmation'
        self.fields['password2'].widget.attrs['id'] = 'floatingInput'

class ChangeUsernameForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', )

    def __init__(self, *args, **kwargs):
        super(ChangeUsernameForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['username'].widget.attrs['id'] = 'floatingInput'

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].widget.attrs['placeholder'] = 'old password'
        self.fields['old_password'].widget.attrs['id'] = 'floatingInput'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'new password'
        self.fields['new_password1'].widget.attrs['id'] = 'floatingInput'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'new password'
        self.fields['new_password2'].widget.attrs['id'] = 'floatingInput'