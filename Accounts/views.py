from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib import messages , auth
from django.contrib.auth.models import User
# Create your views here.

def Signup(request):
    if request.method == 'POST' :
        Username = request.POST.get('Username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_second = request.POST.get('password2')

        if password == password_second:
            if User.objects.filter(username = Username).exists():
                messages.error(request,'User already exist with the enrollment Number')
                return  redirect('registration')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request,'email already in use')
                else:
                    user = User.objects.create_user(username = Username, password=password,
                    email = email, first_name = first_name , last_name = last_name)
                    User.save();
                    auth.login(request,user)
                    messages.success(request,'You are now logged in')
                    return redirect('home')
      
        else:
            messages.error(request,'Passwords do not match')
            return redirect('signup')
    else:
        return render(request,'partial/newsign.html')



def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email = email,password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Email Or Password')
            return redirect('login')
            
    else:
        return render(request,'partial/login.html')
