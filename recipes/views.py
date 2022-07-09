from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .forms import RecipeForm, RecipeIngredientFormset, RecipeStepFormset
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
        context['ingredients'] = Ingredient.objects.all()
        return context


class RecipeListView(ListView):
    model = Recipe
    paginate_by = 10


class RecipeCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Recipe
    form_class = RecipeForm
    
    def get_context_data(self, **kwargs):
        context = super(RecipeCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['RecipeIngredientFormset'] = RecipeIngredientFormset(self.request.POST) 
            context['RecipeStepFormset'] = RecipeStepFormset(self.request.POST)
        else:
            context['RecipeIngredientFormset'] = RecipeIngredientFormset()
            context['RecipeStepFormset'] = RecipeStepFormset()
        return context

    def form_valid(self, RecipeForm):
        context = self.get_context_data()
        IngredientFormset = context['RecipeIngredientFormset']
        StepFormset = context['RecipeStepFormset']
        if IngredientFormset.is_valid() and StepFormset.is_valid():
            RecipeForm.instance.author = self.request.user
            self.object = RecipeForm.save()
            IngredientFormset.instance = self.object
            IngredientFormset.save()
            StepFormset.instance = self.object
            StepFormset.save()
        else:
            for error in IngredientFormset.errors + StepFormset.errors:
                messages.error(self.request, f'{error}')
        return super(RecipeCreateView, self).form_invalid(RecipeForm)


class RecipeUpdateView(UpdateView, LoginRequiredMixin):
    model = Recipe
    form_class = RecipeForm
    template_name_suffix = '_update_form'


class RecipeDeleteView(DeleteView, LoginRequiredMixin):
    model = Recipe
    success_url = reverse_lazy('recipe-list')
