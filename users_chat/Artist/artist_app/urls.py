from django.urls import path
from . import views

urlpatterns = [
     path("",views.base_art,name="base_art"),
    path('register_art/', views.register_art, name='register_art'),
    path('login_art/', views.login_art, name='login_art'),
    path('superuser_art/', views.superuser_art, name='superuser_art'),
    path('user_art/', views.user_art, name='user_art'),
    path('chat/<str:username>/', views.chat_art, name='chat'),
    # path('chat/<int:user_id>/', views.chat_art, name='chat_art'),
    path('logout_art/', views.logout_art, name='logout_art'),
    
    #  path('chat/', views.chat, name='chat'),
]