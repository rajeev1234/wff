# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create booking Here

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = models.Booking
    template_name = 'booking/booking_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Booking_Status']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# booking Details Here


class BookingDetailView(LoginRequiredMixin, DetailView):
    model = models.Booking
    template_name = 'booking/booking_detail.html'
    login_url = 'login'

# booking ListView Here


class BookingListView(ListView):
    model = models.Booking
    template_name = 'booking/booking_list.html'
    login_url = 'login'

# booking Update Here


class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Booking

    # Decide fields for editing Here

    fields = ['Booking_Status']
    template_name = 'booking/booking_update.html'
    login_url = 'login'

# booking Delete here


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Booking
    template_name = 'booking/booking_delete.html'
    success_url = reverse_lazy('booking_list')
    login_url = 'login'



