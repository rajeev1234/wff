# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create Letter_pdf Here

class Letter_pdfCreateView(LoginRequiredMixin, CreateView):
    model = models.Letter_pdf
    template_name = 'Letter_pdf/Letter_pdf_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Letter_pdf_Addressing_Officer','Letter_pdf_Project','Letter_pdf_Creator']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.Letter_pdf_Author = self.request.user
        return super().form_valid(form)

# Letter_pdf Details Here


class Letter_pdfDetailView(LoginRequiredMixin, DetailView):
    model = models.Letter_pdf
    template_name = 'Letter_pdf/Letter_pdf_detail.html'
    login_url = 'login'

# Letter_pdf ListView Here


class Letter_pdfListView(ListView):
    model = models.Letter_pdf
    template_name = 'Letter_pdf/Letter_pdf_list.html'
    login_url = 'login'

# Letter_pdf Update Here


class Letter_pdfUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Letter_pdf

    # Decide fields for editing Here

    fields = ['Letter_pdf_Addressing_Officer','Letter_pdf_Project','Letter_pdf_Creator']
    template_name = 'Letter_pdf/Letter_pdf_update.html'
    login_url = 'login'

# Letter_pdf Delete here


class Letter_pdfDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Letter_pdf
    template_name = 'Letter_pdf/Letter_pdf_delete.html'
    success_url = reverse_lazy('Letter_pdf_list')
    login_url = 'login'



