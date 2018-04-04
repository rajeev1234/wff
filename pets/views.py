# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create pets Here

class PetsCreateView(LoginRequiredMixin, CreateView):
    model = models.Pets
    template_name = 'pets/pets_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Pets_Age','Pets_Animal_Type','Pets_Breed','Pets_Daily_Charges','Pets_Description','Pets_Ownership_Status','Pets_Weekly_Charges']

    # Set fields from current data or automated data
    #
    def form_valid(self, form):
        form.instance.Pets_Author = self.request.user
        return super().form_valid(form)

# pets Details Here


class PetsDetailView(LoginRequiredMixin, DetailView):
    model = models.Pets
    context_object_name = 'Pets'
    template_name = 'pets/pets_detail.html'
    login_url = 'login'

# pets ListView Here


class PetsListView(ListView):
    model = models.Pets
    template_name = 'pets/pets_list.html'
    login_url = 'login'

# pets Update Here


class PetsUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Pets

    # Decide fields for editing Here

    fields = ['Pets_Age','Pets_Animal_Type','Pets_Breed','Pets_Daily_Charges','Pets_Description','Pets_Ownership_Status','Pets_Weekly_Charges']
    template_name = 'pets/pets_update.html'
    login_url = 'login'

# pets Delete here


class PetsDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Pets
    template_name = 'pets/pets_delete.html'
    success_url = reverse_lazy('pets_list')
    login_url = 'login'
