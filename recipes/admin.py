from django.contrib import admin
from .models import Recipe, Ingredient, RecipeDirection

admin.site.site_header = 'SteinTech Admin'
admin.site.index_title = 'Site Information and Data'
admin.site.site_title = 'SteinTech Admin'

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1

class DirectionInline(admin.TabularInline):
    model = RecipeDirection
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, DirectionInline]
    raw_id_fields = ['author']
    readonly_fields = [
        'slug',
        'date_posted',
        'date_last_edited',
    ]

admin.site.register(Recipe, RecipeAdmin)
