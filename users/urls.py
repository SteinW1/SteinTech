from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('user/login/', views.UserLoginView.as_view(), name='user-login'),
    path('user/logout/', views.UserLogoutView, name='user-logout'),
    path('welcome/', TemplateView.as_view(template_name="new_user_welcome.html"), name='new-user-welcome'),
]
