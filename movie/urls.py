"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""
from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='Home'),
    path('login/', auth_views.LoginView.as_view(template_name='detail/form.html'), name='Login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='detail/form.html'), name='Logout'),
    path('register/', register, name='Signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('search/', search, name='search'),
    path('addmovie/', addMovie, name='addMovie'),
    path('addshows/', addShows, name='addShows'),
    # path('viewshows/', addMovie, name='viewShows'),
    path('buytickets/', buyTickets, name='buyTickets'),
]