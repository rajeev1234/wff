# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create FilmRecceTourGuide Here

class FilmRecceTourGuideCreateView(LoginRequiredMixin, CreateView):
    model = models.FilmRecceTourGuide
    template_name = 'FilmRecceTourGuides/FilmRecceTourGuide_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = [
            'FilmRecceTourGuide_EndLocation',
            'FilmRecceTourGuide_EndTime',
            'FilmRecceTourGuide_Passing_Year',
            # 'FilmRecceTourGuide_guidedlocation_List'
            'FilmRecceTourGuide_StartLocation',
            'FilmRecceTourGuide_StartTime',
            'FilmRecceTourGuide_TourGuideName',
            'FilmRecceTourGuide_Creator']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.FilmRecceTourGuide_Author = self.request.user
        return super().form_valid(form)

# FilmRecceTourGuide Details Here


class FilmRecceTourGuideDetailView(LoginRequiredMixin, DetailView):
    model = models.FilmRecceTourGuide
    context_object_name = 'FilmRecceTourGuide'
    template_name = 'FilmRecceTourGuides/FilmRecceTourGuide_details.html'
    login_url = 'login'

# FilmRecceTourGuide ListView Here


class FilmRecceTourGuideListView(ListView):
    model = models.FilmRecceTourGuide
    template_name = 'FilmRecceTourGuides/FilmRecceTourGuide_list.html'
    login_url = 'login'

# FilmRecceTourGuide Update Here


class FilmRecceTourGuideUpdateView(LoginRequiredMixin, UpdateView):
    model = models.FilmRecceTourGuide

    # Decide fields for editing Here

    fields = [
            'FilmRecceTourGuide_EndLocation',
            'FilmRecceTourGuide_EndTime',
            'FilmRecceTourGuide_Passing_Year',
            # 'FilmRecceTourGuide_guidedlocation_List'
            'FilmRecceTourGuide_StartLocation',
            'FilmRecceTourGuide_StartTime',
            'FilmRecceTourGuide_TourGuideName',
            'FilmRecceTourGuide_Creator']

    template_name = 'FilmRecceTourGuides/FilmRecceTourGuide_update.html'
    login_url = 'login'

# FilmRecceTourGuide Delete here


class FilmRecceTourGuideDeleteView(LoginRequiredMixin, DeleteView):
    model = models.FilmRecceTourGuide
    template_name = 'FilmRecceTourGuides/FilmRecceTourGuide_delete.html'
    success_url = reverse_lazy('FilmRecceTourGuide_list')
    login_url = 'login'



