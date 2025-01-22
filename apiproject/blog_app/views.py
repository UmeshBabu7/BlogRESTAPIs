from django.shortcuts import render
from django.http import JsonResponse
from .models import Blog,Category
from .serializers import BlogSerializer,CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins, generics

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
    


# Concrete Views

class BlogCreateCon(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogListcon(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogRetrievecon(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'


class BlogDestroyCon(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogUpdateCon(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogretrieveUpdateCon(generics.RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogRetrieveDestroyCon(generics.RetrieveDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# class BlogListView(APIView):
#     def get(self, request):
#         all_blogs=Blog.objects.filter(is_public=True)
#         serializer=BlogSerializer(all_blogs,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    

# def post(self, request):
#         serializer=BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# generic views with mixins(list and post:create)
# class BlogListGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     # genericapiview
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

#     #mixins 
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# retrieve
# class BlogDetailGenericView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     lookup_field = 'slug'

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

    

# class BlogDetailView(APIView):
#     def get(self, request, pk):
#         blog=Blog.objects.get(id=id)
#         serializer=BlogSerializer(blog)
#         return Response(serializer.data,status=status.HTTP_200_OK)


# def put(self, request, pk):
#         blog=Blog.objects.get(id=id)
#         serializer=BlogSerializer(blog,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
# def delete(self, request, pk):
#         blog=Blog.objects.get(id=id)
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
    
    
    
    

