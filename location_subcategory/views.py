# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create location_subcategory Here

class LocationSubCategoryCreateView(LoginRequiredMixin, CreateView):
    model = models.LocationSubCategory
    template_name = 'location_subcategorys/location_subcategory_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['LocationSubCategory_Location_Category','Location_Subcategory','LocationSubCategory_Subcategory_No','LocationSubCategory_Message']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.LocationSubCategory_Author = self.request.user
        return super().form_valid(form)

# location_subcategory Details Here


class LocationSubCategoryDetailView(LoginRequiredMixin, DetailView):
    model = models.LocationSubCategory
    context_object_name = 'LocationSubCategory'
    template_name = 'location_subcategorys/location_subcategory_detail.html'
    login_url = 'login'

# location_subcategory ListView Here


class LocationSubCategoryListView(ListView):
    model = models.LocationSubCategory
    template_name = 'location_subcategorys/location_subcategory_list.html'
    login_url = 'login'

# location_subcategory Update Here


class LocationSubCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = models.LocationSubCategory

    # Decide fields for editing Here

    fields = ['LocationSubCategory_Location_Category','Location_Subcategory','LocationSubCategory_Subcategory_No','LocationSubCategory_Message']
    template_name = 'location_subcategorys/location_subcategory_update.html'
    login_url = 'login'

# location_subcategory Delete here


class LocationSubCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = models.LocationSubCategory
    template_name = 'location_subcategorys/location_subcategory_delete.html'
    success_url = reverse_lazy('location_subcategory_list')
    login_url = 'login'
