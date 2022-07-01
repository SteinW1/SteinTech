from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('profile/login/', views.UserLoginView.as_view(), name='profile-login'),
    path('profile/logout/', views.UserLogoutView, name='profile-logout'),
    path('profile/<slug:slug>/update/', views.UserUpdateView.as_view(), name='profile-update'),
    path('profile/<slug:slug>/', views.UserDetailView.as_view(), name='profile-detail'),
    path('signup/', views.UserCreateView.as_view(), name='user-register'),
    path('welcome/', TemplateView.as_view(template_name="profiles/new_user_welcome.html"), name='new-user-welcome'),
]
