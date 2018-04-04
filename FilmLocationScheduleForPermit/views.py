# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create FilmLocationScheduleForPermit Here

class FilmLocationScheduleForPermitCreateView(LoginRequiredMixin, CreateView):
    model = models.FilmLocationScheduleForPermit
    template_name = 'FilmLocationScheduleForPermits/FilmLocationScheduleForPermit_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = [
            'FilmLocationScheduleForPermit_Location',
            # 'FilmLocationScheduleForPermit_ProjectID',
            'FilmLocationScheduleForPermit_SNo',
            # 'FilmLocationScheduleForPermit_Shooting_Date',
            'FilmLocationScheduleForPermit_Creator',
            ]

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.FilmLocationScheduleForPermit_Author = self.request.user
        return super().form_valid(form)

# FilmLocationScheduleForPermit Details Here


class FilmLocationScheduleForPermitDetailView(LoginRequiredMixin, DetailView):
    model = models.FilmLocationScheduleForPermit
    context_object_name = 'FilmLocationScheduleForPermit'
    template_name = 'FilmLocationScheduleForPermits/FilmLocationScheduleForPermit_details.html'
    login_url = 'login'

# FilmLocationScheduleForPermit ListView Here


class FilmLocationScheduleForPermitListView(ListView):
    model = models.FilmLocationScheduleForPermit
    template_name = 'FilmLocationScheduleForPermits/FilmLocationScheduleForPermit_list.html'
    login_url = 'login'

# FilmLocationScheduleForPermit Update Here


class FilmLocationScheduleForPermitUpdateView(LoginRequiredMixin, UpdateView):
    model = models.FilmLocationScheduleForPermit

    # Decide fields for editing Here


    fields = [
            'FilmLocationScheduleForPermit_Location',
            # 'FilmLocationScheduleForPermit_ProjectID',
            'FilmLocationScheduleForPermit_SNo',
            # 'FilmLocationScheduleForPermit_Shooting_Date',
            'FilmLocationScheduleForPermit_Creator',
            ]
            
    template_name = 'FilmLocationScheduleForPermits/FilmLocationScheduleForPermit_update.html'
    login_url = 'login'

# FilmLocationScheduleForPermit Delete here


class FilmLocationScheduleForPermitDeleteView(LoginRequiredMixin, DeleteView):
    model = models.FilmLocationScheduleForPermit
    template_name = 'FilmLocationScheduleForPermits/FilmLocationScheduleForPermit_delete.html'
    success_url = reverse_lazy('FilmLocationScheduleForPermit_list')
    login_url = 'login'



