from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Recipe(models.Model):
    primary_key = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_last_edited = models.DateTimeField(auto_now=True)
    source = models.CharField(max_length=100)
    difficulty_choices = [
        ('hard', 'Hard'),
        ('medium', 'Medium'),
        ('easy','Easy'),
    ]
    difficulty = models.CharField(max_length=10, choices=difficulty_choices)
    servings = models.CharField(max_length=3)
    prep_time = models.DurationField()
    cook_time = models.DurationField()
    note = models.TextField(blank=True, default='')
    
    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})
    
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=30)
    unit_of_measurement = models.CharField(max_length=10)
    quantity = models.CharField(max_length=10)
    
    def __str__(self):
        return self.ingredient
