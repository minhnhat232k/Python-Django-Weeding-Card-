from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from users import views as user_views 

urlpatterns = [
   path('', views.index, name="home"),
   path('review/', views.review, name="review"),
   path('product/', views.product, name="product"),
   path('introduce/', views.introduce, name="introduce"),

   path('profile/', user_views.profile, name = 'profile'),
   path('contact/', views.contact, name='contact'),
   path('register/', views.register, name="register"),
   path('login/',auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
   path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
   
]