from django.shortcuts import render
from django.http import JsonResponse
from .models import Blog

# Create your views here.

def blog_list(request):
    blogs=Blog.objects.all()

    context={
        "Blogs":list(blogs.values())
    }
    
    return JsonResponse(context)


def blog_detail(request,pk):
    blogs=Blog.objects.get(pk=pk)

    context={
        "name":blogs.name,
        "description":blogs.description,
        "slug":blogs.slug
    }

    return JsonResponse(context)

