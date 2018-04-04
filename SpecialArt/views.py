# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create SpecialArt Here

class SpecialArtCreateView(LoginRequiredMixin, CreateView):
    model = models.SpecialArt
    template_name = 'SpecialArt/SpecialArt_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = [
            'SpecialArt_Charges_Available',
            # 'SpecialArt_Comments',
            'SpecialArt_Daily_Charges',
            'SpecialArt_Description',
            # 'SpecialArt_Portfolio',
            # 'SpecialArt_Profile_Projects',
            # 'SpecialArt_Ratings',
            'SpecialArt_Special_Art_ID',
            # 'SpecialArt_Video',
            ]

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.SpecialArt_Author = self.request.user
        return super().form_valid(form)

# SpecialArt Details Here


class SpecialArtDetailView(LoginRequiredMixin, DetailView):
    model = models.SpecialArt
    context_object_name = 'SpecialArt'
    template_name = 'SpecialArt/SpecialArt_details.html'
    login_url = 'login'

# SpecialArt ListView Here


class SpecialArtListView(ListView):
    model = models.SpecialArt
    template_name = 'SpecialArt/SpecialArt_list.html'
    login_url = 'login'

# SpecialArt Update Here


class SpecialArtUpdateView(LoginRequiredMixin, UpdateView):
    model = models.SpecialArt

    # Decide fields for editing Here

    fields = [
            'SpecialArt_Charges_Available',
            # 'SpecialArt_Comments',
            'SpecialArt_Daily_Charges',
            'SpecialArt_Description',
            # 'SpecialArt_Portfolio',
            # 'SpecialArt_Profile_Projects',
            # 'SpecialArt_Ratings',
            'SpecialArt_Special_Art_ID',
            # 'SpecialArt_Video',
            ]



    template_name = 'SpecialArt/SpecialArt_update.html'
    login_url = 'login'

# SpecialArt Delete here


class SpecialArtDeleteView(LoginRequiredMixin, DeleteView):
    model = models.SpecialArt
    template_name = 'SpecialArt/SpecialArt_delete.html'
    success_url = reverse_lazy('SpecialArt_list')
    login_url = 'login'



