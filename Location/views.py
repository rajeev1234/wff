# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create Location Here

class LocationCreateView(LoginRequiredMixin, CreateView):
    model = models.Location
    template_name = 'Location/Location_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Location_Area','Location_Authorities_Involved','Location_Budget','Location_City','Location_Description','Location_District','Location_Locality','Location_Name','Location_Postal_Address','Location_Creator','Location_Financial','Location_Id','Location_Latitude','Location_Longitude','Location_Subcategory','Location_Modifications_Allowed','Location_Ownership_Status','Location_Pincode','Location_Restrictions','Location_State','Location_Street_Address','Location_Surrounding']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.Location_Author = self.request.user
        return super().form_valid(form)

# Location Details Here


class LocationDetailView(LoginRequiredMixin, DetailView):
    model = models.Location
    template_name = 'Location/Location_detail.html'
    login_url = 'login'

# Location ListView Here


class LocationListView(ListView):
    model = models.Location
    template_name = 'Location/Location_list.html'
    login_url = 'login'

# Location Update Here


class LocationUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Location

    # Decide fields for editing Here

    fields = ['Location_Area','Location_Authorities_Involved','Location_Budget','Location_City','Location_Description','Location_District','Location_Locality','Location_Name','Location_Postal_Address','Location_Creator','Location_Financial','Location_Id','Location_Latitude','Location_Longitude','Location_Subcategory','Location_Modifications_Allowed','Location_Ownership_Status','Location_Pincode','Location_Restrictions','Location_State','Location_Street_Address','Location_Surrounding']
    template_name = 'Location/Location_update.html'
    login_url = 'login'

# Location Delete here


class LocationDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Location
    template_name = 'Location/Location_delete.html'
    success_url = reverse_lazy('Location_list')
    login_url = 'login'



