# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create comments Here

class CommentsCreateView(LoginRequiredMixin, CreateView):
    model = models.Comments
    template_name = 'comments/comments_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Comments_Comment',
'Comments_Helpfull']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# comments Details Here


class CommentsDetailView(LoginRequiredMixin, DetailView):
    model = models.Comments
    template_name = 'comments/comments_detail.html'
    login_url = 'login'

# comments ListView Here


class CommentsListView(ListView):
    model = models.Comments
    template_name = 'comments/comments_list.html'
    login_url = 'login'

# comments Update Here


class CommentsUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Comments

    # Decide fields for editing Here

    fields = ['Comments_Comment',
'Comments_Helpfull']
    template_name = 'comments/comments_update.html'
    login_url = 'login'

# comments Delete here


class CommentsDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Comments
    template_name = 'comments/comments_delete.html'
    success_url = reverse_lazy('comments_list')
    login_url = 'login'



