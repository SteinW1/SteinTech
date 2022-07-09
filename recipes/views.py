from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .forms import RecipeForm, RecipeIngredientFormset, RecipeStepFormset
from .models import Recipe


def home(request):
    context = {
        'recipes': Recipe.objects.all(),
    }
    return render(request, 'recipes/home.html', context)


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = "recipe"


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
            return super(RecipeCreateView, self).form_valid(RecipeForm)
        else:
            for error in IngredientFormset.errors + StepFormset.errors:
                messages.error(self.request, f'{error}')
            return super(RecipeCreateView, self).form_invalid(RecipeForm)


class RecipeUpdateView(UpdateView, LoginRequiredMixin):
    model = Recipe
    form_class = RecipeForm
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super(RecipeUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['RecipeIngredientFormset'] = RecipeIngredientFormset(self.request.POST, instance=self.object) 
            context['RecipeStepFormset'] = RecipeStepFormset(self.request.POST, instance=self.object)

        else:
            context['RecipeIngredientFormset'] = RecipeIngredientFormset(instance=self.object) 
            context['RecipeStepFormset'] = RecipeStepFormset(instance=self.object)
        return context

    def form_valid(self, RecipeForm):
        context = self.get_context_data(form=RecipeForm)
        RecipeIngredientFormset = context['RecipeIngredientFormset']
        RecipeStepForm = context['RecipeStepFormset']
        if RecipeIngredientFormset.is_valid() and RecipeStepForm.is_valid():
            response = super().form_valid(RecipeForm)
            RecipeIngredientFormset.instance = self.object
            RecipeIngredientFormset.save()
            RecipeStepForm.instance = self.object
            RecipeStepForm.save()
            return response
        else:
            return super().form_invalid(RecipeForm)


class RecipeDeleteView(DeleteView, LoginRequiredMixin):
    model = Recipe
    success_url = reverse_lazy('recipe-list')
