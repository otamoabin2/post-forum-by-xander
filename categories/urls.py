from django.conf.urls import url
from django.views.generic import RedirectView
from django.urls import path, include
from . import views
from django.contrib import admin
import config

urlpatterns = [

    # path('', views.landing_page, name='landing_page'),
    path('categories/', views.category_list, name='index'),
    path('categories/<int:pk>', include('posts.urls')),
    path('categories/new/', views.category_create, name='category_new'),
    path('categories/<int:pk>/edit', views.category_update, name='category_edit'),
    path('categories/<int:pk>/delete',
         views.category_delete, name='category_delete'),
    path('categories/<int:pk>/posts/', include('posts.urls')),
]
