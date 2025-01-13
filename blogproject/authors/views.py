from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignupForm

# Create your views here.

def signUp(request):
    if request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request,"Your account is created successfully")
        return redirect('home')
    else:
        messages.error(request, "Error")

        form=SignupForm()
    return render(request, "register.html",{'form':form})


def logIn(request):
    return render(request, "login.html")