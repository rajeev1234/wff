from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create Costume Here

class CostumeCreateView(LoginRequiredMixin, CreateView):
    model = models.Costume
    template_name = 'Costumes/Costume_new.html'
    login_url = 'login'

# Decide fields for taking input Here

    fields = [  
                    'Costume_Color',
                    'Costume_Category',
                    'Costume_Style',
                    'Costume_Type',
                    'Costume_Description',
                    'Costume_Modification_Allowed',
                    'Costume_Trend_Year',
                    'Costume_Weekly_Rent',
                    'Costume_Creator',
                ]

# Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.Costume_Author = self.request.user
        return super().form_valid(form)

# Costume Details Here


class CostumeDetailView(LoginRequiredMixin, DetailView):
    model = models.Costume
    context_object_name = 'Costume'
    template_name = 'Costumes/Costume_details.html'
    login_url = 'login'

# Costume ListView Here


class CostumeListView(ListView):
    model = models.Costume
    template_name = 'Costumes/Costume_list.html'
    login_url = 'login'

# Costume Update Here


class CostumeUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Costume

    # Decide fields for editing Here
    fields = [  
                    'Costume_Color',
                    'Costume_Category',
                    'Costume_Type',
                    'Costume_Style',
                    'Costume_Description',
                    'Costume_Modification_Allowed',
                    'Costume_Trend_Year',
                    'Costume_Weekly_Rent',
                    'Costume_Creator',
                ]
    template_name = 'Costumes/Costume_update.html'
    login_url = 'login'

# Costume Delete here


class CostumeDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Costume
    template_name = 'Costumes/Costume_delete.html'
    success_url = reverse_lazy('Costume_list')
    login_url = 'login'



