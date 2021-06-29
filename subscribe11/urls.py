from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe11, name='subscribe11'),
]
