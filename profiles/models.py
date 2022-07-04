from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    slug = models.SlugField(null=False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'slug': self.slug})
    