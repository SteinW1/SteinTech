from django.urls import path
from .views import PostCreateView
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('newpost/', views.PostCreateView.as_view(), name='post-create')
]
