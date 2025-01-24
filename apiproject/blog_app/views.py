from django.shortcuts import render
from django.http import JsonResponse
from .models import Blog,Category,BlogComment
from .serializers import BlogSerializer,CategorySerializer,BlogCommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins, generics
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadonly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from .throttle import BlogListCreateViewThrottle
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

# category(list,create)
class CategoryListeCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # UserRate & AnonRate Throttle
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    
    # ScopeRateThrottle
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'blog-list'
    # Custom Throttle
    throttle_classes = [BlogListCreateViewThrottle]
    


    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True, context={'request': request})
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'No category found'}, status=status.HTTP_404_NOT_FOUND)
        

# category(retrieve,update,delete)
class CategorydetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    liikup_field = 'id' # slug
    permission_classes = [IsOwnerOrReadonly]
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'No blog Found'}, status=status.HTTP_404_NOT_FOUND)
    

# blog(list,create)
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BlogSerializer(queryset, many=True, context={'request': request})

        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Message':'No blogs found'}, status=status.HTTP_204_NO_CONTENT)
        
        
    def create(self, request, *args, **kwargs):
        serializer = BlogSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
     # throttle_classes = [BlogListCreateViewThrottle]
    
    # Filtering
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__category_name', 'is_public']
    

# blog(retrieve,update,delete)
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.filter(is_public = True)
    serializer_class = BlogSerializer
    liikup_field = 'id' # slug

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'No blog Found'}, status=status.HTTP_404_NOT_FOUND)
        

# blog comment(list,create)
class BlogCommentListCreateView(generics.ListCreateAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        blog_id = self.kwargs.get('blog_id')
        return BlogComment.objects.filter(blog_id=blog_id)
    
    def perform_create(self, serializer):
        blog_id = self.kwargs.get('blog_id')
        blog = get_object_or_404(Blog, id=blog_id)
        if BlogComment.objects.filter(blog=blog, author=self.request.user).exists():
            raise serializers.ValidationError({'Message': 'You have already added comment on this blog'})
        serializer.save(author=self.request.user, blog=blog)

class BlogCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    permission_classes = [IsOwnerOrReadonly]
    
    def get_object(self):
        comment_id = self.kwargs.get('comment_id')
        comment = get_object_or_404(BlogComment, id = comment_id)
        
        blog_id = self.kwargs.get("blog_id")
        if comment.blog.id != blog_id:
            raise serializers.ValidationError({"Message": "This comment is not related to the requested blog"}, status=status.HTTP_401_UNAUTHORIZED)
        return comment
    
    def delete(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user:
            raise serializers.ValidationError({"Message": "You are not authorized to perform this action"}, status=status.HTTP_401_UNAUTHORIZED)
        return super().delete(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        comment = self.get_object()
        
        if comment.author != request.user:
            raise serializers.ValidationError({"Message": "You are not authorized to perform this action"}, status=status.HTTP_401_UNAUTHORIZED)
        return super().put(request, *args, **kwargs)

# Concrete Views
# class BlogCreateCon(generics.CreateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


# class BlogListcon(generics.ListAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


# class BlogRetrievecon(generics.RetrieveAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     lookup_field = 'slug'


# class BlogDestroyCon(generics.DestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


# class BlogUpdateCon(generics.UpdateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


# class BlogretrieveUpdateCon(generics.RetrieveUpdateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


# class BlogRetrieveDestroyCon(generics.RetrieveDestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


# class BlogListCreateApiView(generics.ListCreateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


# class BlogRUDApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


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
        
    
    
    
    

