from django.contrib import admin
from django.urls import path, include
from pages.views import home_view
from . import views

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
]