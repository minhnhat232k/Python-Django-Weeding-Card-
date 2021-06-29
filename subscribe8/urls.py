from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe8, name='subscribe8'),
]
