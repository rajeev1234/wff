# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create client Here

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = models.Client
    template_name = 'client/client_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Client_Contact_Person',
'Client_Contact_Person_Designation',
'Client_Contact_Person_Email',
'Client_Contact_Person_Number',
'Client_Production_House_City_Address',
'Client_Production_House_Name',
'Client_Production_House_Street_Addrerss',
]

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.Client_Contact_Person = self.request.user
        return super().form_valid(form)

# client Details Here


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = models.Client
    template_name = 'client/client_detail.html'
    login_url = 'login'

# client ListView Here


class ClientListView(ListView):
    model = models.Client
    template_name = 'client/client_list.html'
    login_url = 'login'

# client Update Here


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Client

    # Decide fields for editing Here

    
    fields = ['Client_Contact_Person',
'Client_Contact_Person_Designation',
'Client_Contact_Person_Email',
'Client_Contact_Person_Number',
'Client_Production_House_City_Address',
'Client_Production_House_Name',
'Client_Production_House_Street_Addrerss',
]
    template_name = 'client/client_update.html'
    login_url = 'login'

# client Delete here


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Client
    template_name = 'client/client_delete.html'
    success_url = reverse_lazy('client_list')
    login_url = 'login'



