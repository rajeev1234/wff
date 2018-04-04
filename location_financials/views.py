# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create LocationFinancial Here

class LocationFinancialCreateView(LoginRequiredMixin, CreateView):
    model = models.LocationFinancial
    template_name = 'location_financial/location_financial_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['LocationFinancial_Availability','LocationFinancial_Discount_On_Crewsize','LocationFinancial_Discount_On_Shoot_Length','LocationFinancial_Location_Id','LocationFinancial_Monthly_Rate_Crewsize1','LocationFinancial_Monthly_Rate_Crewsize2','LocationFinancial_Monthly_Rate_Crewsize3','LocationFinancial_Monthly_Rate_Crewsize4','LocationFinancial_One_Day_Rent_Crewsize1','LocationFinancial_One_Day_Rent_Crewsize2','LocationFinancial_One_Day_Rent_Crewsize3','LocationFinancial_One_Day_Rent_Crewsize4',   'LocationFinancial_Prices_Available','LocationFinancial_Student_Rate','LocationFinancial_Weekly_Rate_Crewsize1','LocationFinancial_Weekly_Rate_Crewsize2','LocationFinancial_Weekly_Rate_Crewsize3','LocationFinancial_Weekly_Rate_Crewsize4',]

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.LocationFinancial_Creator = self.request.user
        return super().form_valid(form)

# LocationFinancial Details Here


class LocationFinancialDetailView(LoginRequiredMixin, DetailView):
    model = models.LocationFinancial
    context_object_name = 'LocationFinancial'
    template_name = 'location_financial/location_financial_detail.html'
    login_url = 'login'

# LocationFinancial ListView Here


class LocationFinancialListView(ListView):
    model = models.LocationFinancial
    context_object_name = 'LocationFinancial'
    template_name = 'location_financial/location_financial_list.html'
    login_url = 'login'

# LocationFinancial Update Here


class LocationFinancialUpdateView(LoginRequiredMixin, UpdateView):
    model = models.LocationFinancial
    context_object_name = 'LocationFinancial'

    # Decide fields for editing Here

    fields = ['LocationFinancial_Availability','LocationFinancial_Discount_On_Crewsize','LocationFinancial_Discount_On_Shoot_Length','LocationFinancial_Location_Id','LocationFinancial_Monthly_Rate_Crewsize1','LocationFinancial_Monthly_Rate_Crewsize2','LocationFinancial_Monthly_Rate_Crewsize3','LocationFinancial_Monthly_Rate_Crewsize4','LocationFinancial_One_Day_Rent_Crewsize1','LocationFinancial_One_Day_Rent_Crewsize2','LocationFinancial_One_Day_Rent_Crewsize3','LocationFinancial_One_Day_Rent_Crewsize4','LocationFinancial_Prices_Available','LocationFinancial_Student_Rate','LocationFinancial_Weekly_Rate_Crewsize1','LocationFinancial_Weekly_Rate_Crewsize2','LocationFinancial_Weekly_Rate_Crewsize3','LocationFinancial_Weekly_Rate_Crewsize4']

    template_name = 'location_financial/location_financial_update.html'
    login_url = 'login'

# LocationFinancial Delete here


class LocationFinancialDeleteView(LoginRequiredMixin, DeleteView):
    model = models.LocationFinancial
    template_name = 'location_financial/location_financial_delete.html'
    success_url = reverse_lazy('location_financial_list')
    login_url = 'login'
