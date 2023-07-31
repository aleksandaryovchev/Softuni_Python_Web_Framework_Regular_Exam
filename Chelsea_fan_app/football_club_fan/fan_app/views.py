from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import User, Profile, Post, Comment
from .forms import UserProfileForm, PostForm, CommentForm


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


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'register.html', {'form': form})


class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html')


class EditProfileView(UpdateView):
    model = Profile
    form_class = UserProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('profile')


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
