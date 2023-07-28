from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.sing_up_view, name='signup'),     # .../accounts/signup/
    path('password-change/', views.change_password, name='password_change'),     # .../accounts/password-change/
]
