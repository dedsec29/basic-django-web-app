from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
def home(request):
    return render(request,'home.html')

# User Register
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = RegisterForm()
    return render(request,'registration/register.html',{'form':form})
