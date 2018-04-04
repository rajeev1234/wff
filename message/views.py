# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create messages Here

class MessagesCreateView(LoginRequiredMixin, CreateView):
    model = models.Messages
    template_name = 'messages/messages_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Messages_Subject','Messages_Message']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.Messages_Author = self.request.user
        return super().form_valid(form)

# messages Details Here


class MessagesDetailView(LoginRequiredMixin, DetailView):
    model = models.Messages
    context_object_name = 'Messages'
    template_name = 'messages/messages_detail.html'
    login_url = 'login'

# messages ListView Here


class MessagesListView(ListView):
    model = models.Messages
    template_name = 'messages/messages_list.html'
    login_url = 'login'

# messages Update Here


class MessagesUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Messages

    # Decide fields for editing Here

    fields = ['Messages_Message','Messages_Subject']
    template_name = 'messages/messages_update.html'
    login_url = 'login'

# messages Delete here


class MessagesDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Messages
    template_name = 'messages/messages_delete.html'
    success_url = reverse_lazy('messages_list')
    login_url = 'login'
