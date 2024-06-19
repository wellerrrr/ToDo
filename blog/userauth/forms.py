from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

from .models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input text-l rounded py-3 px-3',
                                                             'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input text-l rounded py-3 px-3',
                                                                 'placeholder': 'Password'}))


class SignUpUserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input text-l rounded py-3 px-3',
                                                             'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input text-l rounded py-3 px-3',
                                                          'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input text-l rounded py-3 px-3',
                                                                 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input text-l rounded py-3 px-3',
                                                                  'placeholder': 'Confirm password'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password2']