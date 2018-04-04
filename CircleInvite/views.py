# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create circleinvite Here

class CircleInviteCreateView(LoginRequiredMixin, CreateView):
    model = models.CircleInvite
    template_name = 'circleinvite/circleinvite_new.html'
    login_url = 'login'

    #cide fields for taking input Here

    fields = ['CircleInvite_Accepted']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# circleinvite Details Here


class CircleInviteDetailView(LoginRequiredMixin, DetailView):
    model = models.CircleInvite
    template_name = 'circleinvite/circleinvite_detail.html'
    login_url = 'login'

# circleinvite ListView Here


class CircleInviteListView(ListView):
    model = models.CircleInvite
    template_name = 'circleinvite/circleinvite_list.html'
    login_url = 'login'

# circleinvite Update Here


class CircleInviteUpdateView(LoginRequiredMixin, UpdateView):
    model = models.CircleInvite

    # Decide fields for editing Here

    fields = ['CircleInvite_Accepted']
    template_name = 'circleinvite/circleinvite_update.html'
    login_url = 'login'

# circleinvite Delete here


class CircleInviteDeleteView(LoginRequiredMixin, DeleteView):
    model = models.CircleInvite
    template_name = 'circleinvite/circleinvite_delete.html'
    success_url = reverse_lazy('circleinvite_list')
    login_url = 'login'



