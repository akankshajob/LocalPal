from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('explore/', views.explore, name='explore'),
    path('logout/', views.logout_view, name='logout'),
]
