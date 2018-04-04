# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create Location_Amenitie Here

class Location_AmenitieCreateView(LoginRequiredMixin, CreateView):
    model = models.Location_Amenitie
    template_name = 'Location_Amenitie/Location_Amenitie_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Location_Amenitie_Carparking','Location_Amenitie_Carparking_Latitide','Location_Amenitie_Carparking_Longitude','Location_Amenitie_Catering_Base','Location_Amenitie_Catering_Base_Latitude','Location_Amenitie_Catering_Base_Longitude','Location_Amenitie_Controlling_Status','Location_Amenitie_Genset_Parking','Location_Amenitie_Genset_Parking_Latitude','Location_Amenitie_Genset_Parking_Longitude','Location_Amenitie_Location_Id','Location_Amenitie_Truck_Parking_Latitude','Location_Amenitie_Truck_Parking_Longitude','Location_Amenitie_Vanity_Parking','Location_Amenitie_Vanity_Parking_Latitude','Location_Amenitie_Vanity_Parking_Longitude','Location_Amenitie_Washroom','Location_Amenitie_Creator',]

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.Location_Amenitie_Author = self.request.user
        return super().form_valid(form)

# Location_Amenitie Details Here


class Location_AmenitieDetailView(LoginRequiredMixin, DetailView):
    model = models.Location_Amenitie
    template_name = 'Location_Amenitie/Location_Amenitie_detail.html'
    login_url = 'login'

# Location_Amenitie ListView Here


class Location_AmenitieListView(ListView):
    model = models.Location_Amenitie
    template_name = 'Location_Amenitie/Location_Amenitie_list.html'
    login_url = 'login'

# Location_Amenitie Update Here


class Location_AmenitieUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Location_Amenitie

    # Decide fields for editing Here

    fields = ['Location_Amenitie_Carparking','Location_Amenitie_Carparking_Latitide','Location_Amenitie_Carparking_Longitude','Location_Amenitie_Catering_Base','Location_Amenitie_Catering_Base_Latitude','Location_Amenitie_Catering_Base_Longitude','Location_Amenitie_Controlling_Status','Location_Amenitie_Genset_Parking','Location_Amenitie_Genset_Parking_Latitude','Location_Amenitie_Genset_Parking_Longitude','Location_Amenitie_Location_Id','Location_Amenitie_Truck_Parking_Latitude','Location_Amenitie_Truck_Parking_Longitude','Location_Amenitie_Vanity_Parking','Location_Amenitie_Vanity_Parking_Latitude','Location_Amenitie_Vanity_Parking_Longitude','Location_Amenitie_Washroom','Location_Amenitie_Creator',]
    template_name = 'Location_Amenitie/Location_Amenitie_update.html'
    login_url = 'login'

# Location_Amenitie Delete here


class Location_AmenitieDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Location_Amenitie
    template_name = 'Location_Amenitie/Location_Amenitie_delete.html'
    success_url = reverse_lazy('Location_Amenitie_list')
    login_url = 'login'



