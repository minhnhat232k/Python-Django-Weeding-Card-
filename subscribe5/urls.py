from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe5, name='subscribe5'),
]
