from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,BlogComment

# Create your views here.

def blog_home(request):
    all_blogs=Blog.objects.all()

    context={
        'blogs':all_blogs
    }

    return render(request,'blog_home.html',context)


def blog_detail(request):
    return render(request,'blog_detail.html')


def profile(request):
    return render(request,'profile.html')


def contactUs(request):
    return render(request, "contact_us.html")



