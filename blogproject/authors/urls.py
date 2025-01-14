from django.urls import path
from .import views
from unicodedata import name

urlpatterns = [
    path('create-new-account/', views.signUp, name="register"),
    path('login/', views.logIn, name="login"),
    path('logout/', views.logOut, name="logout")
]

