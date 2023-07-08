from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.sing_up_view, name='signup'),
    path('password-change/', views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
]
