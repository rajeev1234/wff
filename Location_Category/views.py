# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create Location_Category Here

class Location_CategoryCreateView(LoginRequiredMixin, CreateView):
    model = models.Location_Category
    template_name = 'Location_Category/Location_Category_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Location_Category_No','Location_Category_Name','Location_Category_Creator']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.Location_Category_Author = self.request.user
        return super().form_valid(form)

# Location_Category Details Here


class Location_CategoryDetailView(LoginRequiredMixin, DetailView):
    model = models.Location_Category
    template_name = 'Location_Category/Location_Category_detail.html'
    login_url = 'login'

# Location_Category ListView Here


class Location_CategoryListView(ListView):
    model = models.Location_Category
    template_name = 'Location_Category/Location_Category_list.html'
    login_url = 'login'

# Location_Category Update Here


class Location_CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Location_Category

    # Decide fields for editing Here

    fields = ['Location_Category_No','Location_Category_Name','Location_Category_Creator']
    template_name = 'Location_Category/Location_Category_update.html'
    login_url = 'login'

# Location_Category Delete here


class Location_CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Location_Category
    template_name = 'Location_Category/Location_Category_delete.html'
    success_url = reverse_lazy('Location_Category_list')
    login_url = 'login'



