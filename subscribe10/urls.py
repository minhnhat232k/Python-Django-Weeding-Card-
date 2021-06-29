from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe10, name='subscribe10'),
]
