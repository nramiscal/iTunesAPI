from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('get_movie', views.get_movie),
]
