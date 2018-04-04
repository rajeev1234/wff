# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create permit_query Here

class PermitQueryCreateView(LoginRequiredMixin, CreateView):
    model = models.PermitQuery
    template_name = 'permit_query/permit_query_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['PermitQuery_API_Address','PermitQuery_City_State_Country','PermitQuery_Latitude','PermitQuery_Location','PermitQuery_Longitude','PermitQuery_Map_Address','Permit_Query_Number','PermitQuery_Query_Mode','PermitQuery_Street_Address']

    # Set fields from current data or automated data
    #
    def form_valid(self, form):
        form.instance.PermitQuery_Author = self.request.user
        return super().form_valid(form)

# permit_query Details Here


class PermitQueryDetailView(LoginRequiredMixin, DetailView):
    model = models.PermitQuery
    context_object_name = 'PermitQuery'
    template_name = 'permit_query/permit_query_detail.html'
    login_url = 'login'

# permit_query ListView Here


class PermitQueryListView(ListView):
    model = models.PermitQuery
    template_name = 'permit_query/permit_query_list.html'
    login_url = 'login'

# permit_query Update Here


class PermitQueryUpdateView(LoginRequiredMixin, UpdateView):
    model = models.PermitQuery

    # Decide fields for editing Here

    fields = ['PermitQuery_API_Address','PermitQuery_City_State_Country','PermitQuery_Latitude','PermitQuery_Location','PermitQuery_Longitude','PermitQuery_Map_Address','Permit_Query_Number','PermitQuery_Query_Mode','PermitQuery_Street_Address']
    template_name = 'permit_query/permit_query_update.html'
    login_url = 'login'

# permit_query Delete here


class PermitQueryDeleteView(LoginRequiredMixin, DeleteView):
    model = models.PermitQuery
    template_name = 'permit_query/permit_query_delete.html'
    success_url = reverse_lazy('permit_query_list')
    login_url = 'login'
