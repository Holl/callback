from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.template import context
from registration.models import User
from accounts_manager.forms import SignupForm, LoginForm, ProfileForm, ProductionProfileForm
from accounts_manager.models import MainUser, ActorProfile, ProductionProfile
from auditioneer.models import Audition


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
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            login_user = authenticate(username=username, password=password)
            login(request, login_user)
            return redirect('choice/')
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
                    return redirect('/')
                else:
                    return redirect('/login_page')
    else:
        form = LoginForm
    dataum = {'form': form}
    return render(request, 'login.html', dataum)


def profile_builder(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                submission = form.save(commit=False)
                usr = request.user
                submission.user = usr
                submission.headshot = request.FILES['headshot']
                submission.highlight_reel = request.FILES['highlight_reel']
                submission.save()
                return redirect('/')

        except:
            if form.is_valid():
                profiler = ActorProfile.objects.get(user=request.user)
                form = ProfileForm(request.POST, request.FILES, instance=profiler)
                submission = form.save(commit=False)
                submission.headshot = request.FILES['headshot']
                submission.save()
                return redirect('/')
    try:
        profiler = ActorProfile.objects.get(user=request.user)
        form = ProfileForm(instance=profiler)
    except:
        form = ProfileForm

    dataums = {'form': form}
    return render(request, 'profile_builder.html', dataums)


def production_profile_builder(request):
    if request.method == "POST":
        profiler = ProductionProfileForm.objects.get(user=request.user)
        form = ProductionProfileForm(request.POST, instance=profiler)
        try:
            if form.is_valid():
                submission = form.save(commit=False)
                usr = request.user
                submission.user = usr
                submission.save()
                return redirect('/')
        except:
            if form.is_valid():
                submission = form.save(commit=False)
                submission.save()
                return redirect('/')
    try:
        profiler = ProductionProfile.objects.get(user=request.user)
        form = ProductionProfileForm(instance=profiler)
    except:
        form = ProductionProfileForm
    dataums = {'form': form}
    return render(request, 'production_profile_builder.html', dataums)


def choice(response):
    return render(response, 'choice.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def about(request):
    return render(request, 'about.html')


def news(request):
    return render(request, 'news.html')


def audition_signup(request, id):
    profiler = ActorProfile.objects.get(user=request.user)
    auditioner = Audition.objects.get(id=id)

    auditioner.actor_user.add(profiler)

    return render(request, 'AuditionSignup.html')