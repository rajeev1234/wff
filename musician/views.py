# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create musician Here

class MusicianCreateView(LoginRequiredMixin, CreateView):
    model = models.Musician
    template_name = 'musician/musician_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Musician_Daily_Charges','Musician_Description','Musician_Financial_Available','Musician_Genre']

    # Set fields from current data or automated data
    #
    def form_valid(self, form):
        form.instance.Musician_Author = self.request.user
        return super().form_valid(form)

# musician Details Here


class MusicianDetailView(LoginRequiredMixin, DetailView):
    model = models.Musician
    context_object_name = 'Musician'
    template_name = 'musician/musician_detail.html'
    login_url = 'login'

# musician ListView Here


class MusicianListView(ListView):
    model = models.Musician
    template_name = 'musician/musician_list.html'
    login_url = 'login'

# musician Update Here


class MusicianUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Musician

    # Decide fields for editing Here

    fields = ['Musician_Daily_Charges','Musician_Description','Musician_Financial_Available','Musician_Genre']
    template_name = 'musician/musician_update.html'
    login_url = 'login'

# musician Delete here


class MusicianDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Musician
    template_name = 'musician/musician_delete.html'
    success_url = reverse_lazy('musician_list')
    login_url = 'login'
