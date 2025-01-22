from django.urls import path

from .import views

urlpatterns = [
    path('class_blog_list/', views.BlogListView.as_view(), name="all_blog_list"),
    path('class_blog_detail/<int:pk>/', views.BlogDetailView.as_view(), name="blog_detail")
    
]
