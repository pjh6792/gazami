from django.shortcuts import render, redirect
from .forms import c_RegisterForm, p_RegisterForm, c_updateForm, p_updateForm
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

def c_update(request): #예매자 회원 회원정보 수정
    if request.method == 'POST':
        form = c_updateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
    else:
        form = c_updateForm(instance=request.user)
    return render(request, 'accounts/c_update.html',{'form':form})

def p_update(request): #공연자 회원 회원정보 수정
    if request.method == 'POST':
        form = p_updateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
    else:
        form = p_updateForm(instance=request.user)
    return render(request, 'accounts/p_update.html',{'form':form})


