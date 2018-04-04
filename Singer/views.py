# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create Singer Here

class SingerCreateView(LoginRequiredMixin, CreateView):
    model = models.Singer
    template_name = 'Singer/Singer_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = [
            # 'Singer_Comments',
            'Singer_Daily_Charges',
            'Singer_Description',
            'Singer_Financials_Available',
            'Singer_Genre',
            # 'Singer_Languages',
            # 'Singer_Portfolio',
            # 'Singer_Profile_Projects',
            # 'Singer_Ratings',
            # 'Singer_Scale_Rate',
            # 'Singing_Style',
            # 'Singer_Video',
            ]

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.Singer_Author = self.request.user
        return super().form_valid(form)

# Singer Details Here


class SingerDetailView(LoginRequiredMixin, DetailView):
    model = models.Singer
    context_object_name = 'Singer'
    template_name = 'Singer/Singer_details.html'
    login_url = 'login'

# Singer ListView Here


class SingerListView(ListView):
    model = models.Singer
    template_name = 'Singer/Singer_list.html'
    login_url = 'login'

# Singer Update Here


class SingerUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Singer

    # Decide fields for editing Here

    fields = [
            # 'Singer_Comments',
            'Singer_Daily_Charges',
            'Singer_Description',
            'Singer_Financials_Available',
            'Singer_Genre',
            # 'Singer_Languages',
            # 'Singer_Portfolio',
            # 'Singer_Profile_Projects',
            # 'Singer_Ratings',
            # 'Singer_Scale_Rate',
            # 'Singing_Style',
            # 'Singer_Video',
            ]

    template_name = 'Singer/Singer_update.html'
    login_url = 'login'

# Singer Delete here


class SingerDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Singer
    template_name = 'Singer/Singer_delete.html'
    success_url = reverse_lazy('Singer_list')
    login_url = 'login'



