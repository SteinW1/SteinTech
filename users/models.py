from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    slug = models.SlugField(null=False, unique=True)
