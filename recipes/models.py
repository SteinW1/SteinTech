from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from profiles.models import User
from .utils import number_str_to_float
from .validators import validate_unit_of_measurement, validate_quantity_measurement

class Recipe(models.Model):
    primary_key = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, null=False, unique=True)
    slug = models.SlugField(null=False, unique=True)
    approved_by_staff = models.BooleanField(default=False)

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
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.slug
    
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=30)
    unit_of_measurement = models.CharField(max_length=12, validators=[validate_unit_of_measurement])
    quantity = models.CharField(max_length=10, validators=[validate_quantity_measurement])
    quantity_float = models.FloatField(null=True, default=None)

    def save(self, *args, **kwargs):
        test_float, conversion_success = number_str_to_float(self.quantity)
        if conversion_success:
            self.quantity_float = test_float
        else:
            self.quantity_float = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.ingredient_name

class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    recipe_step_text = models.TextField(blank = True, default=None)
