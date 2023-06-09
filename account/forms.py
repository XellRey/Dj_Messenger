from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):
    avatar = forms.FileField(widget=forms.FileInput(attrs={}))

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name', 'description', 'avatar')


class AddToContact(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('is_contact',)
