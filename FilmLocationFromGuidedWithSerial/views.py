# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create FilmLocationFromGuidedWithSerial Here

class FilmLocationFromGuidedWithSerialCreateView(LoginRequiredMixin, CreateView):
    model = models.FilmLocationFromGuidedWithSerial
    template_name = 'FilmLocationFromGuidedWithSerials/FilmLocationFromGuidedWithSerial_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = [
            'FilmLocationFromGuidedWithSerial_Arrival_Time',
            'FilmLocationFromGuidedWithSerial_Departure_Time',
            'FilmLocationFromGuidedWithSerial_Location_From_Guideno',
            'FilmLocationFromGuidedWithSerial_Location',
            'FilmLocationFromGuidedWithSerial_Creator',
            ]

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.FilmLocationFromGuidedWithSerial_Author = self.request.user
        return super().form_valid(form)

# FilmLocationFromGuidedWithSerial Details Here


class FilmLocationFromGuidedWithSerialDetailView(LoginRequiredMixin, DetailView):
    model = models.FilmLocationFromGuidedWithSerial
    context_object_name = 'FilmLocationFromGuidedWithSerial'
    template_name = 'FilmLocationFromGuidedWithSerials/FilmLocationFromGuidedWithSerial_details.html'
    login_url = 'login'

# FilmLocationFromGuidedWithSerial ListView Here


class FilmLocationFromGuidedWithSerialListView(ListView):
    model = models.FilmLocationFromGuidedWithSerial
    template_name = 'FilmLocationFromGuidedWithSerials/FilmLocationFromGuidedWithSerial_list.html'
    login_url = 'login'

# FilmLocationFromGuidedWithSerial Update Here


class FilmLocationFromGuidedWithSerialUpdateView(LoginRequiredMixin, UpdateView):
    model = models.FilmLocationFromGuidedWithSerial

    # Decide fields for editing Here
    fields = [
            'FilmLocationFromGuidedWithSerial_Arrival_Time',
            'FilmLocationFromGuidedWithSerial_Departure_Time',
            'FilmLocationFromGuidedWithSerial_Location_From_Guideno',
            'FilmLocationFromGuidedWithSerial_Location',
            'FilmLocationFromGuidedWithSerial_Creator',
            ]

    template_name = 'FilmLocationFromGuidedWithSerials/FilmLocationFromGuidedWithSerial_update.html'
    login_url = 'login'

# FilmLocationFromGuidedWithSerial Delete here


class FilmLocationFromGuidedWithSerialDeleteView(LoginRequiredMixin, DeleteView):
    model = models.FilmLocationFromGuidedWithSerial
    template_name = 'FilmLocationFromGuidedWithSerials/FilmLocationFromGuidedWithSerial_delete.html'
    success_url = reverse_lazy('FilmLocationFromGuidedWithSerial_list')
    login_url = 'login'



