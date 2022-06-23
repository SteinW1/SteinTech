from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('<str:user>', views.RecipeDetailView.as_view(), name='recipe-detail'),
]