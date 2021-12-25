from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.ExcelPageView.as_view(), name = 'excel'),
    path('export', views.export_boat, name = 'export_boat'),
]