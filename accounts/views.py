from django.shortcuts import render, redirect
from .forms import c_RegisterForm, p_RegisterForm, c_updateForm, p_updateForm, cuserForm
from django.contrib import auth
from django.contrib.auth.models import User
from .models import CUser, PUser
# Create your views here.

def c_signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"],
                email=request.POST["email"],
                first_name=request.POST["first_name"],
                )
            cuser = CUser(
                user=user,
                c_phone=request.POST["c_phone"],
                )
            cuser.save()
            auth.login(request,user)
            return redirect('main')
    return render(request, 'accounts/c_signup.html')

def p_signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"],
                email=request.POST["email"],
                first_name=request.POST["first_name"],
                )
            puser = PUser(
                user=user,
                p_phone=request.POST["p_phone"],
                )
            puser.save()
            auth.login(request,user)
            return redirect('main')
    return render(request, 'accounts/p_signup.html')
            
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


