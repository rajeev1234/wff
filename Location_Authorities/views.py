# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create Location_Authoritis Here

class Location_AuthoritisCreateView(LoginRequiredMixin, CreateView):
    model = models.LocationAuthority
    template_name = 'Location_Authorities/Location_Authorities_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Location_Authority_Detail','Location_Authority_Email','Location_Authority_Google_Address','Location_Authority_Latitude','Location_Authority_Longitude','Location_Authority_Name','Location_Authority_Postal_Address','Location_Authority_Contact_Number','Location_Authority_Contact_Name','Location_Authority_Locality_City_State','Location_Authority_Location_ID','Location_Authority_Office_Charges','Location_Authority_Street_Address','Location_Authority_Creator']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.Location_Authoritis_Author = self.request.user
        return super().form_valid(form)

# Location_Authoritis Details Here


class Location_AuthoritisDetailView(LoginRequiredMixin, DetailView):
    model = models.LocationAuthority
    template_name = 'Location_Authorities/Location_Authorities_detail.html'
    login_url = 'login'

# Location_Authoritis ListView Here


class Location_AuthoritisListView(ListView):
    model = models.LocationAuthority
    template_name = 'Location_Authorities/Location_Authorities_list.html'
    login_url = 'login'

# Location_Authoritis Update Here


class Location_AuthoritisUpdateView(LoginRequiredMixin, UpdateView):
    model = models.LocationAuthority

    # Decide fields for editing Here

    fields = ['Location_Authority_Detail','Location_Authority_Email','Location_Authority_Google_Address','Location_Authority_Latitude','Location_Authority_Longitude','Location_Authority_Name','Location_Authority_Postal_Address','Location_Authority_Contact_Number','Location_Authority_Contact_Name','Location_Authority_Locality_City_State','Location_Authority_Location_ID','Location_Authority_Office_Charges','Location_Authority_Street_Address','Location_Authority_Creator']
    template_name = 'Location_Authorities/Location_Authorities_update.html'
    login_url = 'login'

# Location_Authoritis Delete here


class Location_AuthoritisDeleteView(LoginRequiredMixin, DeleteView):
    model = models.LocationAuthority
    template_name = 'Location_Authorities/Location_Authorities_delete.html'
    success_url = reverse_lazy('Location_Authoritis_list')
    login_url = 'login'



