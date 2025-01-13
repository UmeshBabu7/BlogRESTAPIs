from django.urls import path
from .import views

urlpatterns = [
    path('',views.blog_home,name="home"),
    path('blog_detail/',views.blog_detail,name='blog_detail'),
    path('user_profile/',views.profile,name='user_profile'),
    path('contact_us/', views.contactUs, name="contact_us"),
    path('blog_detail/<str:slug>', views.blog_detail, name="blog_detail"),
    
]
