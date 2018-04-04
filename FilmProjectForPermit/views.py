# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create FilmProjectForPermit Here

class FilmProjectForPermitCreateView(LoginRequiredMixin, CreateView):
    model = models.FilmProjectForPermit
    template_name = 'FilmProjectForPermits/FilmProjectForPermit_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = [
            # 'FilmProjectForPermit_Cast',
            'FilmProjectForPermit_Category',
            'FilmProjectForPermit_Crew_Size',
            # 'FilmProjectForPermit_PermitLocationList',
            'FilmProjectForPermit_Project_Name',
            'FilmProjectForPermit_ScriptasFile',
            'FilmProjectForPermit_Synopsis',
            'FilmProjectForPermit_Title',
            'FilmProjectForPermit_Creator'
            ]

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.FilmProjectForPermit_Author = self.request.user
        return super().form_valid(form)

# FilmProjectForPermit Details Here


class FilmProjectForPermitDetailView(LoginRequiredMixin, DetailView):
    model = models.FilmProjectForPermit
    context_object_name = 'FilmProjectForPermit'
    template_name = 'FilmProjectForPermits/FilmProjectForPermit_details.html'
    login_url = 'login'

# FilmProjectForPermit ListView Here


class FilmProjectForPermitListView(ListView):
    model = models.FilmProjectForPermit
    template_name = 'FilmProjectForPermits/FilmProjectForPermit_list.html'
    login_url = 'login'

# FilmProjectForPermit Update Here


class FilmProjectForPermitUpdateView(LoginRequiredMixin, UpdateView):
    model = models.FilmProjectForPermit

    # Decide fields for editing Here


    fields = [
            # 'FilmProjectForPermit_Cast',
            'FilmProjectForPermit_Category',
            'FilmProjectForPermit_Crew_Size',
            # 'FilmProjectForPermit_PermitLocationList',
            'FilmProjectForPermit_Project_Name',
            'FilmProjectForPermit_ScriptasFile',
            'FilmProjectForPermit_Synopsis',
            'FilmProjectForPermit_Title',
            'FilmProjectForPermit_Creator'
            ]

    template_name = 'FilmProjectForPermits/FilmProjectForPermit_update.html'
    login_url = 'login'

# FilmProjectForPermit Delete here


class FilmProjectForPermitDeleteView(LoginRequiredMixin, DeleteView):
    model = models.FilmProjectForPermit
    template_name = 'FilmProjectForPermits/FilmProjectForPermit_delete.html'
    success_url = reverse_lazy('FilmProjectForPermit_list')
    login_url = 'login'



