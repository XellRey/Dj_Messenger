from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view()),
    path('profile/', views.profile_view, name='profile'),
    path('chat/', views.chat_view, name='chat'),
    path('<int:userid>', views.user_chat, name='user_chat'),
    path('add/operation/<operation>/<pk>/', views.add_new_friend, name='add'),
    path('remove/<operation>/<pk>', views.add_new_friend, name='remove'),
    path('block/<operation>/<pk>/', views.block_user, name='block'),
    path('unblock/<operation>/<pk>/', views.block_user, name='unblock'),
    path('sent_msg/<str:userid>', views.sent_messages, name='sent_msg'),
    path('rec_msg/<str:userid>', views.received_messages, name="rec_msg"),
]
