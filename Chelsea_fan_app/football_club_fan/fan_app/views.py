from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import User, Profile, Post, Comment
from .forms import RegistrationForm, PostForm, CommentForm, UserProfileForm
from django.contrib.auth import login, logout
from django.views.generic import FormView
from django.contrib.auth.models import User, auth
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


class CustomLoginView(LoginView):
    template_name = 'login.html'


class CustomLogoutView(LogoutView):
    pass


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')  # Redirect to home page on successful registration

    def form_valid(self, form):
        user = form.save()
        user.backend = f"{ModelBackend.__module__}.{ModelBackend.__qualname__}"
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        selected_country = form.cleaned_data.get('country')
        profile = Profile.objects.create(user=user, first_name=first_name, last_name=last_name,
                                         country=selected_country)
        login(self.request, user)
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'profile_edit.html'
    fields = ['first_name', 'last_name', 'country', 'birth_date', 'favorite_player', 'favorite_match']

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.profile.pk})


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
