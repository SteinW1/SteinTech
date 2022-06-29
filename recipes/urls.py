from django.urls import path
from .views import RecipeCreateView, RecipeDetailView, RecipeListView, RecipeUpdateView, RecipeDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.RecipeListView.as_view(), name='recipe-list'),
    path('recipes/<slug:slug>', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipes/<int:pk>/edit/', views.RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipes/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe-delete'),
    path('new/', views.RecipeCreateView.as_view(), name='recipe-create'),
]
