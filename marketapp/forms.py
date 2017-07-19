from django import forms
from models import UserModel

class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['name','username','email','password']

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = UserModel
#         fields = ['username','password']

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contrasena',widget = forms.PasswordInput)
