from django import forms
from recipes.models import Recipe, Ingredient

class RecipeForm(forms.Form):
    source = forms.CharField(
        required=True,
        label='Author',
        widget=forms.TextInput(
            attrs={'placeholder':'Where did this recipe come from?'},
            },
        ))
    difficulty = forms.CharField(
        required=True,
        label='Difficulty',
        widget=forms.RadioSelect(
            choices=Recipe.difficulty_choices,
            attrs={},
            },
        ))
        
    servings = forms.CharField(
        required=True,
        label='Servings',
        models.DecimalField(
            max_digits=4,
            decimal_places=2
        ))
    cook_time = forms.TimeField(
    
        )
    prep_time = forms.TimeField(
    
        )