from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe12, name='subscribe12'),
]
