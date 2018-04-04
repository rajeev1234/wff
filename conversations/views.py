# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create conversations Here

class ConversationsCreateView(LoginRequiredMixin, CreateView):
    model = models.Conversations
    template_name = 'conversations/conversations_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Conversations_Message_List']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# conversations Details Here


class ConversationsDetailView(LoginRequiredMixin, DetailView):
    model = models.Conversations
    template_name = 'conversations/conversations_detail.html'
    login_url = 'login'

# conversations ListView Here


class ConversationsListView(ListView):
    model = models.Conversations
    template_name = 'conversations/conversations_list.html'
    login_url = 'login'

# conversations Update Here


class ConversationsUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Conversations

    # Decide fields for editing Here

    fields = ['Conversations_Message_List']
    template_name = 'conversations/conversations_update.html'
    login_url = 'login'

# conversations Delete here


class ConversationsDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Conversations
    template_name = 'conversations/conversations_delete.html'
    success_url = reverse_lazy('conversations_list')
    login_url = 'login'



