from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.RecipeListView.as_view(), name='recipe-list'),
    path('recipes/new/', views.RecipeCreateView.as_view(), name='recipe-create'),
    path('recipes/<slug:slug>', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipes/<slug:slug>/edit/', views.RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipes/<slug:slug>/delete/', views.RecipeDeleteView.as_view(), name='recipe-delete'),
]
