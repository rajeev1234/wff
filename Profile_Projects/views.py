# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create profile_projects Here

class profile_projectsCreateView(LoginRequiredMixin, CreateView):
    model = models.profile_projects
    template_name = 'profile_projects/profile_projects_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Category','Director','Production_House','Title','profile_projects_Message']

    # Set fields from current data or automated data
    #
    def form_valid(self, form):
        form.instance.profile_projects_Author = self.request.user
        return super().form_valid(form)

# profile_projects Details Here


class profile_projectsDetailView(LoginRequiredMixin, DetailView):
    model = models.profile_projects
    template_name = 'profile_projects/profile_projects_detail.html'
    login_url = 'login'

# profile_projects ListView Here


class profile_projectsListView(ListView):
    model = models.profile_projects
    template_name = 'profile_projects/profile_projects_list.html'
    login_url = 'login'

# profile_projects Update Here


class profile_projectsUpdateView(LoginRequiredMixin, UpdateView):
    model = models.profile_projects

    # Decide fields for editing Here

    fields = ['Category','Director','Production_House','Title','profile_projects_Message']
    template_name = 'profile_projects/profile_projects_update.html'
    login_url = 'login'

# profile_projects Delete here


class profile_projectsDeleteView(LoginRequiredMixin, DeleteView):
    model = models.profile_projects
    template_name = 'profile_projects/profile_projects_delete.html'
    success_url = reverse_lazy('profile_projects_list')
    login_url = 'login'



