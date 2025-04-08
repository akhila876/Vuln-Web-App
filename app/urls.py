from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('gallery/', views.gallery_view, name='gallery'),
   
    path('create_post/', views.create_post, name='create_post'),
    path('change_password/', views.change_password, name='change_password'),
]
