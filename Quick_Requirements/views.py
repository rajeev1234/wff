# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create Quick_Requirements Here

class Quick_RequirementsCreateView(LoginRequiredMixin, CreateView):
    model = models.Quick_Requirements
    template_name = 'Quick_Requirements/Quick_Requirements_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Quick_Requirements_Crew_Size','Quick_Requirements_From_User','Quick_Requirements_New_Requirement','Quick_Requirements_Recipient','Quick_Requirements_Requirement_Description','Quick_Requirements_Shoot_Category','Quick_Requirements_Shooting_Region','Quick_Requirements_Tentative_Dates','Quick_Requirements_Creator']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.Quick_Requirements_Author = self.request.user
        return super().form_valid(form)

# Quick_Requirements Details Here


class Quick_RequirementsDetailView(LoginRequiredMixin, DetailView):
    model = models.Quick_Requirements
    template_name = 'Quick_Requirements/Quick_Requirements_detail.html'
    login_url = 'login'

# Quick_Requirements ListView Here


class Quick_RequirementsListView(ListView):
    model = models.Quick_Requirements
    template_name = 'Quick_Requirements/Quick_Requirements_list.html'
    login_url = 'login'

# Quick_Requirements Update Here


class Quick_RequirementsUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Quick_Requirements

    # Decide fields for editing Here

    fields = ['Quick_Requirements_Crew_Size','Quick_Requirements_From_User','Quick_Requirements_New_Requirement','Quick_Requirements_Recipient','Quick_Requirements_Requirement_Description','Quick_Requirements_Shoot_Category','Quick_Requirements_Shooting_Region','Quick_Requirements_Tentative_Dates','Quick_Requirements_Creator']

    template_name = 'Quick_Requirements/Quick_Requirements_update.html'
    login_url = 'login'

# Quick_Requirements Delete here


class Quick_RequirementsDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Quick_Requirements
    template_name = 'Quick_Requirements/Quick_Requirements_delete.html'
    success_url = reverse_lazy('Quick_Requirements_list')
    login_url = 'login'



