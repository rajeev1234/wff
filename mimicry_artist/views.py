# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create mimicry_artist Here

class MimicryArtistCreateView(LoginRequiredMixin, CreateView):
    model = models.MimicryArtist
    template_name = 'mimicry_artists/mimicry_artist_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['MimicryArtist_Daily_Financials', 'MimicryArtist_Description', 'MimicryArtist_Financials_Available', 'MimicryArtist_Voices', 'MimicryArtist_Author']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.MimicryArtist_Author = self.request.user
        return super().form_valid(form)

# mimicry_artist Details Here


class MimicryArtistDetailView(LoginRequiredMixin, DetailView):
    model = models.MimicryArtist
    context_object_name = 'MimicryArtist'
    template_name = 'mimicry_artists/mimicry_artist_detail.html'
    login_url = 'login'

# mimicry_artist ListView Here


class MimicryArtistListView(ListView):
    model = models.MimicryArtist
    template_name = 'mimicry_artists/mimicry_artist_list.html'
    login_url = 'login'

# mimicry_artist Update Here


class MimicryArtistUpdateView(LoginRequiredMixin, UpdateView):
    model = models.MimicryArtist

    # Decide fields for editing Here
    fields = ['MimicryArtist_Daily_Financials', 'MimicryArtist_Description', 'MimicryArtist_Financials_Available', 'MimicryArtist_Voices', 'MimicryArtist_Author']
    template_name = 'mimicry_artists/mimicry_artist_update.html'
    login_url = 'login'

# mimicry_artist Delete here


class MimicryArtistDeleteView(LoginRequiredMixin, DeleteView):
    model = models.MimicryArtist
    template_name = 'mimicry_artists/mimicry_artist_delete.html'
    success_url = reverse_lazy('mimicry_artist_list')
    login_url = 'login'
