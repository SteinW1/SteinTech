from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    slug = models.SlugField(default='site_admin_01', null=False, unique=True)
    
    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'slug': self.slug})
    