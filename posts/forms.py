from django import forms
from .models import Post
from datetime import datetime


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'category', 'title', 'text')
