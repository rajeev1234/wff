# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create search Here

class searchCreateView(LoginRequiredMixin, CreateView):
    model = models.Search
    template_name = 'search/search_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Search_City','Search_Key_Word','Search_Range','Search_Creator']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.search_Author = self.request.user
        return super().form_valid(form)

# search Details Here


class searchDetailView(LoginRequiredMixin, DetailView):
    model = models.Search
    template_name = 'search/search_detail.html'
    login_url = 'login'

# search ListView Here


class searchListView(ListView):
    model = models.Search
    template_name = 'search/search_list.html'
    login_url = 'login'

# search Update Here


class searchUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Search

    # Decide fields for editing Here

    fields = ['Search_City','Search_Key_Word','Search_Range','Search_Creator']
    template_name = 'search/search_update.html'
    login_url = 'login'

# search Delete here


class searchDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Search
    template_name = 'search/search_delete.html'
    success_url = reverse_lazy('search_list')
    login_url = 'login'



