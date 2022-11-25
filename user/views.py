from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
# Create your views here.


def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Başarıyla giriş yaptınız')
            return redirect('index')
        else:
            messages.warning(request, 'Kullanıcı Adı veya şifre hatalı')
            return redirect('login')
      
    return render(request, "login.html")


def userRegister(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['psw']
        repassword = request.POST['psw-repeat']
        
        if password == repassword:
            if User.objects.filter(username = username).exists():
                messages.warning(request, 'Bu Kullanıcı Adı Zaten Kullanılıyor')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.warning(request, 'Bu Email Zaten Kullanılıyor')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, email=email, password=password)
                Profile.objects.create(
                   
                    user = user,
                    email = email,
                    
               )
                user.save()
                messages.success(request, 'Başarıyla Kayıt Oldunuz')
                return redirect('login')

    return render(request, "register.html")

def userLogout(request):
    logout(request)
    messages.success(request, 'Çıkış Yaptınız')
    return redirect('login')
    


