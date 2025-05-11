from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from student import settings
from .forms import SignupForm, MicrofileForm
from .models import Microfile

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            send_mail(
                "Registration Successful",
                "You have successfully registered!",
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')
@login_required
def dashboard(request):
    microfiles = Microfile.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'microfiles': microfiles, 'user': request.user})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    microfiles = Microfile.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'microfiles': microfiles})

@login_required
def upload_microfile(request):
    if request.method == "POST":
        form = MicrofileForm(request.POST, request.FILES)
        if form.is_valid():
            microfile = form.save(commit=False)
            microfile.user = request.user
            microfile.save()
            return redirect('dashboard')
    else:
        form = MicrofileForm()
    return render(request, 'upload_microfile.html', {'form': form})
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
