# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create police_station Here

class PoliceStationCreateView(LoginRequiredMixin, CreateView):
    model = models.PoliceStation
    template_name = 'police_station/police_station_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['PoliceStation_Area_Police_Station','PoliceStation_DCP','PoliceStation_Station_Name']

    # Set fields from current data or automated data
    #
    def form_valid(self, form):
        form.instance.PoliceStation_Author = self.request.user
        return super().form_valid(form)

# police_station Details Here


class PoliceStationDetailView(LoginRequiredMixin, DetailView):
    model = models.PoliceStation
    context_object_name = 'PoliceStation'
    template_name = 'police_station/police_station_detail.html'
    login_url = 'login'

# police_station ListView Here


class PoliceStationListView(ListView):
    model = models.PoliceStation
    template_name = 'police_station/police_station_list.html'
    login_url = 'login'

# police_station Update Here


class PoliceStationUpdateView(LoginRequiredMixin, UpdateView):
    model = models.PoliceStation

    # Decide fields for editing Here

    fields = ['PoliceStation_Area_Police_Station','PoliceStation_DCP','PoliceStation_Station_Name']
    template_name = 'police_station/police_station_update.html'
    login_url = 'login'

# police_station Delete here


class PoliceStationDeleteView(LoginRequiredMixin, DeleteView):
    model = models.PoliceStation
    template_name = 'police_station/police_station_delete.html'
    success_url = reverse_lazy('police_station_list')
    login_url = 'login'
