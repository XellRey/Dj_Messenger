from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('chat/', views.chat_view, name='chat'),
    path('<int:userid>/', views.user_chat, name='user_chat'),
]
