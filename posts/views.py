from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.forms import ModelForm
from datetime import datetime
from categories.models import Categories
from django.urls import reverse
from django.contrib.auth.models import User
import config


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'category', 'title', 'text']


def post_list(request, pk):
    posts = Post.objects.all()
    this_category = get_object_or_404(Categories, pk=pk)
    posts2 = []
    for post in posts:
        if post.category == this_category:
            posts2.append(post)
        config.z = posts2
    config.x = this_category.id
    return render(request, 'Post_List.html', {'posts': posts2, 'category': this_category}, config.z)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    this_category = Categories.objects.all()
    return render(request, 'Post_Detail.html', {'post': post, 'category': config.x})


def new_post(request, pk):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form, 'type_of_request': 'new'})


def post_edit(request, pk, template_name='post_form.html'):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form': form, 'new_or_edit': 'Edit'})


def post_delete(request, pk, template_name='post_confirm_delete.html'):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, template_name, {'object': post})
