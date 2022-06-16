from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from recipes.models import Recipe, Ingredient

def home(request):
    context = {
        'blog_view_name': 'home',
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)

class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        
        #add a QuerySet of all recipes
        context['recipes'] = Recipe.objects.all()
        context['ingredients'] = Ingredient.objects.all()
        
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    
    # fields to be displayed in the form
    fields = [
        'title',
        'post_type',
    ]
    
    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author = self.request.user
        return super().form_valid(form)

'''
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
'''