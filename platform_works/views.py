# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create platform_works Here

class PlatformWorksCreateView(LoginRequiredMixin, CreateView):
    model = models.PlatformWorks
    template_name = 'platform_works/platform_works_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['PlatformWorks_Client_Name','PlatformWorks_Project_Name','PlatformWorks_Project_Details']

    # Set fields from current data or automated data
    #
    def form_valid(self, form):
        form.instance.PlatformWorks_Author = self.request.user
        return super().form_valid(form)

# platform_works Details Here


class PlatformWorksDetailView(LoginRequiredMixin, DetailView):
    model = models.PlatformWorks
    context_object_name = 'PlatformWorks'
    template_name = 'platform_works/platform_works_detail.html'
    login_url = 'login'

# platform_works ListView Here


class PlatformWorksListView(ListView):
    model = models.PlatformWorks
    template_name = 'platform_works/platform_works_list.html'
    login_url = 'login'

# platform_works Update Here


class PlatformWorksUpdateView(LoginRequiredMixin, UpdateView):
    model = models.PlatformWorks

    # Decide fields for editing Here

    fields = ['PlatformWorks_Client_Name','PlatformWorks_Project_Name','PlatformWorks_Project_Details']
    template_name = 'platform_works/platform_works_update.html'
    login_url = 'login'

# platform_works Delete here


class PlatformWorksDeleteView(LoginRequiredMixin, DeleteView):
    model = models.PlatformWorks
    template_name = 'platform_works/platform_works_delete.html'
    success_url = reverse_lazy('platform_works_list')
    login_url = 'login'
