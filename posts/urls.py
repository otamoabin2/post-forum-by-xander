from django.conf.urls import url
from django.views.generic import RedirectView
from django.urls import path, include, reverse
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.new_post, name='new_post'),
    path('<int:pk>/edit', views.post_edit, name='post_edit'),
    path('<int:pk>/delete', views.post_delete, name='post_delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
