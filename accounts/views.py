from django.shortcuts import render, redirect
from .forms import c_RegisterForm, p_RegisterForm
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.

def c_signup(request):
    if request.method == 'POST':
        form = c_RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('main')
    else:
        form = c_RegisterForm()
    return render(request, 'accounts/c_signup.html', {'form':form})

def p_signup(request):
    if request.method == 'POST':
        form = p_RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('main')
    else:
        form = p_RegisterForm()
    return render(request, 'accounts/p_signup.html', {'form':form})
            
            

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = auth.authenticate(request, username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')       

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main')
    return redirect('login')