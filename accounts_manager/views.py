from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from accounts_manager.forms import SignupForm, LoginForm, ProfileForm
from accounts_manager.models import MainUser

def index(response):
    return render(response, 'index.html')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = MainUser.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"],
                )
            return redirect('profile/')
    else:
        form = SignupForm
    dataums = {'form': form}
    return render(request, 'signup.html', dataums)


def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/profile')
                else:
                    return redirect('/login_page')
    else:
        form = LoginForm
    dataum = {'form': form}
    return render(request, 'login.html', dataum)

def profile_builder(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = MainUser.objects.create_user(
                form.cleaned_data["first_name"],
                )
            return redirect('index/')
    else:
        form = ProfileForm
    dataums = {'form': form}
    return render(request, 'profile_builder.html', dataums)