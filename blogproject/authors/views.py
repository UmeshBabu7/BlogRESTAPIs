from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from .forms import SignupForm,LoginUserForm
from django.contrib.auth import authenticate, login,logout
from main.models import Blog
from django.urls import reverse_lazy
from .forms import SignupForm, LoginUserForm, PasswordChangingForm,EditUserProfileForm
from django.contrib.auth.views import PasswordChangeView
from django.views import generic

# Create your views here.

def signUp(request):
    if request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request,"Your account is created successfully")
        new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            
        login(request, new_user)
        return redirect('home')
    else:
        messages.error(request, "Error")

        form=SignupForm()
    return render(request, "register.html",{'form':form})


def logIn(request):
    if request.method == "POST":
        form = LoginUserForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username = username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f"You are logged in as {username}")
                return redirect('home')
            else:
                messages.error(request, "Error")
        else:
            messages.error(request, "Username or password incorrect")
    form = LoginUserForm()
    return render(request, "login.html", {"login_form": form})


def logOut(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')


def profile(request, user_name):
    user_related_data = Blog.objects.filter(author__username = user_name)
    context = {
        "user_related_data": user_related_data
    }
    return render(request, "profile.html", context)


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')
    
def password_success(request):
    return render(request, "password_change_success.html")


class UpdateUserView(generic.UpdateView):
    form_class = EditUserProfileForm
    template_name = "edit_user_profile.html"
    success_url = reverse_lazy('home')
    
    def get_object(slef):
        return slef.request.user