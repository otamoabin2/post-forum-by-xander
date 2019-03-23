
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', RedirectView.as_view(url='/categories/', permanent=True)),
    path('categories/', include('categories.urls')),
    path('', include('categories.urls')),
    # path('', include('categories.urls')),
    # path('categories/<int:pk>/posts', include('posts.urls')),
    # path('categories/<int:pk>/posts/', include('posts.urls')),
]
