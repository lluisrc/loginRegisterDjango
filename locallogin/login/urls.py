from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
]