# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create subcription_plan Here

class subcription_planCreateView(LoginRequiredMixin, CreateView):
    model = models.subcription_plan
    template_name = 'subcription_plan/subcription_plan_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Amount','End_Date','FOR_FILM_COIN','Location_Allowed','Openings_Allowed','Pitch_Allowed','Pitch_Box_Capacity_Image_per_pitch','Start_Date','Type','subcription_plan_Message']

    # Set fields from current data or automated data
    #
    def form_valid(self, form):
        form.instance.subcription_plan_Author = self.request.user
        return super().form_valid(form)

# subcription_plan Details Here


class subcription_planDetailView(LoginRequiredMixin, DetailView):
    model = models.subcription_plan
    template_name = 'subcription_plan/subcription_plan_detail.html'
    login_url = 'login'

# subcription_plan ListView Here


class subcription_planListView(ListView):
    model = models.subcription_plan
    template_name = 'subcription_plan/subcription_plan_list.html'
    login_url = 'login'

# subcription_plan Update Here


class subcription_planUpdateView(LoginRequiredMixin, UpdateView):
    model = models.subcription_plan

    # Decide fields for editing Here

    fields = ['Amount','End_Date','FOR_FILM_COIN','Location_Allowed','Openings_Allowed','Pitch_Allowed','Pitch_Box_Capacity_Image_per_pitch','Start_Date','Type','subcription_plan_Message']
    template_name = 'subcription_plan/subcription_plan_update.html'
    login_url = 'login'

# subcription_plan Delete here


class subcription_planDeleteView(LoginRequiredMixin, DeleteView):
    model = models.subcription_plan
    template_name = 'subcription_plan/subcription_plan_delete.html'
    success_url = reverse_lazy('subcription_plan_list')
    login_url = 'login'



