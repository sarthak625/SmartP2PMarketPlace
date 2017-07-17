from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.hashers import make_password
from datetime import datetime
from forms import SignUpForm
from models import UserModel

# View to the home page

def signup(request):
    today = datetime.now()
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)

        if signup_form.is_valid():
            # Extract the details from the form
            username = signup_form.cleaned_data['username']
            name = signup_form.cleaned_data['name']
            email = signup_form.cleaned_data['email']
            password = signup_form.cleaned_data['password']

            #Saving data to the database
            user = UserModel(name=name, password=make_password(password), email=email, username=username)
            user.save()

            #Show the success page
            return render(request, 'success.html')

    else:
        signup_form = SignUpForm()

    # Render the home page
    return render(request,'home.html',{'signup_form': signup_form})
