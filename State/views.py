# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create State Here

class StateCreateView(LoginRequiredMixin, CreateView):
    model = models.State
    template_name = 'States/State_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = [
            'States',
          ]

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.State_Author = self.request.user
        return super().form_valid(form)

# State Details Here


class StateDetailView(LoginRequiredMixin, DetailView):
    model = models.State
    context_object_name = 'State'
    template_name = 'States/State_details.html'
    login_url = 'login'

# State ListView Here


class StateListView(ListView):
    model = models.State
    template_name = 'States/State_list.html'
    login_url = 'login'

# State Update Here


class StateUpdateView(LoginRequiredMixin, UpdateView):
    model = models.State

    # Decide fields for editing Here

    fields = [
            'States',
          ]


    template_name = 'States/State_update.html'
    login_url = 'login'

# State Delete here


class StateDeleteView(LoginRequiredMixin, DeleteView):
    model = models.State
    template_name = 'States/State_delete.html'
    success_url = reverse_lazy('State_list')
    login_url = 'login'



