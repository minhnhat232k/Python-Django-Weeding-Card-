from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe2, name='subscribe2'),
]
