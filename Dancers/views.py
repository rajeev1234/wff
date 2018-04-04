from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse_lazy


# Create your views here.

# Create Dancer Here

class DancerCreateView(LoginRequiredMixin, CreateView):
    model = models.Dancer
    template_name = 'Dancers/Dancer_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = [
    'Dancer_Charges_Available',
    'Dancer_Daily_Charges',
    'Dancer_Dancing_Style',
    'Dancer_Description',
    'Dancer_Genre',
    'Dancer_Creator'
    ]

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.Dancer_Author = self.request.user
        return super().form_valid(form)

# Dancer Details Here


class DancerDetailView(LoginRequiredMixin, DetailView):
    model = models.Dancer
    context_object_name = 'Dancer'
    template_name = 'Dancers/Dancer_details.html'
    login_url = 'login'

# Dancer ListView Here


class DancerListView(ListView):
    model = models.Dancer
    template_name = 'Dancers/Dancer_list.html'
    login_url = 'login'

# Dancer Update Here


class DancerUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Dancer

    # Decide fields for editing Here

    fields = [
    'Dancer_Charges_Available',
    'Dancer_Daily_Charges',
    'Dancer_Dancing_Style',
    'Dancer_Description',
    'Dancer_Genre',
    'Dancer_Creator'
    ]
    template_name = 'Dancers/Dancer_update.html'
    login_url = 'login'

# Dancer Delete here


class DancerDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Dancer
    template_name = 'Dancers/Dancer_delete.html'
    success_url = reverse_lazy('Dancer_list')
    login_url = 'login'



