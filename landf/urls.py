import django.views.defaults
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="landf-home"),
    path('home/', views.home, name="landf-home"),
    path('about/', views.about, name="landf-about"),
    path('profile/', views.profile, name="landf-profile"),
    path('login/', views.login, name="landf-login"),
    # path('register/', views.register, name="landf-register"),
    # path('*/', views.error, name="landf-error")
    path('contact/', views.contact, name="landf-contact"),

]
