# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create portfolio_element Here

class PortfolioElementCreateView(LoginRequiredMixin, CreateView):
    model = models.PortfolioElement
    template_name = 'portfolio_element/portfolio_element_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['PortfolioElement_Category','PortfolioElement_Director','PortfolioElement_Production_House','PortfolioElement_Title']

    # Set fields from current data or automated data
    #
    def form_valid(self, form):
        form.instance.PortfolioElement_Author = self.request.user
        return super().form_valid(form)

# portfolio_element Details Here


class PortfolioElementDetailView(LoginRequiredMixin, DetailView):
    model = models.PortfolioElement
    context_object_name = 'PortfolioElement'
    template_name = 'portfolio_element/portfolio_element_detail.html'
    login_url = 'login'

# portfolio_element ListView Here


class PortfolioElementListView(ListView):
    model = models.PortfolioElement
    template_name = 'portfolio_element/portfolio_element_list.html'
    login_url = 'login'

# portfolio_element Update Here


class PortfolioElementUpdateView(LoginRequiredMixin, UpdateView):
    model = models.PortfolioElement

    # Decide fields for editing Here

    fields = ['PortfolioElement_Category','PortfolioElement_Director','PortfolioElement_Production_House','PortfolioElement_Title']
    template_name = 'portfolio_element/portfolio_element_update.html'
    login_url = 'login'

# portfolio_element Delete here


class PortfolioElementDeleteView(LoginRequiredMixin, DeleteView):
    model = models.PortfolioElement
    template_name = 'portfolio_element/portfolio_element_delete.html'
    success_url = reverse_lazy('portfolio_element_list')
    login_url = 'login'
