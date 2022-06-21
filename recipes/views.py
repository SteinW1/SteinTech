from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import RecipeForm
from .models import Recipe, Ingredient
from blog.models import Post

class RecipeCreateView(CreateView):
    model = Recipe

    # fields to be displayed in the form
    fields = ['title', 
        'difficulty',
        'servings',
        'prep_time',
        'cook_time',
        'submit',]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        '''This method is called when valid form data has been POSTed. '''
        print('form is valid')
        print(form.data)
        print(form.cleaned_data)
        return super().form_valid(form)
        
    def form_invalid(self, form):
        print('form is invalid')
        '''
        print(form.data)
        print(form.cleaned_data)
        '''
        response = super().form_invalid(form)
        return response
