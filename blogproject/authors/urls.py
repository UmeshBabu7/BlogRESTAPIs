from django.urls import path
from .import views
from unicodedata import name

urlpatterns = [
    path('create-new-account/', views.signUp, name="register"),
    path('login/', views.logIn, name="login"),
    path('logout/', views.logOut, name="logout"),
    path('change_password', views.PasswordChangeView.as_view(template_name = "password_change.html"), name="change-password"),
    path('password_success', views.password_success, name="password_success"),
    path('user-profile/<str:user_name>/', views.profile, name="profile"),
    path('edit_profile/', views.UpdateUserView.as_view(), name="edit_user"),
]

