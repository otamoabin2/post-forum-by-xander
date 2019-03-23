from django.conf import settings
from django.db import models
from datetime import datetime
# from posts.models import Post
from django.contrib.auth.models import User
import config


class Categories(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
