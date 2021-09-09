from django.shortcuts import render, redirect
from django.contrib import messages
from . form import UserRegisterForm
# Create your views here.

def register(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your have been registered. You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html', {'form':form})

def profile(request):
    return render(request,'users/profile.html')
