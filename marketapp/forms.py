from models import UserModel
from django import forms

class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['name','username','email','password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=40)
