from django.conf import settings
from django.db import models
from datetime import datetime
from django.utils import timezone
from categories.models import Categories
from django.core.validators import MaxLengthValidator
# if stuff breaks, uncomment above and do the opposite in the other models
from django.contrib.auth.models import User
import config
from django.core.validators import MaxLengthValidator
from django import forms


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(
        'categories.Categories', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.title
