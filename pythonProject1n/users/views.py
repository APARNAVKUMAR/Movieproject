from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
# Create your views here.
@login_required(login_url='login')

def addUser(request):
    user= None
    error_message =None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        try:
            user=User.objects.create_user(username=username,password=password)
        except Exception as e:
            error_message = str(e)
    return render(request,'users/addUser.html',{'user':user,'error_message':error_message})

def LoginFunction(request):
    error_message=0
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('list')
        else:
            error_message= 'Invalid credentials'
    return render(request,'users/UserLogin.html',{'error_message':error_message})
@login_required(login_url='login')

def LogOut(request):
    logout(request)
    return redirect('login')