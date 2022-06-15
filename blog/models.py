from django.db import models

class Post(models.Model):
    primary_key = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_last_edited = models.DateField(auto_now=True)
    post_types = [
        ('announcement','Announcement'), #first element is the value set in model, second is the human-readable name
        ('recipe','Recipe'),
        ('personal_article','Personal Article'),
        ('diy','DIY'),
    ]
    post_type = models.CharField(max_length=100, choices=post_types)