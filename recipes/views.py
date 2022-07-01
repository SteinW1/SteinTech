from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Recipe, Ingredient

def home(request):
    context = {
        'recipes': Recipe.objects.all(),
    }
    return render(request, 'recipes/home.html', context)

class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = "recipe"

    def get_context_data(self, *args, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(*args, **kwargs)
        
        #add a QuerySet of all recipes
        context['ingredients'] = Ingredient.objects.all()
        
        return context

class RecipeListView(ListView):
    model = Recipe
    paginate_by = 10

class RecipeCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Recipe

    # fields to be displayed in the form
    fields = ['title',
        'source',
        'difficulty',
        'servings',
        'prep_time',
        'cook_time',
        'note',
        ]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        '''This method is called when valid form data has been POSTed. '''
        print('form is valid')
        print(form.cleaned_data)
        form.instance.slug = slugify(form.cleaned_data['title'])
        form.instance.author = self.request.user
        
        return super().form_valid(form)
        
    def form_invalid(self, form):
        print('form is invalid')
        response = super().form_invalid(form)
        return response

class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = [
        'title',
        'source',
        'difficulty',
        'servings',
        'prep_time',
        'cook_time',
        'note',
    ]
    template_name_suffix = '_update_form'
    
    def form_valid(self, form):
        '''This method is called when valid form data has been POSTed. '''
        print('form is valid')
        return super().form_valid(form)

class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipe-list')
