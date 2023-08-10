from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from .models import Profile, Post
from .widgets import BootstrapDateTimePickerInput


class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=BootstrapDateTimePickerInput()
    )


class RegistrationForm(UserCreationForm):
    # Custom profile fields
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    birth_date = forms.DateField(required=True)
    country = CountryField().formfield()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'country', 'birth_date', 'email', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    bio = forms.CharField()
    profile_picture = forms.ImageField()
    favorite_player = forms.CharField(max_length=100)
    favorite_match = forms.CharField(max_length=200)

    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture', 'birth_date', 'country', 'favorite_player', 'favorite_match']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
