# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create ServiceCatagory Here

class ServiceCatagoryCreateView(LoginRequiredMixin, CreateView):
    model = models.ServiceCatagory
    template_name = 'ServiceCatagory/ServiceCatagory_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = [
            'ServiceCatagory_Icon_Number',
            'ServiceCatagory_Image',
            'ServiceCatagory_Responsibilities',
            # 'ServiceCatagory_guidedlocation_List'
            'ServiceCatagory_Service_Category',
            # 'ServiceCatagory_Service_Subcategory',
            'ServiceCatagory_Users',
            'ServiceCatagory_What_Do_You_Do',
            ]


    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.ServiceCatagory_Author = self.request.user
        return super().form_valid(form)

# ServiceCatagory Details Here


class ServiceCatagoryDetailView(LoginRequiredMixin, DetailView):
    model = models.ServiceCatagory
    context_object_name = 'ServiceCatagory'
    template_name = 'ServiceCatagory/ServiceCatagory_details.html'
    login_url = 'login'

# ServiceCatagory ListView Here


class ServiceCatagoryListView(ListView):
    model = models.ServiceCatagory
    template_name = 'ServiceCatagory/ServiceCatagory_list.html'
    login_url = 'login'

# ServiceCatagory Update Here


class ServiceCatagoryUpdateView(LoginRequiredMixin, UpdateView):
    model = models.ServiceCatagory

    # Decide fields for editing Here
    fields = [
            'ServiceCatagory_Icon_Number',
            'ServiceCatagory_Image',
            'ServiceCatagory_Responsibilities',
            # 'ServiceCatagory_guidedlocation_List'
            'ServiceCatagory_Service_Category',
            # 'ServiceCatagory_Service_Subcategory',
            'ServiceCatagory_Users',
            'ServiceCatagory_What_Do_You_Do',
            ]

    template_name = 'ServiceCatagory/ServiceCatagory_update.html'
    login_url = 'login'

# ServiceCatagory Delete here


class ServiceCatagoryDeleteView(LoginRequiredMixin, DeleteView):
    model = models.ServiceCatagory
    template_name = 'ServiceCatagory/ServiceCatagory_delete.html'
    success_url = reverse_lazy('ServiceCatagory_list')
    login_url = 'login'



