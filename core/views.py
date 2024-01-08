from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import SignUpForm

from django.http import HttpResponse
# Create your views here.


from django.contrib.auth import authenticate, login,logout


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticating the user
        user = authenticate(request, username=username, password=password)
        # Checking if authentication is successful
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')

def index(request):
    return render(request, 'core/index.html')

def signup(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')

    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form' : form})

