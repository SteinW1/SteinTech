from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    primary_key = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_last_edited = models.DateTimeField(auto_now=True)
    post_types = [
        ('recipe','Recipe'), #first element is the value set in model, second is the human-readable name
        ('personal_article','Personal Article'),
    ]
    post_type = models.CharField(max_length=100, choices=post_types)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
