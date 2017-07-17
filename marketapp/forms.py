from django import forms
from models import UserModel

class SignUpForm(forms.ModelForm):
    class Meta:
        models = UserModel
        fields = ['name','username','email','password']
