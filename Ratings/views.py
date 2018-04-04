# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create Rating Here

class RatingCreateView(LoginRequiredMixin, CreateView):
    model = models.Rating
    template_name = 'Rating/Rating_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Rating','Rating_User_ID','Rating_Creator']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.Rating_Author = self.request.user
        return super().form_valid(form)

# Rating Details Here


class RatingDetailView(LoginRequiredMixin, DetailView):
    model = models.Rating
    template_name = 'Rating/Rating_detail.html'
    login_url = 'login'

# Rating ListView Here


class RatingListView(ListView):
    model = models.Rating
    template_name = 'Rating/Rating_list.html'
    login_url = 'login'

# Rating Update Here


class RatingUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Rating

    # Decide fields for editing Here

    fields = ['Rating','Rating_User_ID','Rating_Creator']
    template_name = 'Rating/Rating_update.html'
    login_url = 'login'

# Rating Delete here


class RatingDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Rating
    template_name = 'Rating/Rating_delete.html'
    success_url = reverse_lazy('Rating_list')
    login_url = 'login'



