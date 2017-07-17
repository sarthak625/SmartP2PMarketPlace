from django.forms import ModelForm
from models import UserModel

class SignUpForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ['name','username','email','password']
