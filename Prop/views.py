# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create Prop Here

class PropCreateView(LoginRequiredMixin, CreateView):
    model = models.Prop
    template_name = 'Prop/Prop_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Prop_Color','Prop_Daily_Rent','Prop_Modification_Allowed','Prop_Ownership_Status','Prop_ID','Prop_Make','Prop_Type','Prop_Weekly_Rent']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.Prop_Author = self.request.user
        return super().form_valid(form)

# Prop Details Here


class PropDetailView(LoginRequiredMixin, DetailView):
    model = models.Prop
    template_name = 'Prop/Prop_detail.html'
    login_url = 'login'

# Prop ListView Here


class PropListView(ListView):
    model = models.Prop
    template_name = 'Prop/Prop_list.html'
    login_url = 'login'

# Prop Update Here


class PropUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Prop

    # Decide fields for editing Here

    fields = ['Prop_Color','Prop_Daily_Rent','Prop_Modification_Allowed','Prop_Ownership_Status','Prop_ID','Prop_Make','Prop_Type','Prop_Weekly_Rent']
    template_name = 'Prop/Prop_update.html'
    login_url = 'login'

# Prop Delete here


class PropDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Prop
    template_name = 'Prop/Prop_delete.html'
    success_url = reverse_lazy('Prop_list')
    login_url = 'login'



