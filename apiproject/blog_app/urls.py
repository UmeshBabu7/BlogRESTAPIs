from django.urls import path

from .import views

urlpatterns = [
    # path('class_blog_list/', views.BlogListView.as_view(), name="all_blog_list"),
    path('class_blog_detail/<int:pk>/', views.BlogDetailView.as_view(), name="blog_detail"),

    # Category URLS
    path("category_list/", views.CategoryListView.as_view(), name="category_list"),
    path("category_detail/<int:pk>/", views.CategoryDetailView.as_view(), name="category_detail"),

    
    # Generic view with mixins
    path("blog_list_generic_view/", views.BlogListGenericView.as_view(), name="blog_list_generic_view")
    
]
