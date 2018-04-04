# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create officer_contact Here

class OfficerContactCreateView(LoginRequiredMixin, CreateView):
    model = models.OfficerContact
    template_name = 'officer_contact/officer_contact_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['OfficerContact_CONTACT_NUMBER','OfficerContact_DEPARTMENT','OfficerContact_DESIGNATIONS','OfficerContact_E_Mail','OfficerContact_Name']

    # Set fields from current data or automated data
    #
    def form_valid(self, form):
        form.instance.OfficerContact_Author = self.request.user
        return super().form_valid(form)

# officer_contact Details Here


class OfficerContactDetailView(LoginRequiredMixin, DetailView):
    model = models.OfficerContact
    context_object_name = 'OfficerContact'
    template_name = 'officer_contact/officer_contact_detail.html'
    login_url = 'login'

# officer_contact ListView Here


class OfficerContactListView(ListView):
    model = models.OfficerContact
    template_name = 'officer_contact/officer_contact_list.html'
    login_url = 'login'

# officer_contact Update Here


class OfficerContactUpdateView(LoginRequiredMixin, UpdateView):
    model = models.OfficerContact

    # Decide fields for editing Here

    fields = ['OfficerContact_CONTACT_NUMBER','OfficerContact_DEPARTMENT','OfficerContact_DESIGNATIONS','OfficerContact_E_Mail','OfficerContact_Name']
    template_name = 'officer_contact/officer_contact_update.html'
    login_url = 'login'

# officer_contact Delete here


class OfficerContactDeleteView(LoginRequiredMixin, DeleteView):
    model = models.OfficerContact
    template_name = 'officer_contact/officer_contact_delete.html'
    success_url = reverse_lazy('officer_contact_list')
    login_url = 'login'
