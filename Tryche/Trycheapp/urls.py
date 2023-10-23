from django.urls import path
from .views import *
from Trycheapp import views

urlpatterns = [
        path('', views.home, name='home'),
]