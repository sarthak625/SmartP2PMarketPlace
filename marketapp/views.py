from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
from forms import SignUpForm, LoginForm
from models import UserModel, SessionToken
from django.contrib.auth.hashers import make_password, check_password

# View to the landing page
def landing(request):
    return render(request,'landing.html')


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

    dict = {}
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        # username = form.cleaned_data.get('username')
        # password = form.cleaned_data.get('password')
        # print username
        # print password
        print form

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print username
            print password
            user     = UserModel.objects.filter(username=username).first()

            if user:
                if check_password(password, user.password):
                    # User is Valid
                    print 'Valid'
                    token   =  SessionToken(user=user)
                    token.create_token()
                    token.save()
                    response.redirect('/success/')
                    response.set_cookie(key='session_token', value=token.session_token)
                    return response


                else:
                    # User is not valid
                    print 'Invalid User'
                    dict['message'] = 'Incorrect Password !! Please try again !'
            else:
                # User does not exist'
                print 'User doesnt exist'
        else:
            # Form is not Valid
            print 'Invalid Form'
    else:
        form = LoginForm()

    dict['form'] = form
    return render(request,'login.html', dict)


# Check if the current session is valid 
def check_validation(request):
    if request.COOKIES.get('session_token'):
        session = SessionToken.objects.filter(session_token=request.COOKIES.get('session_token')).first()
        if session:
            return session.user
    else:
        return None
