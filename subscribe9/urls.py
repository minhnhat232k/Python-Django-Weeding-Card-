from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe9, name='subscribe9'),
]
