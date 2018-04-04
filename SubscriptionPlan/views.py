# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create SubscriptionPlan Here

class SubscriptionPlanCreateView(LoginRequiredMixin, CreateView):
    model = models.SubscriptionPlan
    template_name = 'SubscriptionPlans/SubscriptionPlan_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = [
            'SubscriptionPlan_Amount',
            'SubscriptionPlan_End_Date',
            'SubscriptionPlan_FOR_FILM_COIN',
            'SubscriptionPlan_Location_Allowed',
            'SubscriptionPlan_Openings_Allowed',
            'SubscriptionPlan_Pitch_Allowed',
            'SubscriptionPlan_Pitch_Box_Capacity_Image_per_pitch',
            'SubscriptionPlan_Type',
            'SubscriptionPlan_User_ID',

          ]

    # Set fields from current data or automated data

    def form_valid(self, form):
        # form.instance.SubscriptionPlan_Author = self.request.user
        return super().form_valid(form)

# SubscriptionPlan Details Here


class SubscriptionPlanDetailView(LoginRequiredMixin, DetailView):
    model = models.SubscriptionPlan
    context_object_name = 'SubscriptionPlan'
    template_name = 'SubscriptionPlans/SubscriptionPlan_details.html'
    login_url = 'login'

# SubscriptionPlan ListView Here


class SubscriptionPlanListView(ListView):
    model = models.SubscriptionPlan
    template_name = 'SubscriptionPlans/SubscriptionPlan_list.html'
    login_url = 'login'

# SubscriptionPlan Update Here


class SubscriptionPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = models.SubscriptionPlan

    # Decide fields for editing Here

    fields = [
            'SubscriptionPlan_Amount',
            'SubscriptionPlan_End_Date',
            'SubscriptionPlan_FOR_FILM_COIN',
            'SubscriptionPlan_Location_Allowed',
            'SubscriptionPlan_Openings_Allowed',
            'SubscriptionPlan_Pitch_Allowed',
            'SubscriptionPlan_Pitch_Box_Capacity_Image_per_pitch',
            'SubscriptionPlan_Type',
            'SubscriptionPlan_User_ID',

          ]


    template_name = 'SubscriptionPlans/SubscriptionPlan_update.html'
    login_url = 'login'

# SubscriptionPlan Delete here


class SubscriptionPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = models.SubscriptionPlan
    template_name = 'SubscriptionPlans/SubscriptionPlan_delete.html'
    success_url = reverse_lazy('SubscriptionPlan_list')
    login_url = 'login'