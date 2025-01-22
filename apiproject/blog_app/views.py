from django.shortcuts import render
from django.http import JsonResponse
from .models import Blog,Category
from .serializers import BlogSerializer,CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class CategoryListView(APIView):
    def get(self, request):
        all_category = Category.objects.all()
        serializers = CategorySerializer(all_category, many=True, context={'request': request})
        return Response(serializers.data)
    

class CategoryDetailView(APIView):
    def get(self, request, pk):
        single_category = Category.objects.get(pk=pk)
        serializers = CategorySerializer(single_category, context={'request': request})
        return Response(serializers.data)


class BlogListView(APIView):
    def get(self, request):
        all_blogs=Blog.objects.filter(is_public=True)
        serializer=BlogSerializer(all_blogs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

def post(self, request):
        serializer=BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    

class BlogDetailView(APIView):
    def get(self, request, pk):
        blog=Blog.objects.get(id=id)
        serializer=BlogSerializer(blog)
        return Response(serializer.data,status=status.HTTP_200_OK)


def put(self, request, pk):
        blog=Blog.objects.get(id=id)
        serializer=BlogSerializer(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



def delete(self, request, pk):
        blog=Blog.objects.get(id=id)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    
    
    
    

