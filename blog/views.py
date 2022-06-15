from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .models import Post
from recipes.models import Recipe, Ingredient

def home(request):
    context = {
        'blog_view_name': 'home',
        'posts': Post.objects.all(),
        'recipes': Recipe.objects.all(), #delete this
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
        print(context['ingredients'])
        
        return context

class PostCreateView(CreateView):
    model = Post
    
    # fields to be displayed
    fields = [
        'title',
        'author',
        'post_type',
    ]