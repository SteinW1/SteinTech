from django.contrib import admin
from .models import Recipe, Ingredient, RecipeStep

admin.site.site_header = 'SteinTech Admin'
admin.site.index_title = 'Site Information and Data'
admin.site.site_title = 'SteinTech Admin'

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1
    readonly_fields = [
        'quantity_float',
    ]

class RecipeStepInline(admin.TabularInline):
    model = RecipeStep
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, RecipeStepInline]
    raw_id_fields = ['author']
    readonly_fields = [
        'slug',
        'date_posted',
        'date_last_edited',
    ]

admin.site.register(Recipe, RecipeAdmin)
