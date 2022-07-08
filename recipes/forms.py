from django.forms import ModelForm, Textarea, inlineformset_factory
from recipes.models import Ingredient, Recipe, RecipeStep


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'difficulty', 'servings', 'cook_time', 'prep_time', 'note']
        widgets = {
            'note': Textarea(attrs={'cols': 60, 'rows': 4}),
        }


class RecipeStepForm(ModelForm):   
    class Meta:
        model = RecipeStep
        fields = ['recipe_step_text',]


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ingredient_name', 'unit_of_measurement', 'quantity',]


RecipeIngredientFormset = inlineformset_factory(
    Recipe, Ingredient, fields=('ingredient_name','unit_of_measurement','quantity')
    )

RecipeStepFormset = inlineformset_factory(
    Recipe, RecipeStep, fields=('recipe_step_text',)
    )
