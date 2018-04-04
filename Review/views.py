from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create Review Here

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = models.Review
    template_name = 'Review/Review_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Review_Rating','Review_Text','Review_Creator']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.Review_Author = self.request.user
        return super().form_valid(form)

# Review Details Here


class ReviewDetailView(LoginRequiredMixin, DetailView):
    model = models.Review
    template_name = 'Review/Review_detail.html'
    login_url = 'login'

# Review ListView Here


class ReviewListView(ListView):
    model = models.Review
    template_name = 'Review/Review_list.html'
    login_url = 'login'

# Review Update Here


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Review

    # Decide fields for editing Here

    fields = ['Review_Rating','Review_Text','Review_Creator']
    template_name = 'Review/Review_update.html'
    login_url = 'login'

# Review Delete here


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Review
    template_name = 'Review/Review_delete.html'
    success_url = reverse_lazy('Review_list')
    login_url = 'login'



