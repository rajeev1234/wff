# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create location_pitch Here

class LocationPitchCreateView(LoginRequiredMixin, CreateView):
    model = models.LocationPitch
    template_name = 'location_pitch/location_pitch_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['LocationPitch_Message','LocationPitch_By_User','LocationPitch_Location_Required','LocationPitch_Submitted']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.location_pitch_Author = self.request.user
        return super().form_valid(form)

# location_pitch Details Here


class LocationPitchDetailView(LoginRequiredMixin, DetailView):
    model = models.LocationPitch
    context_object_name = 'LocationPitch'
    template_name = 'location_pitch/location_pitch_detail.html'
    login_url = 'login'

# location_pitch ListView Here


class LocationPitchListView(ListView):
    model = models.LocationPitch
    template_name = 'location_pitch/location_pitch_list.html'
    login_url = 'login'

# location_pitch Update Here


class LocationPitchUpdateView(LoginRequiredMixin, UpdateView):
    model = models.LocationPitch

    # Decide fields for editing Here

    fields = ['LocationPitch_Message','LocationPitch_By_User','LocationPitch_Location_Required','LocationPitch_Submitted']
    template_name = 'location_pitch/location_pitch_update.html'
    login_url = 'login'

# location_pitch Delete here


class LocationPitchDeleteView(LoginRequiredMixin, DeleteView):
    model = models.LocationPitch
    template_name = 'location_pitch/location_pitch_delete.html'
    success_url = reverse_lazy('location_pitch_list')
    login_url = 'login'
