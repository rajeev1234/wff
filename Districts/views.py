# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create District Here

class DistrictCreateView(LoginRequiredMixin, CreateView):
    model = models.District
    template_name = 'Districts/District_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = [
                'District_Code',
                'District_Complete',
                'District_Name',
                'District_Email',
                'District_Headquater',
                'District_Phq',
                'District_Phq_Email',
                'District_Phq_Postal_Address',
                'District_Phq_Web',
                'District_Police_Hqaddress',
                'District_Postal_Address',
                'District_State',
                'District_Web_Address',
                'District_Creator']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.District_Author = self.request.user
        return super().form_valid(form)

# District Details Here


class DistrictDetailView(LoginRequiredMixin, DetailView):
    model = models.District
    context_object_name = 'District'
    template_name = 'Districts/District_details.html'
    login_url = 'login'

# District ListView Here


class DistrictListView(ListView):
    model = models.District
    template_name = 'Districts/District_list.html'
    login_url = 'login'

# District Update Here


class DistrictUpdateView(LoginRequiredMixin, UpdateView):
    model = models.District

    # Decide fields for editing Here

    fields = [
                'District_Code',
                'District_Complete',
                'District_Name',
                'District_Email',
                'District_Headquater',
                'District_Phq',
                'District_Phq_Email',
                'District_Phq_Postal_Address',
                'District_Phq_Web',
                'District_Police_Hqaddress',
                'District_Postal_Address',
                'District_State',
                'District_Web_Address',
                'District_Creator']
                
    template_name = 'Districts/District_update.html'
    login_url = 'login'

# District Delete here


class DistrictDeleteView(LoginRequiredMixin, DeleteView):
    model = models.District
    template_name = 'Districts/District_delete.html'
    success_url = reverse_lazy('District_list')
    login_url = 'login'



