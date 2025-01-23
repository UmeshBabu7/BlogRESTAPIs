from django.urls import path

from .import views

urlpatterns = [
    # path('class_blog_list/', views.BlogListView.as_view(), name="all_blog_list"),
    # path('class_blog_detail/<int:pk>/', views.BlogDetailView.as_view(), name="blog_detail"),

    # Category URLS
    path("category_list/", views.CategoryListeCreateView.as_view(), name="category_list"),
    path("category_detail/<int:pk>/", views.CategorydetailView.as_view(), name="category_detail"),

    
    # Generic view with mixins
    # path("blog_list_generic_view/", views.BlogListGenericView.as_view(), name="blog_list_generic_view"),


    # path("blog_detail_generic_view/<int:pk>/", views.BlogDetailGenericView.as_view(), name="blog_detail_generic_view"),
    # path("blog_detail_generic_view/<str:slug>/", views.BlogDetailGenericView.as_view(), name="blog_detail_generic_view"),


    # Concrete  urls
    # path("blog_create_createapiview/", views.BlogCreateCon.as_view(), name="blog_create_createapiview"),
    # path("blog_list_createapiview/", views.BlogListcon.as_view(), name="blog_list_createapiview"),
    # path("blog_retrieve_retrievepiview/<str:slug>/", views.BlogRetrievecon.as_view(), name="blog_retrieve_retrieveapiview"),
    # path("blog_destroypiview/<int:pk>/", views.BlogDestroyCon.as_view(), name="blog_destroy_destroyapiview"),
    # path("blog_updateapiview/<int:pk>/", views.BlogUpdateCon.as_view(), name="blog_update_updateapiview"),
    # path("blog_retrieveUpdateapiview/<int:pk>/", views.BlogretrieveUpdateCon.as_view(), name="blog_retrieveUpdate_retrieveUpdateapiview"),
    # path("blog_retrieveDestroyapiview/<int:pk>/", views.BlogRetrieveDestroyCon.as_view(), name="blog_retrieveDestroy_retrieveDestroyapiview"),
    # path("blog_listcreate_listcreateapiview/", views.BlogListCreateApiView.as_view(), name="blog_listcreate_listcreateapiview"),
    # path("blog_rud/<int:pk>/", views.BlogRUDApiView.as_view(), name="blog_rud"),


# create blog lists,create and retrieve,update and delete view created
    path("blog_list/", views.BlogListCreateView.as_view(), name="blog_list"),
    path("blog_detail/<int:pk>/", views.BlogDetailView.as_view(), name="blog_list"),

# blogs comment
    path("blog_comment_list/blog/<int:blog_id>/", views.BlogCommentListCreateView.as_view(), name="blog_comment_list"),
    path("blog_comment_detail/blog/<int:blog_id>/comment/<int:comment_id>/", views.BlogCommentDetailView.as_view(), name="blog_comment_detail"),

    
    
]
