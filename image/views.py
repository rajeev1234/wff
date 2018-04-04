# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create images Here

class imagesCreateView(LoginRequiredMixin, CreateView):
    model = models.images
    template_name = 'images/images_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['my_image','owned_by']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.images_Author = self.request.user
        return super().form_valid(form)

# images Details Here


class imagesDetailView(LoginRequiredMixin, DetailView):
    model = models.images
    template_name = 'images/images_detail.html'
    login_url = 'login'

# images ListView Here


class imagesListView(ListView):
    model = models.images
    template_name = 'images/images_list.html'
    login_url = 'login'

# images Update Here


class imagesUpdateView(LoginRequiredMixin, UpdateView):
    model = models.images

    # Decide fields for editing Here

    fields = ['owned_by','my_image']
    template_name = 'images/images_update.html'
    login_url = 'login'

# images Delete here


class imagesDeleteView(LoginRequiredMixin, DeleteView):
    model = models.images
    template_name = 'images/images_delete.html'
    success_url = reverse_lazy('images_list')
    login_url = 'login'





# Create your views here.
