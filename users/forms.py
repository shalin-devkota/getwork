from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']


class ProfileRegistrationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['email','about_me','profile_picture','cover_picture']

class ProfileUpdateForm(forms.ModelForm):
    #profile_picutre = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['profile_picture','cover_picture']
