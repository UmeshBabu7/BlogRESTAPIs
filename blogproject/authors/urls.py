from django.urls import path
from .import views

urlpatterns = [
    path('create-new-account/', views.signUp, name="register"),
    path('login/', views.logIn, name="login"),
]

