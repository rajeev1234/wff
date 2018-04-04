# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create location_psndc Here

class LocationPSnDCCreateView(LoginRequiredMixin, CreateView):
    model = models.LocationPSnDC
    template_name = 'location_psndc/location_psndc_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['LocationPSnDC_Dc_Office','LocationPSnDC_Dcp_Office','LocationPSnDC_Location_Id','LocationPSnDC_Police_Station','LocationPSnDC_Message']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.LocationPSnDC_Author = self.request.user
        return super().form_valid(form)

# location_psndc Details Here


class LocationPSnDCDetailView(LoginRequiredMixin, DetailView):
    model = models.LocationPSnDC
    template_name = 'location_psndc/location_psndc_detail.html'
    login_url = 'login'
    context_object_name = 'LocationPSnDC'

# location_psndc ListView Here


class LocationPSnDCListView(ListView):
    model = models.LocationPSnDC
    context_object_name = 'LocationPSnDC'
    template_name = 'location_psndc/location_psndc_list.html'
    login_url = 'login'

# location_psndc Update Here


class LocationPSnDCUpdateView(LoginRequiredMixin, UpdateView):
    model = models.LocationPSnDC

    # Decide fields for editing Here

    fields = ['LocationPSnDC_Dc_Office','LocationPSnDC_Dcp_Office','LocationPSnDC_Location_Id','LocationPSnDC_Police_Station','LocationPSnDC_Message']
    template_name = 'location_psndc/location_psndc_update.html'
    login_url = 'login'

# location_psndc Delete here


class LocationPSnDCDeleteView(LoginRequiredMixin, DeleteView):
    model = models.LocationPSnDC
    template_name = 'location_psndc/location_psndc_delete.html'
    success_url = reverse_lazy('location_psndc_list')
    login_url = 'login'
