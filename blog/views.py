from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Article
from .forms import PostForm, ArticleForm
from recipes.forms import RecipeForm
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

#class PostCreateView(LoginRequiredMixin, CreateView
class PostCreateView(CreateView):
    model = Post

    # fields to be displayed in the form
    fields = ['post_type']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_type_list"] = Post.post_types
        for post_type in Post.post_types:
            context[f'form_{post_type[0]}'] = globals()[f'{post_type[1]}Form']()
        return context

    def form_valid(self, form):
        '''This method is called when valid form data has been POSTed. '''
        print('form is valid')
        print(form.data)
        print(form.cleaned_data)
        form.instance.author = self.request.user
        print(form.cleaned_data['submit'][0])
        if form.cleaned_data['submit'][0] == 'recipe':
            print('that was a recipe')
        elif form.cleaned_data['submit'][0] == 'article':
            print('that was an article')
        form.instance.author = self.form.cleaned_data.author
        
        return super().form_valid(form)
        
    def form_invalid(self, form):
        print('form is invalid')
        '''
        print(form.data)
        print(form.cleaned_data)
        '''
        response = super().form_invalid(form)
        return response
    '''
    def post(self, request):
        print(request.POST)
        return(super(PostCreateView, self).post(request))
        return redirect('/')
    '''
'''
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
'''

class ArticleCreateView(CreateView):
    model = Article

    # fields to be displayed in the form
    fields = [
        'article_title', 
        'article_text',
        ]
    
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
        print(form.data)
        print(form.cleaned_data)
        response = super().form_invalid(form)
        return response
