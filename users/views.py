from django.http import HttpRequest,HttpResponse
from django.shortcuts import render,redirect
from users.forms import LoginForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.
def sign_up(request:HttpRequest):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User Created Successfully")
            return redirect('login')
    context={'form':form}
    return render(request,'users/signup.html',context)

def login_user(request:HttpRequest):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('post_home')
    context={'form':form}
    return render(request,'users/login.html',context)

def logout_user(request:HttpRequest):
    logout(request)
    return redirect('login')