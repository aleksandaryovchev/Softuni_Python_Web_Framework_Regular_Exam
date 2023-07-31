from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture', 'birth_date', 'country', 'favorite_player', 'favorite_match']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
