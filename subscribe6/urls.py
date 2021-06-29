from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe6, name='subscribe6'),
]
