# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create userprofessionalinfo Here

class UserProfessionalInfoCreateView(LoginRequiredMixin, CreateView):
    model = models.UserProfessionalInfo
    template_name = 'userprofessionalinfo/userprofessionalinfo_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['UserProfessionalInfo_Account_Name',
'UserProfessionalInfo_Account_Number',
'UserProfessionalInfo_Bank_Name',
'UserProfessionalInfo_Bank_Account',
'UserProfessionalInfo_Charges_Negotiation',
'UserProfessionalInfo_Daily_Charges',
'UserProfessionalInfo_Expirienced',
'UserProfessionalInfo_Hometown',
'UserProfessionalInfo_IFSI_CODE',
'UserProfessionalInfo_Monthly_Charges',
'UserProfessionalInfo_Rates_Avialability',
'UserProfessionalInfo_User_Proffessional_Category',
'UserProfessionalInfo_Weekly_Charges',
'UserProfessionalInfo_Writtable_Language',
'UserProfessionalInfo_Years_Of_Experience']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.UserProfessionalInfo_Account_Name = self.request.user
        return super().form_valid(form)

# userprofessionalinfo Details Here


class UserProfessionalInfoDetailView(LoginRequiredMixin, DetailView):
    model = models.UserProfessionalInfo
    template_name = 'userprofessionalinfo/userprofessionalinfo_detail.html'
    login_url = 'login'

# userprofessionalinfo ListView Here


class UserProfessionalInfoListView(ListView):
    model = models.UserProfessionalInfo
    template_name = 'userprofessionalinfo/userprofessionalinfo_list.html'
    login_url = 'login'

# userprofessionalinfo Update Here


class UserProfessionalInfoUpdateView(LoginRequiredMixin, UpdateView):
    model = models.UserProfessionalInfo

    # Decide fields for editing Here

    fields = ['UserProfessionalInfo_Account_Name',
'UserProfessionalInfo_Account_Number',
'UserProfessionalInfo_Bank_Name',
'UserProfessionalInfo_Bank_Account',
'UserProfessionalInfo_Charges_Negotiation',
'UserProfessionalInfo_Daily_Charges',
'UserProfessionalInfo_Expirienced',
'UserProfessionalInfo_Hometown',
'UserProfessionalInfo_IFSI_CODE',
'UserProfessionalInfo_Monthly_Charges',
'UserProfessionalInfo_Rates_Avialability',
'UserProfessionalInfo_User_Proffessional_Category',
'UserProfessionalInfo_Weekly_Charges',
'UserProfessionalInfo_Writtable_Language',
'UserProfessionalInfo_Years_Of_Experience']

    template_name = 'userprofessionalinfo/userprofessionalinfo_update.html'
    login_url = 'login'

# userprofessionalinfo Delete here


class UserProfessionalInfoDeleteView(LoginRequiredMixin, DeleteView):
    model = models.UserProfessionalInfo
    template_name = 'userprofessionalinfo/userprofessionalinfo_delete.html'
    success_url = reverse_lazy('userprofessionalinfo_list')
    login_url = 'login'



