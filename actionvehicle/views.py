# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create actionvehicle Here

class ActionVehicleCreateView(LoginRequiredMixin, CreateView):
    model = models.ActionVehicle
    template_name = 'actionvehicle/actionvehicle_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['ActionVehicle_Action_Vehicle_Id',
              'ActionVehicle_Color',
              'ActionVehicle_Company',
              'ActionVehicle_Daily_Rent',
              'ActionVehicle_Description',
              'ActionVehicle_Model',
              'ActionVehicle_Modification',
              'ActionVehicle_Monthly_Rent',
'ActionVehicle_Ownership',
'ActionVehicle_Registration_Number',
'ActionVehicle_Rigging',
'ActionVehicle_Weekly_Rent']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# actionvehicle Details Here


class ActionVehicleDetailView(LoginRequiredMixin, DetailView):
    model = models.ActionVehicle
    fields=['ActionVehicle_Color']
    template_name = 'actionvehicle/actionvehicle_detail.html'
    login_url = 'login'

# actionvehicle ListView Here


class ActionVehicleListView(ListView):
    model = models.ActionVehicle
    template_name = 'actionvehicle/actionvehicle_list.html'
    login_url = 'login'

# actionvehicle Update Here


class ActionVehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = models.ActionVehicle


    # Decide fields for editing Here
    fields = ['ActionVehicle_Action_Vehicle_Id',
              'ActionVehicle_Color',
              'ActionVehicle_Company',
              'ActionVehicle_Daily_Rent',
              'ActionVehicle_Description',
              'ActionVehicle_Model',
              'ActionVehicle_Modification',
              'ActionVehicle_Monthly_Rent',
'ActionVehicle_Ownership',
'ActionVehicle_Registration_Number',
'ActionVehicle_Rigging',
'ActionVehicle_Weekly_Rent']
    
    

    template_name = 'actionvehicle/actionvehicle_update.html'
    login_url = 'login'

# actionvehicle Delete here


class ActionVehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = models.ActionVehicle
    template_name = 'actionvehicle/actionvehicle.html'
    success_url = reverse_lazy('actionvehicle_list')
    login_url = 'login'



