from django import forms
from django.contrib.auth.models import User
from .models import Microfile

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class MicrofileForm(forms.ModelForm):
    class Meta:
        model = Microfile
        fields = ['file']
