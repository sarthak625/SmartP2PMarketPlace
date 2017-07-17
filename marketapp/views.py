from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
from forms import SignUpForm

def home(request):
    return render(request,'home.html')

def signup(request):
    today = datetime.now()
    if request.method == 'POST':
        signup_form = SignUpForm()
        return render(request,'signup.html',{'signup_form': signup_form}) 
