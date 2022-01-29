from django.urls import path
from . import views

app_name = 'basic_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='homed'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login')
]
