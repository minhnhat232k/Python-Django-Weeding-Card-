from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe4, name='subscribe4'),
]
