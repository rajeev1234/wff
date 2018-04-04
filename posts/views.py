# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create Post Here

class PostCreateView(LoginRequiredMixin, CreateView):
    model = models.Post
    template_name = 'posts/post_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Post_Message']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.Post_Author = self.request.user
        return super().form_valid(form)

# Post Details Here


class PostDetailView(LoginRequiredMixin, DetailView):
    model = models.Post
    template_name = 'posts/post_detail.html'
    login_url = 'login'

# Post ListView Here


class PostListView(ListView):
    model = models.Post
    template_name = 'posts/post_list.html'
    login_url = 'login'

# Post Update Here


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Post

    # Decide fields for editing Here

    fields = ['Post_Message']
    template_name = 'posts/post_update.html'
    login_url = 'login'

# Post Delete here


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('post_list')
    login_url = 'login'



