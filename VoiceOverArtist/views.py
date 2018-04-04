# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create voiceoverartist Here

class VoiceOverArtistCreateView(LoginRequiredMixin, CreateView):
    model = models.VoiceOverArtist
    
    template_name = 'voiceoverartist/voiceoverartist_new.html'
    login_url = 'login'


    # Decide fields for taking input Here

    fields = ['VoiceOverArtist_Voice_Over_Artist',
'VoiceOverArtist_Charges_Available',
'VoiceOverArtist_Daily_Charges',
'VoiceOverArtist_Description',
'VoiceOverArtist_Language',
'VoiceOverArtist_Voice_Over_Artist_ID',
'VoiceOverArtist_Voice_Scale',
'VoiceOverArtist_Voice_Over_Artist_Message',
]

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# voiceoverartist Details Here


class VoiceOverArtistDetailView(LoginRequiredMixin, DetailView):
    model = models.VoiceOverArtist
    template_name = 'voiceoverartist/voiceoverartist_detail.html'
    login_url = 'login'

# voiceoverartist ListView Here


class VoiceOverArtistListView(ListView):
    model = models.VoiceOverArtist
    template_name = 'voiceoverartist/voiceoverartist_list.html'
    login_url = 'login'

# voiceoverartist Update Here


class VoiceOverArtistUpdateView(LoginRequiredMixin, UpdateView):
    model = models.VoiceOverArtist

    # Decide fields for editing Here

    
    fields = ['VoiceOverArtist_Voice_Over_Artist',
'VoiceOverArtist_Charges_Available',
'VoiceOverArtist_Daily_Charges',
'VoiceOverArtist_Description',
'VoiceOverArtist_Language',
'VoiceOverArtist_Voice_Over_Artist_ID',
'VoiceOverArtist_Voice_Scale',
'VoiceOverArtist_Voice_Over_Artist_Message',
]
    template_name = 'voiceoverartist/voiceoverartist_update.html'
    login_url = 'login'

# voiceoverartist Delete here


class VoiceOverArtistDeleteView(LoginRequiredMixin, DeleteView):
    model = models.VoiceOverArtist
    template_name = 'voiceoverartist/voiceoverartist_delete.html'
    success_url = reverse_lazy('voiceoverartist_list')
    login_url = 'login'



