from django.contrib import admin
from django.urls import path
from django_smart_export.views import ExportDummyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('export/', ExportDummyView.as_view(), name='export_dummy'),
]
