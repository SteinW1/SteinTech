from django.db import models
from blog.models import Post
from django.contrib.auth.models import User

class Recipe(models.Model):
    post = models.OneToOneField(
        Post,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    
    difficulty_choices = [
        ('hard', 'Hard'),
        ('medium', 'Medium'),
        ('easy','Easy'),
    ]
    difficulty = models.CharField(max_length=10, choices=difficulty_choices)
    servings = models.CharField(max_length=3)
    prep_time = models.DurationField()
    cook_time = models.DurationField()
    note = models.TextField()
    
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=30)
    unit_of_measurement = models.CharField(max_length=10)
    quantity = models.CharField(max_length=10)
    
    def __str__(self):
        return self.ingredient
