"""URL configuration for django-smart-export tests."""

from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/admin/", permanent=False)),
    path("admin/", admin.site.urls),
]

admin.site.site_header = "Django Smart Export - Administration"
admin.site.site_title = "Django Smart Export Admin"
admin.site.index_title = "Welcome to Django Smart Export"
