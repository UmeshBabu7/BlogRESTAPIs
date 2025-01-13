from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog,BlogComment,Contact
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def blog_home(request):
    all_blogs=Blog.objects.all()

    context={
        'blogs':all_blogs
    }

    return render(request,'blog_home.html',context)


def blog_detail(request,slug):
    blog=Blog.objects.get(slug=slug)
    all_blogs = Blog.objects.all().order_by('-post_date')[:10]

    context={
        'blog':blog,
        'all_blogs': all_blogs
    }

    return render(request,'blog_detail.html',context)


def profile(request):
    return render(request,'profile.html')


def contactUs(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "your form is submitted successfully")
    else:
        form = ContactForm()
    return render(request, "contact_us.html", {"form": form})
    



