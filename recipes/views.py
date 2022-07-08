from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
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
    
    def get(self, request):
        super(RecipeCreateView, self).get(request)
        self.context = self.get_context_data()
        self.context['RecipeIngredientFormset'] = RecipeIngredientFormset()
        self.context['RecipeStepFormset'] = RecipeStepFormset()
        return render(request, 'recipes/recipe_form.html' , self.context)

    def post(self, request):
        RecipeForm = self.get_form()
        if RecipeForm.is_valid():
            return self.form_valid(RecipeForm)
        else:
            self.object = None
            return self.form_invalid(RecipeForm)

    def form_valid(self, RecipeForm):
        RecipeForm.instance.author = self.request.user
        self.object = RecipeForm.save(commit=False)
        IngredientFormset = RecipeIngredientFormset(self.request.POST, instance=self.object)
        StepFormset = RecipeStepFormset(self.request.POST, instance=self.object)
        if IngredientFormset.is_valid() and StepFormset.is_valid():
            RecipeForm.save()
            IngredientFormset.save()
            StepFormset.save()
            return redirect(self.object.get_absolute_url())
        else:
            for error in IngredientFormset.errors:
                messages.error(self.request, f'{error}')
            for error in StepFormset.errors:
                messages.error(self.request, f'{error}')
            return self.form_invalid(RecipeForm)

    def form_invalid(self, RecipeForm):
        self.context = self.get_context_data()
        self.context['RecipeForm'] = RecipeForm
        self.context['RecipeIngredientFormset'] = RecipeIngredientFormset()
        self.context['RecipeStepFormset'] = RecipeStepFormset()
        for error in RecipeForm.errors:
            messages.error(self.request, f'{error}')
        return render(self.request, 'recipes/recipe_form.html', self.context)


class RecipeUpdateView(UpdateView, LoginRequiredMixin):
    model = Recipe
    form_class = RecipeForm
    template_name_suffix = '_update_form'


class RecipeDeleteView(DeleteView, LoginRequiredMixin):
    model = Recipe
    success_url = reverse_lazy('recipe-list')
