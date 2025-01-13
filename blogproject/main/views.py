from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog_home(request):
    return render(request,'blog_home.html')


def blog_detail(request):
    return render(request,'blog_detail.html')


def profile(request):
    return render(request,'profile.html')



