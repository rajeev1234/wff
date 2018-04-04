# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create contactmessages Here

class ContactMessagesCreateView(LoginRequiredMixin, CreateView):
    model = models.ContactMessages
    template_name = 'contactmessages/contactmessages_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['ContactMessages_Address',
'ContactMessages_Camera_Model',
'ContactMessages_City_State_Country',
'ContactMessages_Company_Name',
'ContactMessages_Email',
'ContactMessages_From_Page',
'ContactMessages_From_Resource',
'ContactMessages_Full_Name',
'ContactMessages_Message',
'ContactMessages_Phone_Number',
'ContactMessages_Profile']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.ContactMessages_Address = self.request.user
        return super().form_valid(form)

# contactmessages Details Here


class ContactMessagesDetailView(LoginRequiredMixin, DetailView):
    model = models.ContactMessages
    template_name = 'contactmessages/contactmessages_detail.html'
    login_url = 'login'

# contactmessages ListView Here


class ContactMessagesListView(ListView):
    model = models.ContactMessages
    template_name = 'contactmessages/contactmessages_list.html'
    login_url = 'login'

# contactmessages Update Here


class ContactMessagesUpdateView(LoginRequiredMixin, UpdateView):
    model = models.ContactMessages

    # Decide fields for editing Here

    fields = ['ContactMessages_Address',
'ContactMessages_Camera_Model',
'ContactMessages_City_State_Country',
'ContactMessages_Company_Name',
'ContactMessages_Email',
'ContactMessages_From_Page',
'ContactMessages_From_Resource',
'ContactMessages_Full_Name',
'ContactMessages_Message',
'ContactMessages_Phone_Number',
'ContactMessages_Profile']

    template_name = 'contactmessages/contactmessages_update.html'
    login_url = 'login'

# contactmessages Delete here


class ContactMessagesDeleteView(LoginRequiredMixin, DeleteView):
    model = models.ContactMessages
    template_name = 'contactmessages/contactmessages_delete.html'
    success_url = reverse_lazy('contactmessages_list')
    login_url = 'login'



