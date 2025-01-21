from django.shortcuts import render
from django.http import JsonResponse
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def blog_list(request):

    if request.method == "GET":
        all_blogs=Blog.objects.filter(is_public=True)
        serializer=BlogSerializer(all_blogs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    if request.method =="POST":
        serializer=BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    

@api_view(['GET','PUT','DELETE'])
def blog_detail(request,id):

    if request.method =='GET':
        blog=Blog.objects.get(id=id)
        serializer=BlogSerializer(blog)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method =='PUT':
        blog=Blog.objects.get(id=id)
        serializer=BlogSerializer(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    if request.method =='DELETE':
        blog=Blog.objects.get(id=id)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    
    
    
    

