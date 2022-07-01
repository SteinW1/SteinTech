from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('profile/<int:pk>/', views.UserDetailView.as_view(), name='profile-detail'),
    path('user/login/', views.UserLoginView.as_view(), name='user-login'),
    path('user/logout/', views.UserLogoutView, name='user-logout'),
    path('user/signup/', views.UserCreateView.as_view(), name='user-register'),
    path('welcome/', TemplateView.as_view(template_name="profiles/new_user_welcome.html"), name='new-user-welcome'),
]
