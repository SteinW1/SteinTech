from django import forms
from recipes.models import Recipe, Ingredient

class RecipeForm(forms.Form):
    recipe_title = forms.CharField(
        required=True,
        label='Recipe Title',
        widget=forms.TextInput(
            attrs={'placeholder':'What\'s the recipe\'s name?'
                },
        ))
    
    source = forms.CharField(
        required=True,
        label='Source',
        widget=forms.TextInput(
            attrs={'placeholder':'Where did this recipe come from?'
                },
        ))
        
    difficulty = forms.CharField(
        required=True,
        label='Difficulty',
        widget=forms.RadioSelect(
            choices=Recipe.difficulty_choices,
            attrs={
                },
        ))
        
    servings = forms.DecimalField(
            required=True,
            label='servings',
            max_digits=4,
            decimal_places=2
        )
        
    cook_time = forms.DecimalField(
            required=True,
            label='cook_time',
            max_digits=4,
            decimal_places=2
        )
    
    prep_time = forms.DecimalField(
            required=True,
            label='prep_time',
            max_digits=4,
            decimal_places=2
        )
