# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create amenity_adresses Here

class AmenityAdressesCreateView(LoginRequiredMixin, CreateView):
    model = models.Amenity_Adresses
    template_name = 'amenity_adresses/amenity_adresses_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Amenity_Adresses_Car_Parking',
'Amenity_Adresses_Catering_Base',
'Amenity_Adresses_Genset_Parking',
'Amenity_Adresses_Location_Id',
'Amenity_Adresses_Truck_Parking',
'Amenity_Adresses_Vanity_Parking',]

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.user= self.request.user
        return super().form_valid(form)

# amenity_adresses Details Here


class AmenityAdressesDetailView(LoginRequiredMixin, DetailView):
    model = models.Amenity_Adresses
    template_name = 'amenity_adresses/amenity_adresses_detail.html'
    login_url = 'login'

# amenity_adresses ListView Here


class AmenityAdressesListView(ListView):
    model = models.Amenity_Adresses
    template_name = 'amenity_adresses/amenity_adresses_list.html'
    login_url = 'login'

# amenity_adresses Update Here


class AmenityAdressesUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Amenity_Adresses

    # Decide fields for editing Here

    fields = ['Amenity_Adresses_Car_Parking',
'Amenity_Adresses_Catering_Base',
'Amenity_Adresses_Genset_Parking',
'Amenity_Adresses_Location_Id',
'Amenity_Adresses_Truck_Parking',
'Amenity_Adresses_Vanity_Parking',]

    template_name = 'amenity_adresses/amenity_adresses_update.html'
    login_url = 'login'

# amenity_adresses Delete here


class AmenityAdressesDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Amenity_Adresses
    template_name = 'amenity_adresses/amenity_adresses_delete.html'
    success_url = reverse_lazy('amenity_adresses_list')
    login_url = 'login'



