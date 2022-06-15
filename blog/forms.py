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

    date_posted = forms.DateTimeField(
        input_formats=('%m/%d/%y %H:%M'),
        label='DatePosted',
        )

    post_type = forms.CharField(
        choices=Post.post_types,
        required=True,
        label='Post Type',
        widget=forms.RadioSelect(
            attr={},
        ))