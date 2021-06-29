from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe3, name='subscribe3'),
]
