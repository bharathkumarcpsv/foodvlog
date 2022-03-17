from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        print(firstname)
        lastname = request.POST['lastname']
        username = request.POST['Username']
        password1 = request.POST['psw']
        password2 = request.POST['psw-repeat']
        email = request.POST['email']
        if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"username already taken")
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "email already taken")
                else:
                    user = User.objects.create_user(username=username,password=password2,email=email,)
                    user.save();
                    print("user created")
                    messages.success(request,"user created")
                    return redirect('/')
        else:
            messages.success(request,"Password not matching")
    return render(request, 'register.html')
def ulogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        print(username)
        print(password)
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print("invalid")
            messages.info(request,"Invalid username or password ")
            return redirect('login')
    else:
        return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
