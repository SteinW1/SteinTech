from django.contrib import admin
from .models import Recipe,Ingredient

admin.site.register(Recipe)
admin.site.register(Ingredient)

admin.site.site_header = 'SteinTech Admin'
admin.site.index_title = 'Site Information and Data'
admin.site.site_title = 'SteinTech Admin'
