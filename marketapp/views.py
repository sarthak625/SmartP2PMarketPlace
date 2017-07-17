from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.hashers import make_password
from datetime import datetime
from forms import SignUpForm, LoginForm
from models import UserModel
from django.contrib.auth.hashers import make_password, check_password

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


# View for the login page

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user     = UserModel.objects.filter(username=username).first()

            if user:
                if check_password(password, user.password):
                    print 'User is Valid'
                else:
                    print 'User is not valid'
            else:
                print 'User does not exist'
        else:
            print 'Form is not Valid'
    else:
        login_form = LoginForm()

    return render(request,'login.html',{'form': login_form})
