from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Recipe, Ingredient
from .forms import RecipeForm

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
        context['ingredients'] = Ingredient.objects.all()
        return context


class RecipeListView(ListView):
    model = Recipe
    paginate_by = 10


class RecipeCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Recipe
    form_class = RecipeForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        '''This method is called when valid form data has been POSTed. '''
        form.instance.author = self.request.user
        return super().form_valid(form)
        
    def form_invalid(self, form):
        print('form is invalid')
        response = super().form_invalid(form)
        return response


class RecipeUpdateView(UpdateView, LoginRequiredMixin):
    model = Recipe
    form_class = RecipeForm
    template_name_suffix = '_update_form'


class RecipeDeleteView(DeleteView, LoginRequiredMixin):
    model = Recipe
    success_url = reverse_lazy('recipe-list')
