<<<<<<< HEAD
=======
from models import UserModel
>>>>>>> 610eb4db31b286572f3fda85600ebd0c829fa794
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

    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=40)
