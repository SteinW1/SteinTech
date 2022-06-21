from django import forms
from .models import Post
from recipes.models import Recipe, Ingredient

class PostForm(forms.Form):
    title = forms.CharField(
        required=True,
        label='Title',
        widget=forms.TextInput(
            attrs={'placeholder':'Enter post title...'},
        ))

    author = forms.CharField(
        required=True,
        label='Author',
        widget=forms.TextInput(
            attrs={'placeholder':'Who\'s post is this?'},
        ))

    post_type = forms.ChoiceField(
        choices=Post.post_types,
        required=True,
        label='Post Type',
)

class ArticleForm(forms.Form):
    article_title = forms.CharField(
        required=True,
        label='Title',
        widget=forms.TextInput(
            attrs={'placeholder':'Enter article title...'},
        ))
    
    article_text = forms.CharField(
        required=True,
        label='Article',
        widget=forms.Textarea(
            attrs={'placeholder':'Put article text here.'}
        ))