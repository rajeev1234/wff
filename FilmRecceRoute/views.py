# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create FilmRecceRoute Here

class FilmRecceRouteCreateView(LoginRequiredMixin, CreateView):
    model = models.FilmRecceRoute
    template_name = 'FilmRecceRoutes/FilmRecceRoute_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = [
            'FilmRecceRoute_Distance',
            'FilmRecceRoute_Filmrecce_Name',
            'FilmRecceRoute_Route_Name',
            'FilmRecceRoute_Travel_Time',
            'FilmRecceRoute_Creator',
            ]

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.FilmRecceRoute_Author = self.request.user
        return super().form_valid(form)

# FilmRecceRoute Details Here


class FilmRecceRouteDetailView(LoginRequiredMixin, DetailView):
    model = models.FilmRecceRoute
    context_object_name = 'FilmRecceRoute'
    template_name = 'FilmRecceRoutes/FilmRecceRoute_details.html'
    login_url = 'login'

# FilmRecceRoute ListView Here


class FilmRecceRouteListView(ListView):
    model = models.FilmRecceRoute
    template_name = 'FilmRecceRoutes/FilmRecceRoute_list.html'
    login_url = 'login'

# FilmRecceRoute Update Here


class FilmRecceRouteUpdateView(LoginRequiredMixin, UpdateView):
    model = models.FilmRecceRoute

    # Decide fields for editing Here


    fields = [
            'FilmRecceRoute_Distance',
            'FilmRecceRoute_Filmrecce_Name',
            'FilmRecceRoute_Route_Name',
            'FilmRecceRoute_Travel_Time',
            'FilmRecceRoute_Creator',
            ]
                        
    template_name = 'FilmRecceRoutes/FilmRecceRoute_update.html'
    login_url = 'login'

# FilmRecceRoute Delete here


class FilmRecceRouteDeleteView(LoginRequiredMixin, DeleteView):
    model = models.FilmRecceRoute
    template_name = 'FilmRecceRoutes/FilmRecceRoute_delete.html'
    success_url = reverse_lazy('FilmRecceRoute_list')
    login_url = 'login'



