from django.urls import path, include
from django.conf.urls import url
from . import views

# URL patterns to redirect you to the correct page

urlpatterns = [
    path('solookup/',include('solookup.urls')),
    path('signup/', views.signup, name='accounts-signup'),
    path('login/', views.login_view, name='accounts-login'),
    path('logout/', views.logout_view, name='accounts-logout'),
    path('reset/',views.reset_view, name='accounts-reset')
]