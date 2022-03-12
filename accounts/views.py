from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect

from accounts.models import *
def register(request):
    if request.method == "POST":
        firstname=request.POST['firstname']
        print(firstname)
        lastname = request.POST['lastname']
        username = request.POST['Username']
        password1 = request.POST['psw']
        password2 = request.POST['psw-repeat']
        email = request.POST['email']
        if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.success(request, "username taken")
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.success(request, "email already taken")
                else:
                    user=User.objects.create(firstname=firstname,lastname=lastname,username=username,password=password2,email=email)
                    user.save();
                    messages.success(request,"user created")
                    return redirect('/')
        else:
            messages.success(request,"Password does not match")

    return render(request, 'register.html')
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print("invalid")
            messages.success(request,"invalid details")
            return redirect('login')
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
