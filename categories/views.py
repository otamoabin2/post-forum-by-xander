from django.shortcuts import render
from django.http import HttpResponse
from .models import Categories
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoriesForm
from django.forms import ModelForm
from django.urls import reverse
from posts.models import Post
import config


class CategoriesForm(ModelForm):
    class Meta:
        model = Categories
        fields = ['title', ]


def landing_page(request):
    return render(request, 'landing_page.html')


def category_list(request, template_name='Category_List.html'):
    category_list_data = Categories.objects.all()
    return render(request, 'Categories_List.html', {"category_data": category_list_data})


# def category_view(request, pk, template_name='Category_Detail.html'):
#     category = get_object_or_404(Categories, pk=pk)
#     data = {'cat': category}
#     return render(request, template_name, data)

def category_view(request, pk):
    return redirect('post_list', pk=pk)


def new_category(request):
    return render(request, 'Category_New.html')


def category_create(request, template_name='category_form.html'):
    form = CategoriesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form': form, 'new_or_edit': 'New'})


def category_update(request, pk, template_name='category_form.html'):
    category = get_object_or_404(Categories, pk=pk)
    form = CategoriesForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form': form, 'new_or_edit': 'Edit'})


def category_delete(request, pk, template_name='category_confirm_delete.html'):
    category = get_object_or_404(Categories, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('index')
    return render(request, template_name, {'object': category})
