# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create TalentProfile Here

class TalentProfileCreateView(LoginRequiredMixin, CreateView):
    model = models.TalentProfile
    template_name = 'TalentProfiles/TalentProfile_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = [
            'TalentProfile_Actor',
            'TalentProfile_Child_Artist',
            'TalentProfile_Dancer',
            'TalentProfile_Mimicry_Artist',
            'TalentProfile_Musician',
            'TalentProfile_Profile_Talent',
            'TalentProfile_Singer',
            'TalentProfile_Special_Art',
            'TalentProfile_Theater_Artist',
            'TalentProfile_Voice_Over_Artist',
            ]

    # Set fields from current data or automated data

    def form_valid(self, form):
        # form.instance.TalentProfile_Author = self.request.user
        return super().form_valid(form)

# TalentProfile Details Here


class TalentProfileDetailView(LoginRequiredMixin, DetailView):
    model = models.TalentProfile
    context_object_name = 'TalentProfile'
    template_name = 'TalentProfiles/TalentProfile_details.html'
    login_url = 'login'

# TalentProfile ListView Here


class TalentProfileListView(ListView):
    model = models.TalentProfile
    template_name = 'TalentProfiles/TalentProfile_list.html'
    login_url = 'login'

# TalentProfile Update Here


class TalentProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = models.TalentProfile

    # Decide fields for editing Here

    fields = [
            'TalentProfile_Actor',
            'TalentProfile_Child_Artist',
            'TalentProfile_Dancer',
            'TalentProfile_Mimicry_Artist',
            'TalentProfile_Musician',
            'TalentProfile_Profile_Talent',
            'TalentProfile_Singer',
            'TalentProfile_Special_Art',
            'TalentProfile_Theater_Artist',
            'TalentProfile_Voice_Over_Artist',
            ]

    template_name = 'TalentProfiles/TalentProfile_update.html'
    login_url = 'login'

# TalentProfile Delete here


class TalentProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = models.TalentProfile
    template_name = 'TalentProfiles/TalentProfile_delete.html'
    success_url = reverse_lazy('TalentProfile_list')
    login_url = 'login'