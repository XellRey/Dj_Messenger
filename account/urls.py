from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.sing_up_view, name='signup'),
]
