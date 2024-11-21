from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import UserSignupForm
from .models import User, UseContactEmail, UseContactNumber
def signup(request):
    # Get the total number of rows in the User table
    user_count = User.objects.count()

    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            # Extract cleaned data
            fname = form.cleaned_data['fname']
            mname = form.cleaned_data['mname']
            lname = form.cleaned_data['lname']
            utype = form.cleaned_data['utype']
            password = form.cleaned_data['password']
            email_addresses = form.cleaned_data['email_addresses']
            contact_number = form.cleaned_data['contact_number']

            # Save user data to the database
            user = User(
                fname=fname,
                mname=mname,
                lname=lname,
                utype=utype,
                password=make_password(password)  # Hash the password
            )
            user.save()

            # Save contact email and number
            UseContactEmail.objects.create(uid=user, email_addresses=email_addresses)
            UseContactNumber.objects.create(uid=user, contact_number=contact_number)

            # Redirect to the same page after successful sign-up
            return redirect('login')
    else:
        form = UserSignupForm()

    return render(request, 'signup.html', {'form': form, 'user_count': user_count+1})








from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from .models import User
from .forms import UserLoginForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            uid = form.cleaned_data['uid']
            password = form.cleaned_data['password']

            # Authenticate user
            try:
                user = User.objects.get(uid=uid)
                if check_password(password, user.password):
                    # Set session
                    request.session['uid'] = user.uid
                    request.session['fname'] = user.fname
                    messages.success(request, "Logged in successfully!")
                    return redirect('home')  # Redirect to a home page or dashboard
                else:
                    messages.error(request, "Invalid password!")
            except User.DoesNotExist:
                messages.error(request, "User ID does not exist!")
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})



def logout(request):
    request.session.flush()  # Clear all session data
    messages.success(request, "Logged out successfully!")
    return redirect('login')  # Redirect to login page


def home(request):
    if 'uid' not in request.session:
        return redirect('login')  # Redirect to login if not authenticated
    return render(request, 'home.html', {'fname': request.session.get('fname')})

