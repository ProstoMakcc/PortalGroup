from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages 

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            
            return redirect('homepage') # Треба створити юрл(не знаю в якому файлі його розмістити)
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'auth_system/login.html')

def logout_view(request):
    logout(request)

    return redirect('homepage') # Треба створити юрл(не знаю в якому файлі його розмістити)
