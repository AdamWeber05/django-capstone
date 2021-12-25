from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from .views import SearchResultsView, AllBoatsView


urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.update_step, name='udpate'),
    path('<int:pk>/generate-PDF/', views.generate_pdf, name='generate-PDF'),
    path('newboat/', views.BoatGenerateView.as_view(), name='newboat'),
    path('newboat/processing/',views.process_form_data, name='processing'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('all/', AllBoatsView.as_view(), name='all_boats'),
]
