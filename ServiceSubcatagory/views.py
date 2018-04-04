# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create ServiceSubcatagory Here

class ServiceSubcatagoryCreateView(LoginRequiredMixin, CreateView):
    model = models.ServiceSubcatagory
    template_name = 'ServiceSubcatagory/ServiceSubcatagory_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = [
            'Service_Subcatagory_Name'
            ]

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.ServiceSubcatagory_Author = self.request.user
        return super().form_valid(form)

# ServiceSubcatagory Details Here


class ServiceSubcatagoryDetailView(LoginRequiredMixin, DetailView):
    model = models.ServiceSubcatagory
    context_object_name = 'ServiceSubcatagory'
    template_name = 'ServiceSubcatagory/ServiceSubcatagory_details.html'
    login_url = 'login'

# ServiceSubcatagory ListView Here


class ServiceSubcatagoryListView(ListView):
    model = models.ServiceSubcatagory
    template_name = 'ServiceSubcatagory/ServiceSubcatagory_list.html'
    login_url = 'login'

# ServiceSubcatagory Update Here


class ServiceSubcatagoryUpdateView(LoginRequiredMixin, UpdateView):
    model = models.ServiceSubcatagory

    # Decide fields for editing Here

    fields = [
            'Service_Subcatagory_Name'
            ]


    template_name = 'ServiceSubcatagory/ServiceSubcatagory_update.html'
    login_url = 'login'

# ServiceSubcatagory Delete here


class ServiceSubcatagoryDeleteView(LoginRequiredMixin, DeleteView):
    model = models.ServiceSubcatagory
    template_name = 'ServiceSubcatagory/ServiceSubcatagory_delete.html'
    success_url = reverse_lazy('ServiceSubcatagory_list')
    login_url = 'login'



