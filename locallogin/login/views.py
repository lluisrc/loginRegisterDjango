from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrrrect')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account Create for ' + user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'register.html', context)


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')