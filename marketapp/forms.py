from django.forms import ModelForm
from models import UserModel
from django import forms

class SignUpForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ['name','username','email','password']

class LoginForm(forms.Form):
    class Meta:
        model = UserModel
        fields = ['username','password']
