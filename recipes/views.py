from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import RecipeForm
from .models import Recipe, Ingredient
from blog.models import Post

# Create your views here.
