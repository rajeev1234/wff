# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create helpcenter Here

class HelpCenterCreateView(LoginRequiredMixin, CreateView):
    model = models.HelpCenter
    template_name = 'helpcenter/helpcenter_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Help_Center_Help_Name','Help_Center_Help_Id','Help_Center_Creator',]

    # Set fields from current data or automated data


    def form_valid(self, form):
        form.instance.helpcenter_Author = self.request.user
        return super().form_valid(form)

# helpcenter Details Here


class HelpCenterDetailView(LoginRequiredMixin, DetailView):
    model = models.HelpCenter
    template_name = 'helpcenter/helpcenter_detail.html'
    login_url = 'login'

# helpcenter ListView Here


class HelpCenterListView(ListView):
    model = models.HelpCenter
    template_name = 'helpcenter/helpcenter_list.html'
    login_url = 'login'

# helpcenter Update Here


class HelpCenterUpdateView(LoginRequiredMixin, UpdateView):
    model = models.HelpCenter

    # Decide fields for editing Here

    fields = ['Help_Center_Help_Name','Help_Center_Help_Id','Help_Center_Creator',]
    template_name = 'helpcenter/helpcenter_update.html'
    login_url = 'login'

# helpcenter Delete here


class HelpCenterDeleteView(LoginRequiredMixin, DeleteView):
    model = models.HelpCenter
    template_name = 'helpcenter/helpcenter_delete.html'
    success_url = reverse_lazy('helpcenter_list')
    login_url = 'login'



